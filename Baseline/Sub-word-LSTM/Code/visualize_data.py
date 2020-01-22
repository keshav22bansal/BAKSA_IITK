

import pandas as pd


data = pd.read_csv('../Data/sem_eval_data_smileys_replaced_users_removed',delimiter='\t',names=["1","2","3","4"])

import matplotlib.pyplot as plt
plt.hist(data["4"])


for i in range(200):
    print(data["2"][i],data["3"][i])

\
from keras import models

model = models.load_weight('../Models/LSTM_new_experiment_weights.h5')

print(model.summary())