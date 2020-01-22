f = open("train_conll.txt","r")
f1 = open("train.txt","w+")
str1=""
line = f.readline()
l1=[]
# l2 =[]
# l3=[]
flag=0
flag2=0
count=1
while(line):
    if(line=="\n"):
        if(len(l1)):
            str1 = str1+str(count)+"\t"+" ".join(l1)+"\t"+str(flag)+"\t"+str(flag)+"\n"
            # str2 = str2+" ".join(l2)+"\n"
            # str3 = str3+" ".join(l3)+"\n"
            l1=[]
            # l2=[]
            # l3=[]
    else:
        array = line.split("\t")
        print(array,len(array))
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
            l1.append(array[0])
        # l2.append(array[1])
        # l3.append(array[2][:-1])
        # print(array)
        # print(array[2][:-1])
    line = f.readline()
    count += 1
    # break
f1.write(str1)
# f2.write(str2)
# f3.write(str3)
