# removes imbalance using one of these techniques
# undersampling, oversampling, smote analysis
import sys

#f_out = open(sys.argv[2], "w")
cnt = [0, 0, 0]
with open(sys.argv[1], "r") as f:
    line = f.readline().rstrip()
    # dps contains all the datapoints for negative, neutral, positive datapoints
    dps = [[], [], []]
    while(line):
        line = line.split('\t')
        try:
            cnt[int(line[2])] += 1
            dps[int(line[2])].append(line[1])
        except ValueError:
            pass
        line = f.readline().rstrip()

    # now oversample the scarce label classes
    sampling_ratio = [max(cnt) / cnt[0], max(cnt) / cnt[1], max(cnt) / cnt[2]]
    f_out = open(sys.argv[2], "w")
    f_out.write("uid\ttext\tlabel\n")
    idx = 1
    for i in range(3):
        if (sys.argv[3] == "--undersample"):
            dps[i] = dps[i][:min(cnt)]
        elif (sys.argv[3] == "--oversample"):
            dps[i] = dps[i]*int(sampling_ratio[i]) \
                    + dps[i][:int((sampling_ratio[i] - int(sampling_ratio[i]))*cnt[i])]
        elif (sys.argv[3] == "--posneg"):
            if (i == 1):
                continue
        #print(len(dps[i]))
        for dp in dps[i]:
            f_out.write(str(idx)+'\t'+dp+'\t'+str(i)+'\n')
            idx += 1
    f_out.close()
    #print(sampling_ratio)
print(cnt)