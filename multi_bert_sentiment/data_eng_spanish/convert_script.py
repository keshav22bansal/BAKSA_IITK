import sys

f = open(sys.argv[1],"r")
f1 = open(sys.argv[2],"w")
str1=""
line = f.readline()
l1=[]
# l2 =[]
# l3=[]
flag=0
flag2=0
count=1
#f1.write("text\tlabel\tuid\n")
newdatapoint = True
while(line):
    if(line.strip()==""):
        newdatapoint = True
        if(len(l1)):
            str1 = str1+str(flag2)+"\t"+" ".join(l1)+"\t"+str(flag)+"\t"+str(flag)+"\n"
            # str2 = str2+" ".join(l2)+"\n"
            # str3 = str3+" ".join(l3)+"\n"
            l1=[]
            # l2=[]
            # l3=[]
            count += 1

    else:
        array = line.strip().split("\t")
        #print(array,len(array))
        '''
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
        '''
        if (newdatapoint):
            newdatapoint = False
            if(len(array)==3):
                flag2 = count
                if(array[2]=="negative"):
                    flag=0
                elif(array[2]=="positive"):
                    flag=2
                elif(array[2]=="neutral"):
                    flag=1
                else:
                    print("error")
                    exit(0)
            elif (len(array)==2):
                flag2 = count
                flag = 0
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
    # break
f1.write(str1)
# f2.write(str2)
# f3.write(str3)
