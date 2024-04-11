import xml.etree.ElementTree as ET
import torch
import os
import numpy as np
import pickle
import matplotlib.pyplot as plt
from torcheval.metrics.functional import multiclass_f1_score
from sklearn.metrics import precision_recall_fscore_support
import json
import random


#tree = ET.parse('52FRF-G38GNT-07M0400.xml')
#root = tree.getroot()
#for child in root:

#    print(child.tag, child.attrib)

#for elem in root.iter('event'):

    #print(elem.text)
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

def get_data(pcc2_data_folder,data_max_lenght_sent,data_max_lenght_file,l_tags):
    l_files = os.listdir(pcc2_data_folder)
    random.shuffle(l_files)
    train_size = int(len(l_files)*0.8)
    l_files_train = l_files[:train_size]
    l_files_test = l_files[train_size:]
    l_sent_train = []
    l_labels_train = []
    l_sent_test = []
    l_labels_test = []
    l_id_train = []
    l_id_test = [] 
    
    max_lenght = 0
    for elem in l_files_train:
        file = pcc2_data_folder+"/"+elem
        labels = create_label_list(file,data_max_lenght_file,l_tags)
        ll_sent_train, ll_lab_train, max_lenght_one = cut_data_into_sentences(file,labels,data_max_lenght_sent)
        max_lenght = max(max_lenght_one,max_lenght)
        l_sent_train=l_sent_train+ll_sent_train
        l_labels_train=l_labels_train+ll_lab_train

        for i in range(len(ll_sent_train)):
            l_id_train.append(str(i)+elem[4:-4])
    
    for elem in l_files_test:
        file = pcc2_data_folder+"/"+elem
        labels = create_label_list(file,data_max_lenght_file,l_tags)
        ll_sent_test, ll_lab_test, max_lenght_one = cut_data_into_sentences(file,labels,data_max_lenght_sent)
        l_sent_test=l_sent_test+ll_sent_test
        l_labels_test=l_labels_test+ll_lab_test
        max_lenght = max(max_lenght_one,max_lenght)

        for i in range(len(ll_sent_test)):
            l_id_test.append(str(i)+elem[4:-4])
    print("max_lenght_sequ",max_lenght)

    #if debug:
    #    l_sent_train = ["the cat ate the mouse.","I.","the cat ate the mouse the mouse the mouse.","I am."]
    #    l_labels_train = [[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    #    l_sent_test = ["the cat ate the mouse.","I am green and blue.","the cat ate the mouse.","I am green and blue."]
    #    l_labels_test = [[0,1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0]]

    return l_sent_train,l_labels_train,l_id_train, l_sent_test,l_labels_test,l_id_test
    


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
    
    if tup:
        return l_tuple
    else:
        return l_topic_idx
    
def get_noun_idx(file,l_tags):
    #l_files = os.listdir(pcc2_data_folder)
    l_noun_idx = []
    tree = ET.parse(file)
    root = tree.getroot()
    nb = 0
    for elem in root.iter('tier'):
        d = elem.attrib
        if "pos" in d.values():
            for it in elem.iter("event"):
                if it.text in l_tags:
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
            #break
    #print(l_noun_idx)
    return l_v_idx



def get_ponct_idx(file):
    #l_files = os.listdir(pcc2_data_folder)
    l_ponct_idx = []
    tree = ET.parse(file)
    root = tree.getroot()
    #nb = 0
    for elem in root.iter('tier'):
        d = elem.attrib
        if "pos" in d.values():
            for it in elem.iter("event"):
                if it.text[-1] == ".":
                    idx = it.attrib["start"][1:]
                    l_ponct_idx.append(int(idx))
            #break
    #print(l_noun_idx)
    return l_ponct_idx

def token_list(file,idx_start,idx_end):
    tree = ET.parse(file)
    root = tree.getroot()
    #nb = 0
    l_tok = ""
    l_lab = []
    for elem in root.iter('tier'):
        d = elem.attrib
        if "tok" in d.values():
            for it in elem.iter("event"):
                #if it.text[-1] == ".":
                #    idx = it.attrib["start"][1:]
                #    l_ponct_idx.append(int(idx))
                if int(it.attrib["start"][1:]) in range(idx_start,idx_end+1):
                    l_tok = l_tok+" "+it.text
                    
    return l_tok

