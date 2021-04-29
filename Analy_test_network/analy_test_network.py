#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 16:32:52 2021

@author: user
"""
import os
os.chdir("/Users/user/Dropbox/project/2020Teaching_CCE/Analy_test_network/")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
paird = sns.color_palette("Paired")


#%%
#read all data
df_C10000G1R10000 = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test_NetworkC10000G1R10000/mergedD5C10000G1R10000.csv.gz")
df_fixed_R2T1 = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test_NetworkC10000G2R2~6/mergedD5C10000G2R2T1.csv.gz")
df_fixed_R3T2 = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test_NetworkC10000G2R2~6/mergedD5C10000G2R3T2.csv.gz")
df_fixed_R4T3 = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test_NetworkC10000G2R2~6/mergedD5C10000G2R4T3.csv.gz")
df_fixed_R5T4 = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test_NetworkC10000G2R2~6/mergedD5C10000G2R5T4.csv.gz")
df_fixed_R6T5 = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test_NetworkC10000G2R2~6/mergedD5C10000G2R6T5.csv.gz")
df_fixed_R10T9 = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test_NetworkC10000G2R2~6/mergedD5C10000G2R10T9.csv.gz")

#%%
#plot df_C10000G1R10000

sns.set_style("ticks")
for i, r in enumerate([1,4,9,16,25]):
    sns.lineplot(x=df_C10000G1R10000.query(f"Reward=={r}").groupby("Round")["Reward"].count().index
                 ,y=df_C10000G1R10000.query(f"Reward=={r}").groupby("Round")["Reward"].count().values
                 ,color=paird[i]
                 ,legend=None
                 )
plt.ylabel("Frequency of agents who reached each goal", fontsize=11)
plt.ylim(-200,10000)
plt.legend([1,2,3,4,5],title="Goal",fontsize=11,loc='upper left', bbox_to_anchor=(1,1),frameon=False).get_title().set_fontsize(11)
plt.savefig("C10000G1R10000/Freq_byReward_test_network.png",bbox_inches="tight",dpi=600)
plt.show()

sns.set_style("ticks")
for r in [1,10,100,10000]:
    temp = df_C10000G1R10000.query(f"Round=={r}")["Reward"].value_counts()
    for rw in [1.0,4.0,9.0,16.0,25.0]:
        if temp.index.isin([rw]).any():
            pass
        else:
            temp[rw] = 0
    temp = temp.sort_index()
    temp.index = ["1","2","3","4","5"]
    temp.plot.bar(color=paird,rot=0)
    plt.ylim(0,10000)
    plt.xlabel("Goal", fontsize=11)
    plt.ylabel("Frequency of agents who reached each goal", fontsize=11)
    plt.savefig(f"C10000G1R10000/hist_reward_test_networkR{r}.png",bbox_inches="tight",dpi=600)
    plt.show()
    print("Round=",r)
    print(temp)
    print(temp/10000)
'''
Round= 1
1    4537
2    3891
3     511
4     718
5     343
Name: Reward, dtype: int64
1    0.4537
2    0.3891
3    0.0511
4    0.0718
5    0.0343
Name: Reward, dtype: float64
Round= 10
1    2159
2    7355
3     294
4     137
5      55
Name: Reward, dtype: int64
1    0.2159
2    0.7355
3    0.0294
4    0.0137
5    0.0055
Name: Reward, dtype: float64
Round= 100
1     518
2    7590
3    1380
4     353
5     159
Name: Reward, dtype: int64
1    0.0518
2    0.7590
3    0.1380
4    0.0353
5    0.0159
Name: Reward, dtype: float64
Round= 10000
1       2
2      61
3    1901
4    5489
5    2546
Name: Reward, dtype: int64
1    0.0002
2    0.0061
3    0.1901
4    0.5489
5    0.2546
Name: Reward, dtype: float64
'''
#%%
#plot df_fixed
for r in [2]:
    temp = df_fixed_R2T1.query(f"Round=={r}")["Reward"].value_counts()
    for rw in [1.0,4.0,9.0,16.0,25.0]:
        if temp.index.isin([rw]).any():
            pass
        else:
            temp[rw] = 0
    temp = temp.sort_index()
    temp.index = ["1","2","3","4","5"]
    temp.plot.bar(color=paird,rot=0)
    plt.ylim(0,10000)
    plt.xlabel("Goal", fontsize=11)
    plt.ylabel("Frequency of agents who reached each goal", fontsize=11)
    plt.savefig(f"fixed_teaching/hist_reward_test_networkR{r}.png",bbox_inches="tight",dpi=600)
    plt.show()
    print("Round=",r)
    print(temp)
    print(temp/10000)
'''
Round= 2
1    4579
2    3735
3     510
4     601
5     575
Name: Reward, dtype: int64
1    0.4579
2    0.3735
3    0.0510
4    0.0601
5    0.0575
Name: Reward, dtype: float64
'''

for r in [3]:
    temp = df_fixed_R3T2.query(f"Round=={r}")["Reward"].value_counts()
    for rw in [1.0,4.0,9.0,16.0,25.0]:
        if temp.index.isin([rw]).any():
            pass
        else:
            temp[rw] = 0
    temp = temp.sort_index()
    temp.index = ["1","2","3","4","5"]
    temp.plot.bar(color=paird,rot=0)
    plt.ylim(0,10000)
    plt.xlabel("Goal", fontsize=11)
    plt.ylabel("Frequency of agents who reached each goal", fontsize=11)
    plt.savefig(f"fixed_teaching/hist_reward_test_networkR{r}.png",bbox_inches="tight",dpi=600)
    plt.show()
    print("Round=",r)
    print(temp)
    print(temp/10000)
'''
Round= 3
1    4404
2    2969
3     474
4     594
5    1559
Name: Reward, dtype: int64
1    0.4404
2    0.2969
3    0.0474
4    0.0594
5    0.1559
Name: Reward, dtype: float64
'''

for r in [4]:
    temp = df_fixed_R4T3.query(f"Round=={r}")["Reward"].value_counts()
    for rw in [1.0,4.0,9.0,16.0,25.0]:
        if temp.index.isin([rw]).any():
            pass
        else:
            temp[rw] = 0
    temp = temp.sort_index()
    temp.index = ["1","2","3","4","5"]
    temp.plot.bar(color=paird,rot=0)
    plt.ylim(0,10000)
    plt.xlabel("Goal", fontsize=11)
    plt.ylabel("Frequency of agents who reached each goal", fontsize=11)
    plt.savefig(f"fixed_teaching/hist_reward_test_networkR{r}.png",bbox_inches="tight",dpi=600)
    plt.show()
    print("Round=",r)
    print(temp)
    print(temp/10000)
'''
Round= 4
1    3841
2    2208
3     432
4     551
5    2968
Name: Reward, dtype: int64
1    0.3841
2    0.2208
3    0.0432
4    0.0551
5    0.2968
Name: Reward, dtype: float64
'''

for r in [5]:
    temp = df_fixed_R5T4.query(f"Round=={r}")["Reward"].value_counts()
    for rw in [1.0,4.0,9.0,16.0,25.0]:
        if temp.index.isin([rw]).any():
            pass
        else:
            temp[rw] = 0
    temp = temp.sort_index()
    temp.index = ["1","2","3","4","5"]
    temp.plot.bar(color=paird,rot=0)
    plt.ylim(0,10000)
    plt.xlabel("Goal", fontsize=11)
    plt.ylabel("Frequency of agents who reached each goal", fontsize=11)
    plt.savefig(f"fixed_teaching/hist_reward_test_networkR{r}.png",bbox_inches="tight",dpi=600)
    plt.show()
    print("Round=",r)
    print(temp)
    print(temp/10000)
'''
Round= 5
1    3242
2    1908
3     359
4     497
5    3994
Name: Reward, dtype: int64
1    0.3242
2    0.1908
3    0.0359
4    0.0497
5    0.3994
Name: Reward, dtype: float64
'''

for r in [6]:
    temp = df_fixed_R6T5.query(f"Round=={r}")["Reward"].value_counts()
    for rw in [1.0,4.0,9.0,16.0,25.0]:
        if temp.index.isin([rw]).any():
            pass
        else:
            temp[rw] = 0
    temp = temp.sort_index()
    temp.index = ["1","2","3","4","5"]
    temp.plot.bar(color=paird,rot=0)
    plt.ylim(0,10000)
    plt.xlabel("Goal", fontsize=11)
    plt.ylabel("Frequency of agents who reached each goal", fontsize=11)
    plt.savefig(f"fixed_teaching/hist_reward_test_networkR{r}.png",bbox_inches="tight",dpi=600)
    plt.show()
    print("Round=",r)
    print(temp)
    print(temp/10000)
'''
Round= 6
1        0
2        0
3        0
4        0
5    10000
Name: Reward, dtype: int64
1    0.0
2    0.0
3    0.0
4    0.0
5    1.0
Name: Reward, dtype: float64
'''

for r in [10]:
    temp = df_fixed_R10T9.query(f"Round=={r}")["Reward"].value_counts()
    for rw in [1.0,4.0,9.0,16.0,25.0]:
        if temp.index.isin([rw]).any():
            pass
        else:
            temp[rw] = 0
    temp = temp.sort_index()
    temp.index = ["1","2","3","4","5"]
    temp.plot.bar(color=paird,rot=0)
    plt.ylim(0,10000)
    plt.xlabel("Goal", fontsize=11)
    plt.ylabel("Frequency of agents who reached each goal", fontsize=11)
    plt.savefig(f"fixed_teaching/hist_reward_test_networkR{r}.png",bbox_inches="tight",dpi=600)
    plt.show()
    print("Round=",r)
    print(temp)
    print(temp/10000)
'''
Round= 10
1        0
2        0
3        0
4        0
5    10000
Name: Reward, dtype: int64
1    0.0
2    0.0
3    0.0
4    0.0
5    1.0
Name: Reward, dtype: float64
'''