#Thompson Sampling
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#implementing Thompson Sampling
import random
N=10000 # количество показов
d=10 # количество реклам
abs_selected=[]
number_of_rewards_1=[0]*d
number_of_rewards_0=[0]*d
total_reward=0
for n in range(0,N):
    ad=0
    max_random=0
    for i in range(d):
        random_beta=random.betavariate(number_of_rewards_1[i]+1,number_of_rewards_0[i]+1)
        if(random_beta>max_random):
            max_random=random_beta
            ad=i
    abs_selected.append(ad)
    if(dataset.values[n,ad]==1):
        number_of_rewards_1[ad]+=1
        total_reward+=1
    else:
        number_of_rewards_0[ad] += 1


plt.hist(abs_selected)
plt.title('Histogram of ad selected')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()