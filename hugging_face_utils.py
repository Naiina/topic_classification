from datasets import load_dataset, load_metric, Dataset
import transformers
from transformers import AutoTokenizer
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForTokenClassification
from transformers import AutoTokenizer, BertForTokenClassification
import numpy as np
import neptune
from read_xml import get_data
from transformers.integrations import NeptuneCallback
from datasets.dataset_dict import DatasetDict
from datasets import Dataset
from sklearn.metrics import f1_score
from sklearn.metrics import precision_recall_fscore_support
import argparse



#to check: not batched. when is the padding done?

model_checkpoint = "google-bert/bert-base-multilingual-cased"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = BertForTokenClassification.from_pretrained(model_checkpoint, num_labels=2)
print("model and tok loaded")

label_all_tokens = True  #for a word tokenized into several tokens: should all the labels except the first one of this word be set as -100 during alignment?

debug = False


parser = argparse.ArgumentParser()
parser.add_argument('--lr', type=float)
args = parser.parse_args()
lr = args.lr

if debug:
    nept = False
    pcc2_data_folder = "pcc2_data_debug"
    data_max_lenght_file = 600
    data_max_lenght_sent = 80
    nb_epochs = 2
    batch_size = 2
    #lr = 10e-3
    weight_decay = 0.01
    print("batch size: ", batch_size)
    print("learning rate: ", lr)
    
else: 
    pcc2_data_folder = "pcc2_data"
    data_max_lenght_file = 600
    data_max_lenght_sent = 80 #max nb of tokens in a sentence
    nb_epochs = 80
    batch_size = 64
    #lr = 5e-6
    weight_decay = 0.01
    print("batch size: ", batch_size)
    print("learning rate: ", lr)



def tokenize_and_align_labels(data,hug = False):
    """
    get: one or several exemples of the form: dict of id (str), tokens(list of str), (pos_)tag(list of int)
    returns a dict with as keys:
            'input_ids': list (of list if several exemples) of tokens
            "attention masks"
            "labels": list (of list if several exemples) of aligned labels

    """
    tokenized_inputs = tokenizer(data["tokens"], is_split_into_words=False)

    labels = []
    if hug:
        tag = "ner_tags"
    else:
        tag = "labels"
    for i, label in enumerate(data[tag]):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        previous_word_idx = None
        label_ids = []
        
        for word_idx in word_ids:
            # Special tokens have a word id that is None. We set the label to -100 so they are automatically
            # ignored in the loss function.
            if word_idx is None:
                label_ids.append(-100)
            # We set the label for the first token of each word.
            elif word_idx != previous_word_idx:
                label_ids.append(label[word_idx])
            # For the other tokens in a word, we set the label to either the current label or -100, depending on
            # the label_all_tokens flag.
            else:
                label_ids.append(label[word_idx] if label_all_tokens else -100)
            previous_word_idx = word_idx

        labels.append(label_ids)
        #print(data["tokens"][0])
        #print("label",label)
        #print("word_ids",word_ids)
        #print("aligned labels",label_ids )
        #exit()

    tokenized_inputs["labels"] = labels
    return tokenized_inputs

def hug_data_format(pcc2_data_folder,data_max_lenght_sent,data_max_lenght_file,l_tags):
    l_sent_train,l_labels_train, l_id_train, l_sent_test,l_labels_test, l_id_test = get_data(pcc2_data_folder,data_max_lenght_sent,data_max_lenght_file,l_tags)
    d_train =  Dataset.from_dict({"id": l_id_train, "tokens": l_sent_train, "labels": l_labels_train})
    d_test =  Dataset.from_dict({"id": l_id_test, "tokens": l_sent_test, "labels": l_labels_test})
    #d_val = {"id": [], "tokens": [], "labels": []}
    #datasets = Dataset.from_dict({"train": d_train, "test": d_test})

    datasets = DatasetDict({"train": d_train, "test": d_test})
    return datasets


def compute_metrics(p):
    predictions, labels = p
    predictions = np.argmax(predictions, axis=2)

    # Remove ignored index (special tokens)
    true_predictions = [
        [p for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    true_labels = [
        [l for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    
    #exit()
    flat_pred = sum(true_predictions,[])
    flat_labels = sum(true_labels, [])
    print(flat_pred)
    print("true_lab", flat_labels)

    score = precision_recall_fscore_support(flat_labels,flat_pred, average='binary')
    #f1= f1_score( flat_labels, flat_pred, average = 'micro')
        #compute_metrics_hg(torch.tensor(flat_labels),torch.tensor(flat_pred))

    results = metric.compute(predictions=true_predictions, references=true_labels)
    d = {
        "accuracy": results["overall_accuracy"],
        "precision": score[0],
        "recall": score[1],
        "f1": score[2],
    }

    return d


datasets_hug = load_dataset("conll2003")  
print(type(datasets_hug))
l_tags = ["NN","NE","PPER","PDS"]
datasets= hug_data_format(pcc2_data_folder,data_max_lenght_sent,data_max_lenght_file,l_tags)
print(type(datasets))
#exit()
print("pcc2 dataset loaded")
metric = load_metric("seqeval")
assert isinstance(tokenizer, transformers.PreTrainedTokenizerFast)
#print(tokenize_and_align_labels(datasets['train'][:5]))

tokenized_datasets = datasets.map(tokenize_and_align_labels, batched=True)
#exit()


neptune_callback = NeptuneCallback(
    #project="naiina/topic-classifier-more-epochs",
    #api_token="eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vYXBwLm5lcHR1bmUuYWkiLCJhcGlfdXJsIjoiaHR0cHM6Ly9hcHAubmVwdHVuZS5haSIsImFwaV9rZXkiOiI5YzllNjM4MS0zYjBhLTQwNGUtOGM3Mi1hYjE3ZTVjOWVjMTgifQ==",
    tags=["hug_face_implementation"],
    name="hug face implementation ",
    description="adapted the hugging face token classif to topic classification",
)





#params = {"batch_szie": batch_size, "lr": lr}

args = TrainingArguments(
    "tok_classif", #checkpoint folder name
    evaluation_strategy = "epoch",
    learning_rate=lr,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    num_train_epochs=nb_epochs,
    weight_decay=weight_decay,
    #report_to = None
    #push_to_hub=True,
)


data_collator = DataCollatorForTokenClassification(tokenizer)




trainer = Trainer(
    model,
    args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
    data_collator=data_collator,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
    #callbacks=[neptune_callback]
    callbacks = None
)
#run_nept = NeptuneCallback.get_run(trainer)
#run_nept = neptune.init_run(
#        project="naiina/topic-classifier-more-epochs",
#        api_token="eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vYXBwLm5lcHR1bmUuYWkiLCJhcGlfdXJsIjoiaHR0cHM6Ly9hcHAubmVwdHVuZS5haSIsImFwaV9rZXkiOiI5YzllNjM4MS0zYjBhLTQwNGUtOGM3Mi1hYjE3ZTVjOWVjMTgifQ==",
#        tags=["hug_face_implementation"]
#        ) 
#params = {"batch_size": batch_size, "learning_rate": lr, "weight_decay": weight_decay}

#run_nept["parameters"] = params

trainer.train()
trainer.evaluate()


#if nept:
#    run_nept.stop()
#tokenized_datasets = datasets.map(tokenize_and_align_labels, batched=True) #applies on val test and train set