def cut_data_into_sentences(file,labels,data_max_lenght):
    max_lenght = 0
    l_ponct_idx = get_ponct_idx(file)
    l_ponct_idx = [-1]+l_ponct_idx
    l_sent = []
    l_lab = []
    for i in range(len(l_ponct_idx)-1):
        l_sent.append( token_list(file,l_ponct_idx[i]+1,l_ponct_idx[i+1]))
        non_pad_lab = labels[l_ponct_idx[i]+1:l_ponct_idx[i+1]+1]
        pad_lab = non_pad_lab + [-100]*(data_max_lenght-len(non_pad_lab))
        max_lenght =  max(len(non_pad_lab), max_lenght)
        l_lab.append(pad_lab)
    
    return l_sent,l_lab, max_lenght



def rel_position_top_in_sentence(file,l_tags):
    l_main_idx = []
    #l_tags =  ["NN","NE","PPER","PDS"]
    l_top_idx = get_topics_idx(file)

    for idx in l_top_idx:
        tag = get_pos_of_idx(file,idx)
        if tag in l_tags:
            l_main_idx.append(idx)
    #print("all top idx: ",l_top_idx)
    #print("main idx",l_main_idx)


    l_ponct = get_ponct_idx(file)
    l_rel_pos = []
    for top_idx in l_main_idx:
        for i,elem in enumerate(l_ponct):
            if  elem > top_idx:
                if i==0: start = 0
                else: start=l_ponct[i-1]
                end = elem
                break
        #print(start,end)
        rel_pos = (top_idx-start)/(end-start)
        l_rel_pos.append(rel_pos)
    #print(l_rel_pos)
    if len(l_rel_pos)>0:
        return np.mean(l_rel_pos)
    else:
        return None

            


def create_label_list(file,data_size,l_tags):
    #labels: 0 for nouns/proper nouns/pronouns which are not topics, 
    #1 for the nouns/proper nouns/pronouns which are topics. 
    #-100 otherwise 
    sent,d_sent = get_d_sentence_pcc2(file)
    l_topic_idx = get_topics_idx(file)
    l_noun_idx = get_noun_idx(file,l_tags)
    #print("topic",l_topic_idx)
    #print("nouns",l_noun_idx)
    #l_label = [0]#corresponds to the begining token
    l_label = []
    for i in range(data_size-2): 
        if i in l_topic_idx and i in l_noun_idx:
            l_label.append(1)
            #nb_ones+=1
        elif i in l_noun_idx:
            l_label.append(0)
            #nb_zeros+=1
        else:
            l_label.append(-100)
    #l_label.append(0) #to match the end token
    return l_label

def verify_label_list(file,l_tags):
    sent,d_sent = get_d_sentence_pcc2(file)
    l_label = create_label_list(file,l_tags)
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

def get_pos_of_idx(file,idx):
    tree = ET.parse(file)
    root = tree.getroot()
        
    for elem in root.iter('tier'):
        d = elem.attrib
        if "pos" in d.values():
                for it in elem.iter("event"):
                    if str(idx) == it.attrib["start"][1:]:
                     return it.text
    return None

def get_nb_tag(data_folder):
    l_files = os.listdir(data_folder)
    #l_files = ["maz-4282.exb","maz-10207.exb"]
    l_pos =  ["NN","NE","PPER","PDS"]
    d_count = {"NN":0,"NE":0,"PPER":0,"PDS":0}

    for elem in l_files:

        file = data_folder+"/"+elem
        tree = ET.parse(file)
        root = tree.getroot()    
        
        for elem in root.iter('tier'):
            d = elem.attrib
            if "pos" in d.values():
                    for it in elem.iter("event"):
                        if it.text in l_pos:
                            d_count[it.text]+=1
                    
    return d_count



def get_main_elem_topic_cluster(start,l_pos_topic,l_tags):
    #l = ["NN","NE","PPER","PDS"]
    l_main = []
    for i,elem in enumerate(l_pos_topic):
        if elem in l_tags:
            l_main.append(elem)
    return l_main

