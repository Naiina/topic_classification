import xml.etree.ElementTree as ET
import torch
import os
import numpy as np
import pickle
import matplotlib.pyplot as plt
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

def get_topics(file,test=False):
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
    
    if test:
        return l_tuple
    else:
        return l_topic_idx



def create_label_list(file,data_size,nb_zeros,nb_ones):
    #labels: 0 for nouns/proper nouns/pronouns which are not topics, 
    #1 for the nouns/proper nouns/pronouns which are topics. 
    #-100 otherwise 
    sent,d_sent = get_d_sentence_pcc2(file)
    l_topic_idx = get_topics(file)
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



def plot_pkl(file):

    with open(file, 'rb') as f:
        d = pickle.load(f)
    #print(d)
    
    plt.plot(d["train_loss"])
    plt.title("train set loss")
    plt.show()
    plt.plot(d["test_loss"])
    plt.title("test set loss")
    plt.show() 



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

def check_all_topic_are_nn(pcc2_data_folder):
    print("To fix")
    l_files = os.listdir(pcc2_data_folder)
    empty_all = 0
    empty_nn = 0
    for elem in l_files:
        print(elem)
        file = pcc2_data_folder + "/" + elem
        l_nn = get_noun_idx(file)
        l_top_tuple = get_topics(file,True)
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

  
plot_pkl("loss_non_weighted.pkl")
    
