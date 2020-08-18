import torch
from models.bert_attention_model import AttentionModel
from models.bert_cnn_model import BERTCNNSentiment

import sys

if sys.argv[1].lower() =="hinglish":
  data_path = "../data/hinglish/"
elif sys.argv[1].lower() == "spanglish":
  data_path = "../data/spanglish/"
else:
  print("Format: %s %s" %(argv[0], argv[1]))

train_name = "train.txt"
test_name = "test.txt"
model_save_names = ["../checkpoint/cnn_model.txt", "../checkpoint/attention_model.txt"]




import random
import numpy as np

SEED = 1234

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True

from transformers import BertTokenizer, AutoTokenizer, XLMRobertaTokenizer

tokenizer = XLMRobertaTokenizer.from_pretrained("xlm-roberta-base")
print('XLM Roberta Tokenizer Loaded...')



init_token_idx = tokenizer.cls_token_id
eos_token_idx = tokenizer.sep_token_id
pad_token_idx = tokenizer.pad_token_id
unk_token_idx = tokenizer.unk_token_id

max_input_length = 150
print("Max input length: %d" %(max_input_length))

def tokenize_and_cut(sentence):
    tokens = tokenizer.tokenize(sentence) 
    tokens = tokens[:max_input_length-2]
    return tokens




from torchtext import data

UID = data.Field(sequential=False, use_vocab=False, pad_token=None)
TEXT = data.Field(batch_first = True,
                  use_vocab = False,
                  tokenize = tokenize_and_cut,
                  preprocessing = tokenizer.convert_tokens_to_ids,
                  init_token = init_token_idx,
                  eos_token = eos_token_idx,
                  pad_token = pad_token_idx,
                  unk_token = unk_token_idx)


LABEL = data.LabelField()

from torchtext import datasets

fields = [('uid',UID),('text', TEXT),('label', LABEL)]
train_data, test_data = data.TabularDataset.splits(
                                        path = data_path,
                                        train = train_name,
                                        test = test_name,
                                        format = 'tsv',
                                        fields = fields,
                                        skip_header = True)
train_data, valid_data = train_data.split(random_state = random.seed(SEED))
print('Data loading complete')
print(f"Number of training examples: {len(train_data)}")
print(f"Number of validation examples: {len(valid_data)}")
print(f"Number of test examples: {len(test_data)}")


tokens = tokenizer.convert_ids_to_tokens(vars(train_data.examples[0])['text'])



LABEL.build_vocab(train_data, valid_data)


print(LABEL.vocab.stoi)




BATCH_SIZE = 128

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print("Device in use:",device)
train_iterator, valid_iterator, test_iterator = data.BucketIterator.splits(
    (train_data, valid_data, test_data),
    sort_key=lambda x: len(x.text), 
    batch_size = BATCH_SIZE, 
    device = device)

print('Iterators created')

print('Downloading XLM Roberta model...')

from transformers import XLMRobertaModel
bert = XLMRobertaModel.from_pretrained('xlm-roberta-base')

import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
print('XLM Roberta model downloaded')


OUTPUT_DIM = 3
DROPOUT = 0.3
N_FILTERS = 100
FILTER_SIZES = [2,3,4]
HIDDEN_DIM = 100

model_names = ["CNN_Model", "Attention_Model"]
models = [  BERTCNNSentiment(bert, OUTPUT_DIM, DROPOUT, N_FILTERS, FILTER_SIZES),
            AttentionModel(bert, BATCH_SIZE, OUTPUT_DIM, HIDDEN_DIM, 50000, 768)  ]



def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

for i in range(2):
    print(f'The {models[i]} has {count_parameters(models[i]):,} trainable parameters')

for i in range(2):
    print("Parameters for " + f'{model_names[i]}')
    for name, param in models[i].named_parameters():                
        if param.requires_grad:
            print(name)

import torch.optim as optim
from sklearn.metrics import confusion_matrix
def clip_gradient(model, clip_value):
    params = list(filter(lambda p: p.grad is not None, model.parameters()))
    for p in params:
        p.grad.data.clamp_(-clip_value, clip_value)

optimizers = [optim.Adam(models[0].parameters()), optim.Adam(models[1].parameters())]


criterion = nn.CrossEntropyLoss()
nll_loss = nn.NLLLoss()
log_softmax = nn.LogSoftmax()



for i in range(2):
    models[i] = models[i].to(device)
criterion = criterion.to(device)
nll_loss = nll_loss.to(device)
log_softmax = log_softmax.to(device)



from sklearn.metrics import f1_score

def categorical_accuracy(preds, y):
    count0,count1,count2 = torch.zeros(1),torch.zeros(1),torch.zeros(1)
    total0,total1,total2 = torch.FloatTensor(1),torch.FloatTensor(1),torch.FloatTensor(1)
    max_preds = preds.argmax(dim = 1, keepdim = True) # get the index of the max probability
    correct = max_preds.squeeze(1).eq(y)
    predictions = max_preds.squeeze(1)
    true_correct = [0,0,0]
    for j,i in enumerate(y.cpu().numpy()):
      true_correct[y.cpu().numpy()[j]]+=1
      if i==0:
        count0+=correct[j]
        total0+=1
      elif i==1:
        count1+=correct[j]
        total1+=1
      elif i==2:
        count2+=correct[j]
      else:
        total2+=1
    metric=torch.FloatTensor([count0/true_correct[0],count1/true_correct[1],count2/true_correct[2],f1_score(y.cpu().numpy(),predictions.cpu().numpy(),average='macro')])
    return correct.sum() / torch.FloatTensor([y.shape[0]]),metric,confusion_matrix(y.cpu().numpy(),max_preds.cpu().numpy())



