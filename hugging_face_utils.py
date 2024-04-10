from datasets import load_dataset, load_metric
import transformers
from transformers import AutoTokenizer
from transformers import AutoModelForTokenClassification, TrainingArguments, Trainer
from transformers import DataCollatorForTokenClassification
import numpy as np



#to add: neptune

task = "ner" # Should be one of "ner", "pos" or "chunk"
model_checkpoint = "distilbert-base-uncased"
batch_size = 16
label_all_tokens = False  #for a word tokenized into several tokens: should all the labels except the first one of this word be set as -100 during alignment?

datasets = load_dataset("conll2003")  
metric = load_metric("seqeval")
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
assert isinstance(tokenizer, transformers.PreTrainedTokenizerFast)
model = AutoModelForTokenClassification.from_pretrained(model_checkpoint, num_labels=2)

#example = datasets["train"][4]  #dict of id (str), tokens(list of str), (pos_)tag(list of int)
#print(type(example["id"]))



def tokenize_and_align_labels(examples):
    """
    get: one or several exemples of the form: dict of id (str), tokens(list of str), (pos_)tag(list of int)
    returns a dict with as keys:
            'input_ids': list (of list if several exemples) of tokens
            "attention masks"
            "labels": list (of list if several exemples) of aligned labels

    """
    tokenized_inputs = tokenizer(examples["tokens"], truncation=True, is_split_into_words=True)

    labels = []
    for i, label in enumerate(examples[f"{task}_tags"]):
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

    tokenized_inputs["labels"] = labels
    return tokenized_inputs

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

    results = metric.compute(predictions=true_predictions, references=true_labels)
    return {
        "precision": results["overall_precision"],
        "recall": results["overall_recall"],
        "f1": results["overall_f1"],
        "accuracy": results["overall_accuracy"],
    }

#print(tokenize_and_align_labels(datasets['train'][:5]))

model_name = model_checkpoint.split("/")[-1]
args = TrainingArguments(
    "tok_classif", #checkpoint folder name
    evaluation_strategy = "epoch",
    learning_rate=2e-6,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    num_train_epochs=10,
    weight_decay=0.01,
    #push_to_hub=True,
)

data_collator = DataCollatorForTokenClassification(tokenizer)

tokenized_datasets = datasets.map(tokenize_and_align_labels, batched=True)

trainer = Trainer(
    model,
    args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics
)

trainer.train()
trainer.evaluate()

#tokenized_datasets = datasets.map(tokenize_and_align_labels, batched=True) #applies on val test and train set