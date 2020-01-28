f = open("IIITH_Codemixed.txt","r")
f1 = open("train_new_demojise.txt","r")
f2 = open("validation_new_demojise.txt","r")
f3 = open("train_new_demojise_large.txt","w+")
line = f1.readline()
line = f1.readline()
max_id = 0
while line:
    array = line.split("\t")
    max_id = max(int(array[0]),max_id)
    line = f1.readline()
print(max_id)
line = f2.readline()
line = f2.readline()
while (line):
    # print(list(line))
    array = line.split("\t")
    array = array[0].split(" ")
    # print(array)
    max_id = max(int(array[0]),max_id)
    line = f2.readline()

print(max_id)
f1 = open("train_new_demojise.txt","r")
str1=f1.read()
# print(str1)
line = f.readline()
max_id = max_id+1
while line:
    array = line.split("\t")
    # print(array)
    l1=[]
    l1.append(str(max_id))
    max_id=max_id+1
    l1.append(array[1])
    l1.append(array[2])
    ans = "\t".join(l1)
    str1 = str1 + ans + "\n"
    line = f.readline()
    # print(ans)
    # break
f3.write(str1)
