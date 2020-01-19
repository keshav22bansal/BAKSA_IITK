import emoji

newfile = open("../data/sem_eval_data_smileys_replaced", "w")
with open("../data/sem_eval_data.txt") as f:
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
        ans1 = " ".join(l1)
        ans = ans1[:-4] +" "+ " ".join(l2)+" "+ ans1[-4:]+'\n'
        ans = list(ans)
        ans[-3] = '\t'
        ans[-5] = '\t'
        # print(ans)
        ans = "".join(ans)
        # print(ans)
        newfile.write(ans)
        # break