def count_pos_all_files(data_folder,l_tags):

    #main pos in topics
    l_dir = os.listdir(data_folder)
    #l_dir = ["maz-4282.exb","maz-10207.exb"]
    #l_tags = ["NN","NE","PPER","PDS"]
    d_count_topic = {"NN":0,"NE":0,"PPER":0,"PDS":0}
    l_unclear = []
    for elem in l_dir:
        file = data_folder+"/"+elem
        d_main,d_unclear = main_elem_topic_file(file)
        for (l_all,l_main) in d_main.values():
            #print(l_main)
            for t in l_main:
                d_count_topic[t]+=1
        l_unclear.append((elem,d_unclear))
        if len(d_unclear) >0:
            print (elem,d_unclear)
    
    return d_count_topic,l_unclear


def main_elem_topic_file(file,l_tags):
    d_pos = get_pos_of_topics(file)
    d_unclear = {}
    d_main = {}
    for start in d_pos:
        l_main = get_main_elem_topic_cluster(start,d_pos[start],l_tags)
        if l_main == []:
            d_unclear[start] = d_pos[start]
        else:
            d_main[start]=(d_pos[start],l_main)
    return d_main, d_unclear





def get_pos_of_topics(file):
    #return lists of lists, each list containing the labels of a topic set
    l_tup = get_topics_idx(file,tup=True)
    d_pos = {}
    for (start,end) in l_tup:
        l_pos = []
        for idx in range(int(start),int(end)):
            pos = get_pos_of_idx(file,idx)
            l_pos.append(pos)
        d_pos[start] = l_pos
    return d_pos


    return None



def compute_weight(nb_zeros, nb_ones):
    tot = nb_zeros + nb_ones
    pos_weight = tot / (nb_ones * 2)
    neg_weight = tot / (nb_zeros * 2)
    
    weight_tensor = torch.tensor([pos_weight,neg_weight])
    return weight_tensor





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


 



#label = create_label_list("pcc2_data/maz-4282.exb",100)
#print(label)




def ratios(pcc2_data_folder,l_tags):
    l_tag = ["NN","NE","PPER","PDS"]
    d_top,l_unclear = count_pos_all_files(pcc2_data_folder,l_tags)
    d_all = get_nb_tag(pcc2_data_folder)
    d_ratio = {}
    for tag in l_tag:
        if d_all[tag] == 0:
            d_ratio[tag]=0
        else:
            d_ratio[tag] = d_top[tag]/d_all[tag]
    d_top["all"]=sum([d_top[tag] for tag in l_tag])
    d_all["all"]=sum([d_all[tag] for tag in l_tag])
    d_ratio["all"]=d_top["all"]/d_all["all"]

    return d_ratio,d_top,d_all,l_unclear



def gpt_prompts(l_tags,file,data_max_lenght_file,data_max_lenght_sent):

    labels = create_label_list(file,data_max_lenght_file,l_tags)
    ll_sent, ll_lab, max_lenght_one = cut_data_into_sentences(file,labels,data_max_lenght_sent)
    count = 0
    prompt = ""
    for i,sent in enumerate(ll_sent):
        sent_split = sent.split(" ")
        top = " "
        labels = ll_lab[i]

        if 1 in labels:
            idx_top = ll_lab[i].index(1)
            #print(idx_top)
            top = sent_split[idx_top+1]        
            prompt = prompt +"In the sentence: \""+sent+"\", \""+top+"\" is the topic. \n"
            count+=1
        if count >4:
            break

    full_prompt =  prompt + "\nCould you generate 10 more examples of sentences indicating their topics?"
    print(full_prompt)
    #exit()

    json_object = json.dumps(full_prompt,ensure_ascii=False)
    with open("prompts.json", "w") as outfile:
        outfile.write(json_object)

    

"""
file = "pcc2_data/maz-4282.exb"

l_tok = token_list(file,2,8)
print(l_tok)




data_max_lenght = 500
l_tags = ["NN"]
sent,d_sent = get_d_sentence_pcc2(file)
labels,nb_zeros, nb_ones = create_label_list(file,data_max_lenght,1,1,l_tags)
l_sent,l_lab = cut_data_into_sentences(file,sent,labels)
print(l_sent)
print(l_lab)
"""

