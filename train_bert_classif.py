from transformers import AutoTokenizer, BertForTokenClassification
import torch.optim as optim
import torch.nn as nn
import torch
from peft import LoraConfig, TaskType
from peft import get_peft_model
import random



lora_config = LoraConfig(
    task_type=TaskType.SEQ_CLS, r=1, lora_alpha=1, lora_dropout=0.1 )
model = BertForTokenClassification.from_pretrained("google-bert/bert-base-multilingual-cased")
model = get_peft_model(model, lora_config)

tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-multilingual-cased")
optimizer = optim.Adam(model.parameters())
criterion = nn.CrossEntropyLoss()

inputs = tokenizer(["the cat ate the mouse.","I am green."], padding = True, return_tensors="pt")
nb_tok = inputs['input_ids'].size(1)



labels = torch.tensor([[random.randint(0,1) for k in range(nb_tok)],[random.randint(0,1) for k in range(nb_tok)]])

#print(inputs,labels)
with torch.no_grad():
    out_logits = model(**inputs).logits # tensor of size nb_tok * nb_of_classes

predicted_token_class_ids = out_logits.argmax(-1) #get the rank of the greatest elem in logit tensor 
predicted_tokens_classes = [model.config.id2label[t.item()] for t in predicted_token_class_ids[0]] #.item() gets elem of the tensor

out_logits = torch.permute(out_logits, (0, 2, 1))
loss = criterion(out_logits, labels) 
optimizer.zero_grad()
loss.requires_grad = True
loss.backward()
optimizer.step()

print(round(loss.item(), 2))
print(out_logits)
