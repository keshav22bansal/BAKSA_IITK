import numpy as np
import random
f1 = open("sem_eval_data_smileys_replaced_users_removed","r")
l1 = np.arange(1,15132)
f2 = open("test.txt","w+")
f3 = open("train.txt","w+")
line = f1.read()
l = line.split("\n")
l = l[:-1]
random.shuffle(l)
# print(l)
lines1 = "\n".join(l[:1000])
l1 = l[1000:]
l1_new=[]
for ele in l1:
    l11 = ele.split("\t")
    if(len(l11[0].split(" "))>5):
        l1_new.append(ele)
    # if(len((l1.split("\t"))[0]))
lines2 = "\n".join(l1_new)
f2.write(lines1)
f3.write(lines2)
