import sys
f = open(sys.argv[1])
f2write = open(sys.argv[2],'w')

for line in f:
    arr = line.split('\t')
    print(arr)
    if arr[2].startswith('1'):
        continue
    else :
        f2write.write(line)