# from polyglot.transliteration import Transliterator
import requests
l1 =[]
l2 =[]
f1 = open("train_conll.txt","r")
f = open("transliterated_data_google.txt","a+")
flag=0
flag2=0
line =f1.readline()
count=0

str1=[]
hindi =[]

coun=0
while line:
    if(line=="\n"):
        count+=1
        if(count==1774):
            line = f1.readline()
            break
    line = f1.readline()

while(line):
    if(line=="\n"):
        if(len(l1)):
            count+=1
            # str1.append(" ")
            str1.append(str(flag2))
            str1.append("\t")
            str1=str1 + l1
            str1 = str1[:-1]
            str1.append("\t")
            str1.append(str(flag))
            str1.append("\t")
            str1.append(str(flag))
            str1.append("\n")
            if(count%1==0):
                # print(len(hindi))
                hindi1=[]
                for ele in hindi:
                    if len(ele)>8:
                        hindi1.append(ele[:8])
                    else:
                        hindi1.append(ele)
                hindi = hindi1
                # print(hindi)
                hindi = " ".join(hindi)
                URL = "https://www.google.com/inputtools/request?text="+str(hindi)+"&ime=transliteration_en_hi&num=5&cp=0&cs=0&ie=utf-8&oe=utf-8&app=jsapi&uv"
                PARAMS = {} 
                r = requests.get(url = URL, params = PARAMS) 
                data = r.json() 
                hindi_list = data[1][0][1][0]
                hindi_list = hindi_list.split(" ")
                # print(len(hindi_list))
                j=0
                for i in range(len(str1)):
                    if(str1[i]=="qwertyuiopasdfghjklzxcvbnm"):
                        str1[i] = hindi_list[j]
                        j+=1
                str1 = "".join(str1)

                f.write(str1)
                str1=[]
                hindi =[]
                if count%100==0:
                    print(count)
                # exit(0)

            # str1 = str1+str(flag2)+"\t"+" ".join(l1)+"\t"+str(flag)+"\t"+str(flag)+"\n"
            l1=[]
            # print(str1)
            # count=count+1
            # if(count%10==0):
                # print(count)
                # f.write(str1)
                # exit(0)
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
                hindi.append(array[0])
                # URL = "https://www.google.com/inputtools/request?text="+str(array[0])+"&ime=transliteration_en_hi&num=5&cp=0&cs=0&ie=utf-8&oe=utf-8&app=jsapi&uv"
                # PARAMS = {} 
                # r = requests.get(url = URL, params = PARAMS) 
                # data = r.json() 
                # l1.append(transliterate(array[0], sanscript.ITRANS, sanscript.DEVANAGARI))
                # l1.append(data[1][0][1][0])
                l1.append("qwertyuiopasdfghjklzxcvbnm")
                l1.append(" ")
            else:
                l1.append(array[0])
                l1.append(" ")
    line = f1.readline()

f.write(str1)
    
    
        

    
