import sys

f1 = open(sys.argv[1])
f2 = open(sys.argv[2])
f3 = open('output.txt','w')
uid_sent_map={}
m = {'0':'negative','1':'neutral','2':'positive'}
for line in f2:
    try:
        l = line.strip().split(',')
        print(l)
        # uid_sent_map[l[0]] = [l[1],l[2],l[3]]
        uid_sent_map[l[0]] = [l[1]]
    except:
        pass
count = 0
for line in f1:
    if count == 0:
        count+=1
        continue
    count+=1
    l = line.strip().split('\t')
    l[2] = m[l[2]]
    # print(l)
    print(l)
    l.extend(uid_sent_map[l[0]])
    f3.write("\t".join(l)+"\n")
