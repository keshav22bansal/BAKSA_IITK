import emoji
import sys
import re

newfile = open(sys.argv[2], "w")
with open(sys.argv[1]) as f:
    for line in f.readlines():
        modified_line = emoji.demojize(line, delimiters=('<', '> ')).strip()
        l = modified_line.split()
        l1=[]
        l2=[]
        for token in l:
            if token[0] == '<' and token[-1] == '>':
                l2.append(token)
            else:
                l1.append(token)
        ans1 = l1[0]+"\t"
        ans1 = ans1+" ".join(l1[1:])
        ans = ans1[:-4] +" "+ " ".join(l2)+" "+ ans1[-4:]+'\n'
        ans = list(ans)
        ans[-3] = '\t'
        ans[-5] = '\t'
        # print(ans)
        ans = "".join(ans)
        # print(ans)

        #Modified by Keshav
        # print(ans)
        ans = ans.replace('@ ','@').replace('# ','#').replace('<','').replace('>','').replace("_",' ').replace('  ',' ')
        string = ans.split('\t')[1]

        new_ans=[]
        tokens = string.split(" ")
        # print(tokens)
        for t in tokens:
            if(t!=""):
                # print("Here ",t)
                # t1 = list(t)
                if(t[0]=="@" or t[0]=="#"):
                    flag=1
                else:
                    new_ans.append(t)
        
        # processed = text_processor.pre_process_doc(string)
        # print(processed)
        # new_ans = []
        # for token in processed:
        #     if token.startswith(("<hash","<number","<")) or "user" in token:
        #         continue
        #     new_ans.append(token)
        
        arr = ans.split('\t')
        arr[1] = re.sub(r"http.*|…",""," ".join(new_ans))
        ans = "\t".join(arr)
        
        # print(arr[2])
        # print(ans)
        # break
        array_a = ans.split("\t")
        li=[]
        li.append(array_a[1])
        li.append(array_a[-1])
        ans = "\t".join(li)
        newfile.write(ans)
        # break