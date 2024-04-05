import argparse
import csv
import numpy as np
import os
#import pandas as pd
import pickle
import sys
import torch
#import conllu
#from transformers import BertTokenizer, BertModel, BertForMaskedLM
#from collections import defaultdict, Counter
from tqdm import tqdm
import torch.nn as nn
import numpy as np
import torch.optim as optim
import torch.utils.data as data
from read_xml import create_label_list, get_d_sentence_pcc2, compute_weight, get_nb_tok_all_files, get_nb_topic_all_files, cut_data_into_sentences
import os
import random
import neptune
from sklearn.metrics import f1_score
from sklearn.metrics import precision_recall_fscore_support
import json


#from transformers import AutoTokenizer, XLMRobertaModel
from transformers import AutoTokenizer, BertForTokenClassification


BERT_DIM = 768
#UD_path = "ud-treebanks-v2.13/"  
#d_lang = {"fr":"UD_French-PUD"}
#lang = "fr"
load_bert = True
weighted_loss = False
debug = False
early_stopping = False
nept = False


pcc2_data_folder = "pcc2_data"



parser = argparse.ArgumentParser()
parser.add_argument('--out_file', type=str)
parser.add_argument('--lr_file', type=str)
args = parser.parse_args()
out_file = args.out_file
if type(args.lr_file)==str:
    lr_file = "l_lr/"+args.lr_file
    with open(lr_file, 'r') as openfile:   
        l_lr = json.load(openfile)
else:
    l_lr = [5e-5]
print("learning rate:", l_lr)



if debug:
    data_max_lenght = 7
    l_batch = [2]
    #l_lr = [10e-3]
    nb_epochs = 2
else:
    #data_max_lenght = max(get_nb_tok_all_files(pcc2_data_folder))
    data_max_lenght = 60 #max nb of tokens in a sentence 
    nb_epochs = 100
    l_batch = [1]
    print("batch_size", l_batch)


