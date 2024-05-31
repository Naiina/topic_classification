from conllu import parse
from io import open
from conllu import parse_tree, parse_incr
import numpy
import json





def get_dict_sent_subj(file):
    data = open(file,"r", encoding="utf-8")
    dd = parse(data.read())
    d = {}
    
    for i,elem in enumerate(dd):
        l = list(elem)
        text = elem.metadata['text']
        sent_id = elem.metadata['sent_id']
        l_subj=[]
        for d_elem in l:
            if "nsubj" in d_elem.values():
                l_subj.append(d_elem["form"])
                d[i+1] = (sent_id,text,l_subj)
    return d

def turn_the_last_zero_to_one(l):
    i = len(l)-1
    for elem in reversed(l):
        if elem ==0:
            l[i] = 1
            return l
        i = i-1
    return l
        


def get_dict_jap_topic(file,l_tags,len_labels):
    data = open(file,"r", encoding="utf-8")
    dd_data = parse(data.read())
    d_out = {}
    max_len = 0
    l_m = []
    nb_topics = 0
    for idx,elem in enumerate(dd_data):
        l = list(elem)
        l_words = []
        l_labels = [-100]*len_labels
        text_with_wa = elem.metadata['text']
        sent_id = elem.metadata['sent_id']
        text_without_wa = ""
        i=0
        for d_word in l:
            if i>len_labels-1:
                break
            if "は" in d_word.values(): #not added to the list. Track back the topic
                l_labels = turn_the_last_zero_to_one(l_labels)
                nb_topics = nb_topics +1
            else:
                l_words.append(d_word["form"]) 
                text_without_wa = text_without_wa + d_word["form"]
                b = False
                for tag in l_tags:
                    if tag in d_word.values():
                        b = True
                if b:
                    l_labels[i] = 0
                i = i+1
        d_out[idx] = {"sent_id":sent_id,"sentence_with_wa":text_with_wa,"sentence_without_wa":text_without_wa,"labels":l_labels,"word_list":l_words}
        m = len(l_words)
        l_m.append(m)
        max_len = max(m,max_len)
    #print(max_len)
    #print(l_m)
    #print(numpy.quantile(l_m, [0,0.25,0.5,0.85,1]))
    #print(nb_topics)
        
    return d_out


def get_dict_german(UD_file,gpt_annot_file,l_tags,len_labels):
    data_UD = open(UD_file,"r", encoding="utf-8")
    dd_data_UD = parse(data_UD.read())
    d_out = {}
    l_m = []
    f = open(gpt_annot_file,"r", encoding="utf-8")
    l_annot_gpt_data = json.load(f)
    #print(l_annot_gpt_data)
    d_annot_gpt_data = convert_gpt_out_in_dict(l_annot_gpt_data)
    kkk = 0


    for idx,elem in enumerate(dd_data_UD):
        if idx >2000:
            break

        text = elem.metadata['text']
        #print(text)

        if text in d_annot_gpt_data.keys():
            kkk = kkk+1
            
            #print(text)

            l = list(elem)
            l_labels = [-100]*len_labels
            
            sent_id = elem.metadata['sent_id']
            l_words = []
            i = 0
            to_skip = 0
            
            for d_word in l:

                if i>len_labels-1:
                #if False:
                    break
                
                
                if "-" in str(d_word["id"]):
                    to_skip = 2

                if to_skip<1:
                    l_words.append(d_word["form"]) 
                    b = False
                    for tag in l_tags:
                        if tag in d_word.values():
                            b = True
                    if b:
                        l_labels[i] = 0
                    i = i+1
                to_skip = to_skip-1
            #print(l_words)
            topic = d_annot_gpt_data[text]
            pos = topic_pos(text, topic)
            if pos != None:    
                l_labels[pos] = 1
            #print(topic)
            #print(pos)
            #print(l_labels)  
            
            d_out[idx] = {"sent_id":sent_id,"sentence":l_words,"labels":l_labels}
            #m = len(l)
            #l_m.append(m)
        #print(len(m))
        #print(numpy.quantile(l_m, [0,0.25,0.5,0.85,1]))
    print(kkk)       
    return d_out



#def topic_pos(data):
#    l_data_with_pos = []
#    for i,d in enumerate(data):
#        if i>4:
#            break
#        l_sent_split = d["sentence"].split()
#        #print(l_sent_split)
#        l_sent_split[-1] = l_sent_split[-1][:-1] #remove end ponctuation
#        try:
#            pos = l_sent_split.index(d["topic"])
#        except ValueError:
#            pos = None
#        if pos!=None:
#            d["topic_idx"] = pos
#           d["sent_len"] = len(l_sent_split)
#        #print(d)
#        l_data_with_pos.append(d)
#    return l_data_with_pos


def topic_pos(sentence, topic):

    l_sent_split = sentence.split()
    #print(l_sent_split)
    l_sent_split[-1] = l_sent_split[-1][:-1] #remove end ponctuation
    try:
        pos = l_sent_split.index(topic)
    except ValueError:
        pos = None
    #if pos!=None:
    #    d["topic_idx"] = pos
    #    d["sent_len"] = len(l_sent_split)
    #print(d)
    #l_data_with_pos.append(d)
    return pos


#def gpt_to_list_for_hug_format(data, idx_shift = 0):
#    l_data_with_pos = topic_pos(data)
#    l_sent_train,l_labels_train, l_id_train = [], [], []
#    for i,d in enumerate(l_data_with_pos):
#        l_sent_train.append(d["sentence"])
#        l_id_train.append(i+idx_shift)
#        labels = [0]*d["sent_len"]
#        print()
#        labels[d["topic_idx"]] = 1
#        l_labels_train.append(labels)
#    
#    return l_sent_train,l_labels_train, l_id_train 


def convert_gpt_out_in_dict(l):
    d = {}
    for elem in l:
        sentence = elem["sentence"]
        d[sentence] = elem["topic"]
    return d
        



#file = "ud-treebanks-v2.13/UD_English-GUM/en_gum-ud-train.conllu"
#file = "ud-treebanks-v2.13/UD_French-PUD/fr_pud-ud-test.conllu"
UD_file = "ud-treebanks-v2.13/UD_German-GSD/de_gsd-ud-train.conllu"
#file = "UD_Japanese-GSD/ja_gsd-ud-train.conllu"

#l_tags = ["NOUN","PROPN","PRON"]
l_tags = ["NN","NE","PPER","PDS"]

len_labels = 40
#d = get_dict_jap_topic(file,l_tags,len_labels)




#print(d[0])

gpt_annot_file= "UD_german_data.json"  

#f = open(gptfile, "r", encoding='utf-8')
#l_data = json.load(f)
 
# returns JSON object as 
# a dictionary


#data= convert_gpt_out_in_dict(l_data)

#for i,key in enumerate(data.keys()):
#    pos = topic_pos(key, data[key])
#    if i>5:
#        exit()
#    print(data[key])
#    print(key)
#    print(pos)


d = get_dict_german(UD_file,gpt_annot_file,l_tags,len_labels)

#print(d[0])
#print(gpt_to_list_for_hug_format(data))