#Upper Confidence Bound (UCB)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#implementing UCB
import math
N=10000 # количество показов
d=10 # количество реклам
ads_selecteds=[]
numbers_of_selections=[0]*d
sums_of_rewards=[0]*d
total_reward=0
accumulated_reward=[0]*d
print(numbers_of_selections)

for n in range(0,N):
    ad=0
    max_upper_bound=0
    # выбираем рекламу
    for i in range(d):
        if numbers_of_selections[i]>0:
            average_reward=sums_of_rewards[i]/numbers_of_selections[i]
            delta_i=math.sqrt(3*math.log10(n+1)/2/numbers_of_selections[i])
            upper_bound=average_reward+delta_i
        else:
            upper_bound=1e400
        if(upper_bound>max_upper_bound):
            max_upper_bound=upper_bound
            ad=i
    ads_selecteds.append(ad)
    numbers_of_selections[ad]=numbers_of_selections[ad]+1
    reward=dataset.values[n,ad]
    sums_of_rewards[ad]=sums_of_rewards[ad]+reward
    total_reward=total_reward+reward

plt.hist(ads_selecteds)
plt.title('Histogram of ad selected')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()