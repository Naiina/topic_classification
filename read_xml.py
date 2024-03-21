import xml.etree.ElementTree as ET
import torch
import os
import numpy as np
import pickle
import matplotlib.pyplot as plt
from torcheval.metrics.functional import multiclass_f1_score
from sklearn.metrics import precision_recall_fscore_support


#tree = ET.parse('52FRF-G38GNT-07M0400.xml')
#root = tree.getroot()
#for child in root:

#    print(child.tag, child.attrib)

#for elem in root.iter('event'):

    #print(elem.text)




def get(property,file):
    tree = ET.parse(file)
    root = tree.getroot()

    for elem in root.iter('tier'):
        dict = elem.attrib
        if property in dict.values():
            return dict

def get_sentence(file):
    sent = ""
    tree = ET.parse(file)
    root = tree.getroot()

    for elem in root.iter('event'):
        dict = elem.attrib
        sent = sent + " "+ elem.text 
        if dict['end'] == 'T1':
            break
    return sent

def get_translation(file):
    tree = ET.parse(file)
    root = tree.getroot()
    for elem in root.iter('tier'):
        d = elem.attrib
        if "translation" in d.values():
            for it in elem.iter("event"):
                trans = it.text
                break
    return trans

def get_d_sentence_pcc2(file):
    # sent: concatenation of all tokens, d_sent[Tk] = token nb k
    tree = ET.parse(file)
    root = tree.getroot()
    sent = ""
    d_sent = {}
    for elem in root.iter('tier'):
        d = elem.attrib
        if "tok" in d.values():
            for it in elem.iter("event"):
                tok = it.text
                sent = sent + " " + tok
                start = it.attrib["start"]
                d_sent[start] = tok
            break
    return sent,d_sent

def get_topics_idx(file,tup=False):
    #index of all tokens considered as topic in the file
    tree = ET.parse(file)
    root = tree.getroot()
    l_topic_idx = []
    l_tuple = []
    for elem in root.iter('tier'):
        d = elem.attrib
        if "TOPIC" in d.values():
            for it in elem.iter("event"):
                if it.text == "AB":
                    start = it.attrib["start"][1:]
                    end = it.attrib["end"][1:]
                    l_tuple.append((int(start),int(end)))
                    for i in range(int(start),int(end)):
                        l_topic_idx.append(i)
    
    if tuple:
        return l_tuple
    else:
        return l_topic_idx
    
def get_noun_idx(file):
    #l_files = os.listdir(pcc2_data_folder)
    l_noun_idx = []
    tree = ET.parse(file)
    root = tree.getroot()
    nb = 0
    for elem in root.iter('tier'):
        d = elem.attrib
        if "pos" in d.values():
            for it in elem.iter("event"):
                if it.text == "NN" or it.text == "NE" or it.text == "PPER":
                    idx = it.attrib["start"][1:]
                    l_noun_idx.append(int(idx))
            break
    #print(l_noun_idx)
    return l_noun_idx



#def  topic_distribution(file):
#    sent,d_sent = get_d_sentence_pcc2(file)
#    sent_en = len(d_sent)
#    l_topic_idx_tuple = get_topics_idx(file,tup=True)
#    for a,b in l_topic_idx_tuple:






def get_verb_idx(file):
    #l_files = os.listdir(pcc2_data_folder)
    l_v_idx = []
    tree = ET.parse(file)
    root = tree.getroot()
    nb = 0
    for elem in root.iter('tier'):
        d = elem.attrib
        if "pos" in d.values():
            for it in elem.iter("event"):
                if it.text[0] == "V":
                    idx = it.attrib["start"][1:]
                    l_v_idx.append(int(idx))
            break
    #print(l_noun_idx)
    return l_v_idx



def create_label_list(file,data_size,nb_zeros,nb_ones):
    #labels: 0 for nouns/proper nouns/pronouns which are not topics, 
    #1 for the nouns/proper nouns/pronouns which are topics. 
    #-100 otherwise 
    sent,d_sent = get_d_sentence_pcc2(file)
    l_topic_idx = get_topics_idx(file)
    l_noun_idx = get_noun_idx(file)
    #print("topic",l_topic_idx)
    #print("nouns",l_noun_idx)
    #l_label = [0]#corresponds to the begining token
    l_label = []
    for i in range(data_size-2): 
        if i in l_topic_idx and i in l_noun_idx:
            l_label.append(1)
            nb_ones+=1
        elif i in l_noun_idx:
            l_label.append(0)
            nb_zeros+=1
        else:
            l_label.append(-100)
    #l_label.append(0) #to match the end token
    return l_label,nb_zeros, nb_ones

def verify_label_list(file):
    sent,d_sent = get_d_sentence_pcc2(file)
    l_label = create_label_list(file)
    for i,elem in enumerate(l_label):
        if elem == 1:
            print(d_sent["T"+str(i)])


def get_nb_token(file):
    
    tree = ET.parse(file)
    root = tree.getroot()

    for elem in root.iter('tier'):
        d = elem.attrib
        if "tok" in d.values():
            l = [0 for k in elem.iter("event")] 
            break
    
    return len(l)

def get_nb_tok_all_files(pcc2_data_folder):
    l_files = os.listdir(pcc2_data_folder)
    l = [get_nb_token(pcc2_data_folder + "/"+ file ) for file in l_files]
    return l


def get_nb_topic_all_files(pcc2_data_folder):
    l_files = os.listdir(pcc2_data_folder)
    l_topic_tok = []

    for elem in l_files:
        file = pcc2_data_folder + "/"+elem
        tree = ET.parse(file)
        root = tree.getroot()
        nb = 0
        for elem in root.iter('tier'):
            d = elem.attrib
            if "TOPIC" in d.values():
                for it in elem.iter("event"):
                    if it.text == "AB":
                        nb += 1 
                break
        l_topic_tok.append(nb)
    
    return l_topic_tok