def train(model, iterator, optimizer, criterion, i):
    
    epoch_loss = 0
    epoch_acc = 0
    
    model.train()
    
    for batch in iterator:
        optimizer.zero_grad()
        
        if (i == 0):
          predictions =  model(batch.text).squeeze(1)
        else:
          predictions =  model(batch.text, batch_size = len(batch)).squeeze(1)
            
        loss = criterion(predictions, batch.label)

        acc,_,_ = categorical_accuracy(predictions, batch.label)
        
        loss.backward()
        clip_gradient(model, 1e-1)
        optimizer.step()
        
        epoch_loss += loss.item()
        epoch_acc += acc.item()
        
    return epoch_loss / len(iterator), epoch_acc / len(iterator)


def evaluate(model, iterator, criterion, i):
    
    epoch_loss = 0
    epoch_acc = 0
    epoch_all_acc = torch.FloatTensor([0,0,0,0])
    confusion_mat = torch.zeros((3,3))
    confusion_mat_temp = torch.zeros((3,3))

    model.eval()
    
    with torch.no_grad():
    
        for batch in iterator:
            if (i == 0):
              predictions = model(batch.text).squeeze(1)
            else:
              predictions = model(batch.text,batch_size=len(batch)).squeeze(1)
            
            loss = criterion(predictions, batch.label)
            
            acc,all_acc,confusion_mat_temp = categorical_accuracy(predictions, batch.label)
            epoch_loss += loss.item()
            epoch_acc += acc.item()
            epoch_all_acc += all_acc
            confusion_mat+=confusion_mat_temp
    return epoch_loss / len(iterator), epoch_acc / len(iterator),epoch_all_acc/len(iterator),confusion_mat


import time

def epoch_time(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_mins = int(elapsed_time / 60)
    elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
    return elapsed_mins, elapsed_secs


N_EPOCHS = 40

best_f1 = [-1, -1]
for epoch in range(N_EPOCHS):
    for i in range(2):
        start_time = time.time()
        
        train_loss, train_acc = train(models[i], train_iterator, optimizers[i], criterion, i)
        valid_loss, valid_acc,tot,conf = evaluate(models[i], valid_iterator, criterion, i)
        f1 = tot[3]
        end_time = time.time()

        epoch_mins, epoch_secs = epoch_time(start_time, end_time)
        
        if f1 > best_f1[i]:
            best_f1[i] = f1
            
            path = model_save_names[i]
            print(path)
            torch.save(models[i].state_dict(), path)
        
        
        print(f'Epoch: {epoch+1:02} | Epoch Time: {epoch_mins}m {epoch_secs}s')
        print(f'\tTrain Loss: {train_loss:.3f} | Train Acc: {train_acc*100:.2f}%')
        print(f'\t Val. Loss: {valid_loss:.3f} |  Val. Acc: {valid_acc*100:.2f}%')
        print(tot)
        print(conf)

for i in range(2):
    path = model_save_names[i]
    models[i].load_state_dict(torch.load(path))


def ensemble_evaluate(models, iterator, criterion):
    
    epoch_loss = 0
    epoch_acc = 0
    epoch_all_acc = torch.FloatTensor([0,0,0,0])
    models[0].eval()
    models[1].eval()
    confusion_mat = torch.zeros((3,3))
    confusion_mat_temp = torch.zeros((3,3))
    
    with torch.no_grad():
    
        for batch in iterator:
          
          predictions0 = models[0](batch.text).squeeze(1)
          predictions1 = models[1](batch.text, batch_size=len(batch)).squeeze(1)
          
          predictions = F.softmax(predictions0, dim=1) * F.softmax(predictions1, dim=1)
          loss = criterion(predictions, batch.label)
          
          acc,all_acc,confusion_mat_temp = categorical_accuracy(predictions, batch.label)
          epoch_loss += loss.item()
          epoch_acc += acc.item()
          epoch_all_acc += all_acc
          confusion_mat += confusion_mat_temp
    print(confusion_mat)
    return epoch_loss / len(iterator), epoch_acc / len(iterator),epoch_all_acc/len(iterator)


def ensemble_write_to_file(models, test_iterator):
    label_dict = {'0':'negative', '1':'neutral', '2':'positive'}
    file = open("answer.txt", "w")
    file.write('Uid,Sentiment\n')
    count = 0
    for batch in test_iterator:
      predictions0 = models[0](batch.text).squeeze(1)
      predictions1 = models[1](batch.text, batch_size=len(batch)).squeeze(1)
      predictions = F.softmax(predictions0, dim=1) * F.softmax(predictions1, dim=1)
      max_preds = predictions.argmax(dim = 1, keepdim = True).detach().cpu().numpy()
      for i,row in enumerate(batch.uid.cpu().numpy()):
        count += 1
        label_number = max_preds[i][0]
        label_number_str = list(LABEL.vocab.stoi.keys())[list(LABEL.vocab.stoi.values()).index(label_number)]
        predicted_label_name = label_dict[label_number_str]
        if count != len(test_data):
          file.write('%s,%s\n'%(row,predicted_label_name))
        else:
          file.write('%s,%s'%(row,predicted_label_name))
    file.close()

valid_loss, valid_acc, tot = ensemble_evaluate(models, test_iterator, criterion)
print(f'\t Val. Loss: {valid_loss:.3f} |  Val. Acc: {valid_acc*100:.2f}%')
print(tot)