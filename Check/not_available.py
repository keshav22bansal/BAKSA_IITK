f2 = open("answer.txt","r")
f1 = open("dev_3k_split_conll.txt")
f3 = open("answer_validation_extract.txt","w+")
str1="Uid,Sentiment"
di = {}
line = f2.readline()
line = f2.readline()
l =[]
while line:
    array = line.split(",")
    l.append(int(array[0]))
    di[int(array[0])] = array[1][:-1]
    line = f2.readline()

l.sort()

l1 =[]
line = f1.readline()
while line:
    array = line.split("\t")
    if (len(array)==3):
        l1.append(int(array[1]))
        str1 = str1 + "\n" + str(array[1]) + "," + str(array[2][:-1])
    line = f1.readline()
# l1.sort()
print(len(l1))
# for ele in l1:
#     str1= str1+ "\n"+ str(ele)+","+str(di[ele]) 
    # l1.remove(ele)
print(len(l))
print(l1)
f3.write(str1)