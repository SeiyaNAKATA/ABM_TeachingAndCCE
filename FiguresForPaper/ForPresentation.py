#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
os.chdir("/Users/user/Dropbox/project/2020Teaching_CCE/#FiguresForPaper/")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
paird = sns.color_palette("Paired")
#%%
#read all data
df_test5_R10_fround = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G100R10/mergedD5C10000G100R10_fround.csv")
df_test5_R100_fround = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G100R100/mergedD5C10000G100R100_fround.csv")
df_test5_R400_fround = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G100R400/mergedD5C10000G100R400_fround.csv")
df_test5_R5000_fround = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G100R5000/mergedD5C10000G100R5000_fround.csv")
df_test5_R20000_fround = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G100R20000/mergedD5C10000G100R20000_fround.csv")

df_test5_individual = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G1R40000/mergedD5C10000G1R40000.csv")

#%%
#For presentaton: The effect of teaching on cumulative cultural evolution.
#R10G100
sns.set_style("ticks")
mean = df_test5_R10_fround.query("Generation==1")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.xlabel("Generation")
plt.ylabel("Reward")
plt.ylim(3,16.5)
plt.savefig(f"Presentation/R10G100/Line_reward_test5R10Plain.png",bbox_inches="tight",dpi=600)
plt.show()

for t in range(10):
    sns.lineplot(x="Generation", y="Reward", data=df_test5_R10_fround.query(f"Teaching_phase<={t}")
                 , ci=None, hue="Teaching_phase", palette=cycle[1:t+1], legend=False)
    mean = df_test5_R10_fround.query("Generation==1")["Reward"].mean()
    plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
    plt.ylim(3,16.5)
    plt.savefig(f"Presentation/R10G100/Line_reward_test5R10T{t}.png",bbox_inches="tight",dpi=600)
    plt.show()



#%%
generations = [1]+[g for g in range(10,101,10)]
sns.set_style("ticks")

#R10G100
for t in range(1,10):
    for g in generations:
        temp = df_test5_R10_fround.query(f"Teaching_phase=={t}&Generation=={g}")["Reward"].value_counts()
        for rw in [1.0,4.0,9.0,16.0,25.0,36.0]:
            if temp.index.isin([rw]).any():
                pass
            else:
                temp[rw] = 0
        temp = temp.sort_index()
        temp.index = [1,4,9,16,25,36]
        temp.plot(kind="bar",color=paird,rot=0,sharex=True,sharey=True)
        plt.ylim(0,10000)
        plt.xlabel("Reward")
        plt.ylabel("Frequency")
        #plt.title(f"T={t}, Generation {g}")
        plt.savefig(f"Presentation/R10G100/hist_reward_test5G{g}R10T{t}.png",bbox_inches="tight",dpi=600)
        plt.show()

#R100G100
for t in range(10,100,10):
    for g in generations:
        temp = df_test5_R100_fround.query(f"Teaching_phase=={t}&Generation=={g}")["Reward"].value_counts()
        for rw in [1.0,4.0,9.0,16.0,25.0,36.0]:
            if temp.index.isin([rw]).any():
                pass
            else:
                temp[rw] = 0
        temp = temp.sort_index()
        temp.index = [1,4,9,16,25,36]
        temp.plot(kind="bar",color=paird,rot=0,sharex=True,sharey=True)
        plt.ylim(0,10000)
        plt.xlabel("Reward")
        plt.ylabel("Frequency")
        #plt.title(f"T={t}, Generation {g}")
        plt.savefig(f"Presentation/R100G100/hist_reward_test5G{g}R100T{t}.png",bbox_inches="tight",dpi=600)
        plt.show()

#R400G100
for t in range(40,400,40):
    for g in generations:
        temp = df_test5_R400_fround.query(f"Teaching_phase=={t}&Generation=={g}")["Reward"].value_counts()
        for rw in [1.0,4.0,9.0,16.0,25.0,36.0]:
            if temp.index.isin([rw]).any():
                pass
            else:
                temp[rw] = 0
        temp = temp.sort_index()
        temp.index = [1,4,9,16,25,36]
        temp.plot(kind="bar",color=paird,rot=0,sharex=True,sharey=True)
        plt.ylim(0,10000)
        plt.xlabel("Reward")
        plt.ylabel("Frequency")
        #plt.title(f"T={t}, Generation {g}")
        plt.savefig(f"Presentation/R400G100/hist_reward_test5G{g}R400T{t}.png",bbox_inches="tight",dpi=600)
        plt.show()

