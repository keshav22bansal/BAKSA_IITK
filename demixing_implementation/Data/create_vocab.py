
# importing the required module 
import matplotlib.pyplot as plt 
f1 = open("train_new_demojise.txt","r")
line = f1.readline()
vocab = {}
x = []
y=[]
for i in range(600):
    x.append(i)
    y.append(0)
# y = 
max_len=0
while(line):
    line_array = line.split("\t")
    sentence = line_array[1]
    # max_len = max(max_len,len(sentence))
    y[len(sentence)]+=1
    list_s = list(sentence.lower())
    for ele in list_s:
        if ele in vocab:
            vocab[ele] +=1
        else:
            vocab[ele] = 1
    line = f1.readline()

list_l = sorted(vocab.items(), key=lambda item: item[1], reverse = True)
dict2 ={}
count=0
for i in range(10):
    dict2[str(i)] = count
    count+=1
for i in range(26):
    dict2[chr(ord('a') + i)] = count
    count+=1
for ele in list_l:
    if(ele[0] in dict2):
        d=1
    else:
        dict2[ele[0]] = count
        count+=1
        if(count==50):
            break
print(len(list_l))
print(list_l[:100])
print(dict2)
print(max_len)
plt.plot(x,y)
plt.show()