# from polyglot.transliteration import Transliterator
from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate

def  

l1 =[]
l2 =[]
f1 = open("train_conll.txt","r")
f = open("transliterated_data.txt","w+")
flag=0
flag2=0
line =f1.readline()
count=1
str1=""
while(line):
    if(line=="\n"):
        if(len(l1)):
            str1 = str1+str(flag2)+"\t"+" ".join(l1)+"\t"+str(flag)+"\t"+str(flag)+"\n"
            l1=[]
            # print(str1)
            count=count+1
            # if(count%1000==0)
            # exit(0)
    else:
        array = line.split("\t")
        # print(array)
        
        if(len(array)==3):
            flag2 = array[1]
            if(array[2][:-1]=="negative"):
                flag=0
            elif(array[2][:-1]=="positive"):
                flag=2
            elif(array[2][:-1]=="neutral"):
                flag=1
            else:
                print("error")
                exit(0)
        else:
            if(array[1][:-1]=="Hin"):
                # l1.append(transliterate(array[0], sanscript.ITRANS, sanscript.DEVANAGARI))
                l1.append()
            else:
                l1.append(array[0])
    line = f1.readline()

f.write(str1)
    
    
        

    