#R5000G100
for t in range(500,5000,500):
    for g in generations:
        temp = df_test5_R5000_fround.query(f"Teaching_phase=={t}&Generation=={g}")["Reward"].value_counts()
        for rw in [1.0,4.0,9.0,16.0,25.0,36.0]:
            if temp.index.isin([rw]).any():
                pass
            else:
                temp[rw] = 0
        temp = temp.sort_index()
        temp.index = [1,4,9,16,25,36]
        temp.plot(kind="bar",color=paird,rot=0,sharex=True,sharey=True)
        plt.ylim(0,10000)
        plt.xlabel("Reward")
        plt.ylabel("Frequency")
        #plt.title(f"T={t}, Generation {g}")
        plt.savefig(f"Presentation/R5000G100/hist_reward_test5G{g}R5000T{t}.png",bbox_inches="tight",dpi=600)
        plt.show()

#R20000G100
for t in range(2000,20000,2000):
    for g in generations:
        temp = df_test5_R20000_fround.query(f"Teaching_phase=={t}&Generation=={g}")["Reward"].value_counts()
        for rw in [1.0,4.0,9.0,16.0,25.0,36.0]:
            if temp.index.isin([rw]).any():
                pass
            else:
                temp[rw] = 0
        temp = temp.sort_index()
        temp.index = [1,4,9,16,25,36]
        temp.plot(kind="bar",color=paird,rot=0,sharex=True,sharey=True)
        plt.ylim(0,10000)
        plt.xlabel("Reward")
        plt.ylabel("Frequency")
        #plt.title(f"T={t}, Generation {g}")
        plt.savefig(f"Presentation/R20000G100/hist_reward_test5G{g}R20000T{t}.png",bbox_inches="tight",dpi=600)
        plt.show()

#%%

#R10G100
sns.set_style("ticks")
sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R10_fround.query("Generation==100"),
            palette=cycle[1:], ci=None)
#drawing a reference line
mean = df_test5_R10_fround.query("Generation==1")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.ylim(3,16.5)
plt.savefig("Presentation/R10G100/bar_reward_test5G100R10.png",bbox_inches="tight",dpi=600)
plt.show()

#R100G100
sns.set_style("ticks")
sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R100_fround.query("Generation==100"),
            palette=cycle[1:], ci=None)
#drawing a reference line
mean = df_test5_R100_fround.query("Generation==1")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.ylim(3,16.5)
plt.savefig("Presentation/R100G100/bar_reward_test5G100R100.png",bbox_inches="tight",dpi=600)
plt.show()

#R400G100
sns.set_style("ticks")
sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R400_fround.query("Generation==100"),
            palette=cycle[1:], ci=None)
#drawing a reference line
mean = df_test5_R400_fround.query("Generation==1")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.ylim(3,16.5)
plt.savefig("Presentation/R400G100/bar_reward_test5G100R400.png",bbox_inches="tight",dpi=600)
plt.show()

#R5000G100
sns.set_style("ticks")
sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R5000_fround.query("Generation==100"),
            palette=cycle[1:], ci=None)
#drawing a reference line
mean = df_test5_R5000_fround.query("Generation==1")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.ylim(3,16.5)
plt.savefig("Presentation/R5000G100/bar_reward_test5G10050400.png",bbox_inches="tight",dpi=600)
plt.show()

#R20000G100
sns.set_style("ticks")
sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R20000_fround.query("Generation==100"),
            palette=cycle[1:], ci=None)
#drawing a reference line
mean = df_test5_R20000_fround.query("Generation==1")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.ylim(3,16.5)
plt.savefig("Presentation/R20000G100/bar_reward_test5G100R20000.png",bbox_inches="tight",dpi=600)
plt.show()
