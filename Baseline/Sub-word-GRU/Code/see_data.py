import h5py
import numpy as np
filename = "/home/keshav/6thsem/cs698/Sub-word-LSTM/Data/Xtest_new_experiment.h5"
with h5py.File(filename, 'r') as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]

    # Get the data
    data = list(f[a_group_key])
print(data)