def get_data(pcc2_data_folder,data_max_lenght,debug,l_tags):
    l_files = os.listdir(pcc2_data_folder)
    random.shuffle(l_files)
    train_size = int(len(l_files)*0.8)
    l_files_train = l_files[:train_size]
    l_files_test = l_files[train_size:]
    l_sent_train = []
    l_labels_train = []
    l_sent_test = []
    l_labels_test = []
    
    max_lenght = 0
    for elem in l_files_train:
        file = pcc2_data_folder+"/"+elem
        #sent,d_sent = get_d_sentence_pcc2(file)
        labels = create_label_list(file,data_max_lenght,l_tags)
        ll_sent, ll_lab, max_lenght_one = cut_data_into_sentences(file,labels,data_max_lenght)
        max_lenght = max(max_lenght_one,max_lenght)
        #for elem in ll_sent:
        l_sent_train=l_sent_train+ll_sent
        #for elem in ll_lab:
        l_labels_train=l_labels_train+ll_lab
    
    for elem in l_files_test:
        file = pcc2_data_folder+"/"+elem
        #sent,d_sent = get_d_sentence_pcc2(file)
        labels = create_label_list(file,data_max_lenght,l_tags)
        ll_sent_test, ll_lab_test, max_lenght_one = cut_data_into_sentences(file,labels,data_max_lenght)
        #for elem in ll_sent_test:
        l_sent_test=l_sent_test+ll_sent_test
        #for elem in ll_lab_test:
        l_labels_test=l_labels_test+ll_lab_test
        max_lenght = max(max_lenght_one,max_lenght)
    print("max_lenght_sequ",max_lenght)
    if debug:
        l_sent_train = ["the cat ate the mouse.","I.","the cat ate the mouse the mouse the mouse.","I am."]
        l_labels_train = [[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        l_sent_test = ["the cat ate the mouse.","I am green and blue.","the cat ate the mouse.","I am green and blue."]
        l_labels_test = [[0,1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0]]
    
    
    return l_sent_train,l_labels_train, l_sent_test,l_labels_test


class LabelDataset(data.Dataset):
    def __init__(self, l_sent, l_labels):
      self.l_labels = l_labels
      self.l_sent = l_sent
      

    def __getitem__(self, idx):
        return self.l_sent[idx], self.l_labels[idx]

    #def __getitem__(self, idx):
    #    return self.l_sent[idx], idx

    def __len__(self):
      return len(self.l_sent)
    
    def get_dataloader(self, batch_size, shuffle=True):
      return data.DataLoader(self, batch_size, shuffle=shuffle)

class _classifier(nn.Module):
    def __init__(self, nlabels):
        super(_classifier, self).__init__()
        self.main = nn.Sequential(
            nn.Linear(BERT_DIM, 64),
            nn.ReLU(),
            nn.Linear(64, nlabels),
            nn.Dropout(.1)
        )
    def forward(self, input):
        return self.main(input)
    



def get_path(d_lang,lang,UD_path):
    return  UD_path+"/"+d_lang[lang] +"/"+d_lang[lang].lower() +"-test.conllu"


def detach_and_flatten(l_tensor):
    n_pred = np.array([])
    for t in l_tensor:
        t_flat = torch.flatten(t)
        #print(t_flat)
        n_flat = t_flat.detach().numpy()
        #print(n_flat)
        n_pred = np.concatenate((n_pred, n_flat), axis=None)
        #print(n_pred)
    return n_pred


def align_labels(tok_batch,t_labels):
    #tokenized_inputs = tokenizer(examples["tokens"], truncation=True, is_split_into_words=True)
    
    l_aligned_labels = []
    for i, label in enumerate(t_labels):
        word_ids = tok_batch.word_ids(batch_index=i)  # Map tokens to their respective word.
        previous_word_idx = None
        label_ids = []
        #print("label",label)
        #print("word_id",word_ids)
        for word_idx in word_ids:  # Set the special tokens to -100.
            if word_idx is None:
                label_ids.append(-100)
            elif word_idx != previous_word_idx:  # Only label the first token of a given word.
                label_ids.append(label[word_idx])
            else:
                label_ids.append(-100)
            previous_word_idx = word_idx
        l_aligned_labels.append(label_ids)
        #print("label_ids",label_ids)
        #exit()
        
    return torch.tensor(l_aligned_labels)


def run_experiment(pcc2_data_folder,nb_epochs,batch_size,lr,data_max_lenght,out_file,load_bert=False,weighted_loss=True,debug=False):
                
    if load_bert:
        #tokenizer = AutoTokenizer.from_pretrained("FacebookAI/xlm-roberta-base")
        #model = XLMRobertaModel.from_pretrained("FacebookAI/xlm-roberta-base")
        tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-multilingual-cased")
        model = BertForTokenClassification.from_pretrained("google-bert/bert-base-multilingual-cased")

        print("model loaded")
    else:
        tokenizer = None
        model = None
        print("run without loading bert")

    l_tags = ["NN","NE","PPER","PDS"]
    l_sent_train,l_labels_train, l_sent_test,l_labels_test = get_data(pcc2_data_folder,data_max_lenght,debug,l_tags)
    print(l_sent_train[3])
    print(l_labels_train[3])
    #exit()
    

    #classifier = _classifier(2)
    #optimizer = optim.Adam(classifier.parameters())
    optimizer = optim.Adam(model.parameters(),lr=lr)
    if weighted_loss:
        print("Weighted loss")
        #nb_zeros = 8142-1736
        #nb_ones = 1736

        #weight_tensor = compute_weight(nb_zeros,nb_ones)
        weight_tensor = torch.tensor([10,0.5])

        print(weight_tensor)
        criterion = nn.CrossEntropyLoss(weight=weight_tensor)
    else:
        print("non weighted loss")
        criterion = nn.CrossEntropyLoss()
        weight_tensor = None

    #l_mean_loss_train = []
    #l_mean_loss_test = []
    #l_mean_fscore_train = []
    #l_mean_fscore_test = []
    all_labels_train = [] #tensor of all lebels over the epoch in the order of the batch to match all_pred
    all_pred_train = [] #tensor of all the predictions
    all_labels_test = [] 
    all_pred_test = [] 


    #run_nept = neptune.init_run(
    #project="naiina/topic-classifier",
    #api_token="eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vYXBwLm5lcHR1bmUuYWkiLCJhcGlfdXJsIjoiaHR0cHM6Ly9hcHAubmVwdHVuZS5haSIsImFwaV9rZXkiOiI5YzllNjM4MS0zYjBhLTQwNGUtOGM3Mi1hYjE3ZTVjOWVjMTgifQ==",
    #tags=["labels in scores","weighted loss"]
    #)
    if nept:
        run_nept = neptune.init_run(
        project="naiina/topic-classifier-more-epochs",
        api_token="eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vYXBwLm5lcHR1bmUuYWkiLCJhcGlfdXJsIjoiaHR0cHM6Ly9hcHAubmVwdHVuZS5haSIsImFwaV9rZXkiOiI5YzllNjM4MS0zYjBhLTQwNGUtOGM3Mi1hYjE3ZTVjOWVjMTgifQ==",
        tags=["sentences"]
        ) 
        #params = {"batch_szie": batch_size, "lr": lr}
        params = {"batch_szie": batch_size, "lr": lr}
        run_nept["parameters"] = params


    class EarlyStopper:
        def __init__(self, patience=1, min_delta=0):
            self.patience = patience
            self.min_delta = min_delta
            self.counter = 0
            self.min_validation_loss = float('inf')
    
        def early_stop(self, validation_loss):
            if validation_loss < self.min_validation_loss:
                self.min_validation_loss = validation_loss
                self.counter = 0
            elif validation_loss > (self.min_validation_loss + self.min_delta):
                self.counter += 1
                if self.counter >= self.patience:
                    return True
            return False
    early_stopper = EarlyStopper(patience=3, min_delta=0.02)

    for epoch in tqdm(range(nb_epochs), desc="epoch" ):

        #early_stop = 0
        #l=[0,0,0]
        #if epoch>10 and early_stop>3

        dataset_train = LabelDataset(l_sent_train,l_labels_train)
        dataloader_train = dataset_train.get_dataloader(batch_size) 
        #ll = next(iter(train_dataloader))
        train_features, train_labels = next(iter(dataloader_train))
        print(" train_features, train_labels", train_features, train_labels)
        l_loss_train = []
        #exit()

        dataset_test = LabelDataset(l_sent_test,l_labels_test)
        
        dataloader_test = dataset_test.get_dataloader(batch_size,shuffle=False) 
        #print("dataset_train",dataset_test[0])
        #exit()

        l_loss_test = []
        model.train()
        l_all_labels_one_ep_train = []
        l_all_pred_one_ep_train = []
        l_all_labels_one_ep_test = []
        l_all_pred_one_ep_test = []

        for sent_batch, label_batch in dataloader_train:
            print("TODO random samples")

            tok_batch = tokenizer(sent_batch, return_tensors="pt", padding=True) 
            print("padding in the dataloader: Data collator")
            print("label_batch",label_batch)
            t_labels = torch.stack(label_batch, dim=1)

            print("sent",sent_batch)
            print("tokenized sent", tok_batch)
            print("t_labels",t_labels)
            t_aligned_labels = align_labels(tok_batch,t_labels)
            print(t_aligned_labels)
            #print(tok_batch,t_labels)
            exit()

            
            if load_bert:
                out_logits = model(**tok_batch).logits # tensor of size nb_batch * nb_tok * nb_of_classes
                predicted_labels = out_logits.argmax(-1) # tensor of size nb_batch * nb_tok
            else:
                out_logits = torch.tensor([1,0,0])

            out_logits = torch.permute(out_logits, (0, 2, 1))
            
            sent_batch_size = out_logits.size()[-1]
            loss = criterion(out_logits, t_aligned_labels) 
            #l_f_score_train = compute_f1_score(predicted_labels,t_aligned_labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            l_loss_train.append(loss.data.mean().item())

            l_all_pred_one_ep_train.append(predicted_labels)
            l_all_labels_one_ep_train.append(t_aligned_labels)
        t_loss = np.mean(l_loss_train)
        print('[%d/%d] Train loss: %.3f' % (epoch+1, nb_epochs, t_loss))
        #print('[%d/%d] Train accuracy: %.3f' % (epoch+1, nb_epochs, np.mean(l_f_score_train)))

        #l_mean_loss_train.append(np.mean(l_loss_train))
        #l_mean_fscore_train.append(np.mean(l_f_score_train))
        
        
        
        flat_pred = detach_and_flatten(l_all_pred_one_ep_train)
        flat_labels = detach_and_flatten(l_all_labels_one_ep_train)
        #t_all_labels_one_ep_train = torch.tensor(l_all_labels_one_ep_train)
        #t_all_pred_one_ep_train = torch.tensor(l_all_pred_one_ep_train)
        if debug:
            print("epoch %d:" %epoch)
            print("flat pred: ", flat_pred)
            print("flat_lab: ", flat_labels)

        all_labels_train.append(flat_labels)
        all_pred_train.append(flat_pred)
        #t_all_labels_train = torch.tensor(all_labels_train)
        #t_all_pred_train = torch.tensor(all_pred_train)

        score_train = precision_recall_fscore_support(torch.tensor(flat_labels),torch.tensor(flat_pred), average='micro',labels = np.array([0,1]))
        f1_score_train = f1_score( torch.tensor(flat_labels), torch.tensor(flat_pred), labels = np.array([0,1]),average = 'micro')

        if nept:
            run_nept["precision_train"].append((score_train[0]))
            run_nept["recall_train"].append(score_train[1])
            run_nept["F1_score_train"].append(f1_score_train)
            run_nept["loss_train"].append(t_loss)
        

        model.eval()

        for sent_batch, label_batch in dataloader_test:
            #print(len(sent_batch),len(label_batch))
            
            tok_batch = tokenizer(sent_batch, return_tensors="pt", padding=True ) 

            t_labels = torch.stack(label_batch, dim=1)
            t_aligned_labels = align_labels(tok_batch,t_labels)

            #if load_bert:
            #    out_xlm = model(**tok_batch)
            #    last_h_layer = out_xlm.last_hidden_state
            #else:
            #    last_h_layer = torch.tensor([1,2,3])

            if load_bert:
                out_logits = model(**tok_batch).logits # tensor of size nb_batch * nb_tok * nb_of_classes
                predicted_labels = out_logits.argmax(-1) # tensor of size nb_batch * nb_tok
            else:
                out_logits = torch.tensor([1,0,0])


            out_logits = torch.permute(out_logits, (0, 2, 1))
            sent_batch_size = out_logits.size()[-1]
            #t_labels = torch.stack(label_batch, dim=1)
            

            loss = criterion(out_logits, t_aligned_labels) 
            #loss = criterion(out_logits, label_batch) 
            l_loss_test.append(loss.data.mean().item())
            #l_f_score_test = compute_f1_score(predicted_labels,t_aligned_labels)
            
            l_all_pred_one_ep_test.append(predicted_labels)
            l_all_labels_one_ep_test.append(t_aligned_labels)
        val_loss = np.mean(l_loss_test)
        print('[%d/%d] Eval loss: %.3f' % (epoch+1, nb_epochs, val_loss))

        flat_pred_test = detach_and_flatten(l_all_pred_one_ep_test)
        flat_labels_test = detach_and_flatten(l_all_labels_one_ep_test)
        
        all_labels_test.append(flat_labels_test)
        all_pred_test.append(flat_pred_test)

        score_test = precision_recall_fscore_support( torch.tensor(flat_labels_test), torch.tensor(flat_pred_test), average='micro', labels = np.array([0,1]))
        f1_score_test = f1_score(torch.tensor(flat_labels_test), torch.tensor(flat_pred_test),  labels = np.array([0,1]),average = 'micro')
        if nept:
            run_nept["precision_test"].append((score_test[0]))
            run_nept["recall_test"].append(score_test[1])
            run_nept["F1_score_test"].append(f1_score_test)
            run_nept["loss_test"].append(val_loss)

        d_loss={"train_labels":all_labels_train,"train_pred": all_pred_train, "test_label": all_labels_test,"test_pred": all_pred_test, "loss_train":l_loss_train,"loss_test":l_loss_test}
        if early_stopping:
            if early_stopper.early_stop(val_loss):             
                break
    with open(out_file, 'wb') as file: 
        pickle.dump(d_loss, file) 
    #print(d_loss)
    if nept:
        run_nept.stop()
    return None
            

  


#l_tok = get_nb_tok_all_files(pcc2_data_folder)
#l_topic = get_nb_topic_all_files(pcc2_data_folder)
#print(min(l_tok),max(l_tok),np.mean(np.array(l_tok)),sum(l_tok))
#print(min(l_topic),max(l_topic),np.mean(np.array(l_topic)),sum(l_topic))




for batch_size in tqdm(l_batch, desc="batch size"):
    for lr in tqdm(l_lr, desc="lr"):
        out_file_lr = "loss/"+out_file+"_lr_"+str(lr)+"_bs_"+str(batch_size)+".pkl"
        run_experiment(pcc2_data_folder,nb_epochs,batch_size,lr,data_max_lenght,out_file_lr,load_bert,weighted_loss,debug)



