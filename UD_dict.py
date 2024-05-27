from conllu import parse
from io import open
from conllu import parse_tree, parse_incr


#file = "ud-treebanks-v2.13/UD_English-GUM/en_gum-ud-train.conllu"
file = "ud-treebanks-v2.13/UD_French-PUD/fr_pud-ud-test.conllu"



#sentences = parse_tree(data)
#print(sentences[0])
#exit
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

d = get_dict_sent_subj(file)
print(d)