def get_weight(pcc2_data_folder):
    print("probably buggy")
    l_noun= get_noun_idx(pcc2_data_folder)
    l_topic = get_nb_topic_all_files(pcc2_data_folder)

    nb_tot_nouns = sum(l_noun)
    nb_tot_topic = sum(l_topic)

    pos_weight = nb_tot_nouns / (nb_tot_topic * 2)
    neg_weight = nb_tot_nouns / ((nb_tot_nouns-nb_tot_topic) * 2)
    
    weight_tensor = torch.tensor([pos_weight,neg_weight])
    return weight_tensor

def compute_weight(nb_zeros, nb_ones):
    tot = nb_zeros + nb_ones
    pos_weight = tot / (nb_ones * 2)
    neg_weight = tot / (nb_zeros * 2)
    
    weight_tensor = torch.tensor([neg_weight,pos_weight])
    return weight_tensor

def get_nouns_all_files(pcc2_data_folder):
    l_files = os.listdir(pcc2_data_folder)
    l_tot = []
    for file in l_files:
        l_tot = l_tot + get_noun_idx(file)



def plot_pkl(loss_file):

    d_train, d_test = compute_accuracy(loss_file)



    figure, axis = plt.subplots(2, 4) 
  
    # train set plots 
    axis[0, 0].plot(d_train["train_loss"]) 
    axis[0, 0].set_title("train set loss") 

    axis[0, 1].plot(d_train["l_precision_train"]) 
    axis[0, 1].set_title("train set precision") 

    axis[0, 2].plot(d_train["l_recall_train"]) 
    axis[0, 2].set_title("train set recall") 

    axis[0, 3].plot(d_train["l_f_score_train"]) 
    axis[0, 3].set_title("train set F1 score") 

    # test set plots 
    axis[1, 0].plot(d_test["train_loss"]) 
    axis[1, 0].set_title("test set loss") 

    axis[1, 1].plot(d_test["l_precision_test"]) 
    axis[1, 1].set_title("test set precision") 

    axis[1, 2].plot(d_test["l_recall_test"]) 
    axis[1, 2].set_title("test set recall") 

    axis[1, 3].plot(d_test["l_f_score_test"]) 
    axis[1, 3].set_title("test set F1 score") 

    

    



    plt.show() 





def compute_accuracy(loss_file):
    with open(loss_file, 'rb') as f:
        d_loss = pickle.load(f)

    l_precision_train = []
    l_precision_test = []
    l_recall_train = []
    l_recall_test = []
    l_f_score_train = []
    l_f_score_test = []

    for i,elem in enumerate(d_loss["train_labels"]):
        prediction_train = d_loss["train_pred"][i]
        score_train = precision_recall_fscore_support(torch.tensor(prediction_train), torch.tensor(elem), average='micro')
        f1_score_train = multiclass_f1_score(torch.tensor(prediction_train), torch.tensor(elem), num_classes = 2)
        l_precision_train.append(score_train[0])
        l_recall_train.append(score_train[1])
        l_f_score_train.append(f1_score_train)
    d_train_scores = {"l_precision_train":l_precision_train,"l_recall_train":l_recall_train,"l_f_score_train":l_f_score_train,"loss_train":d_loss["loss_train"]}

    for i,elem in enumerate(d_loss["test_labels"]):
        prediction_test = d_loss["test_pred"][i]
        score_test = precision_recall_fscore_support(torch.tensor(prediction_test), torch.tensor(elem), average='micro')
        f1_score_test = multiclass_f1_score(torch.tensor(prediction_test), torch.tensor(elem), num_classes = 2)
        l_precision_test.append(score_test[0])
        l_recall_test.append(score_test[1])
        l_f_score_test.append(f1_score_test)
    d_test_scores = {"l_precision_test":l_precision_test,"l_recall_test":l_recall_test,"l_f_score_test":l_f_score_test,"loss_test":d_loss["loss_test"]}
    return d_train_scores, d_test_scores

def check_all_topic_are_nn(pcc2_data_folder):
    print("To fix")
    l_files = os.listdir(pcc2_data_folder)
    empty_all = 0
    empty_nn = 0
    for elem in l_files:
        print(elem)
        file = pcc2_data_folder + "/" + elem
        l_nn = get_noun_idx(file)
        l_top_tuple = get_topics_idx(file,tup=True)
        l_v = get_verb_idx(file)
        for start,end in l_top_tuple:
            l_idx_top = range(start,end)
            S_top = set(l_idx_top)
            S_nn = set(l_nn)
            S_v = set(l_v)
            S_v_nn = S_nn.union(S_v)
            
            inter_nn = S_top.intersection(S_nn)
            inter_all = S_top.intersection(S_v_nn)
            print(inter_nn)
            print(inter_all)
            if len(inter_nn)==0:
                empty_nn+=1
            if len(inter_all)==0:
                empty_all+=1
        print(empty_all-empty_nn)
            
    print(empty_nn/empty_all)


#label = create_label_list("pcc2_data/maz-4282.exb",100)
#print(label)

#if __name__ == 'main':
    
   
l_batch = [16,32]
l_lr = [5e-6, 2e-5, 5e-5]
l_batch = [32,64]
#l_lr = [5e-6, 2e-5]
for batch in l_batch:
    for lr in l_lr:
        plot_pkl("loss/loss_grid_search_lr_"+str(lr)+"_bs_"+str(batch)+"_10ep.pkl")

