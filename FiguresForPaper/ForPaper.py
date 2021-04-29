#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
os.chdir("/Users/user/Dropbox/project/2020Teaching_CCE/FiguresForPaper/")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
paird = sns.color_palette("Paired")


#%%
#read all data
df_test5_R10_fround = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G100R10/mergedD5C10000G100R10_fround.csv.gz")
df_test5_R10_fround_ByG10 = pd.read_feather("/Users/user/Dropbox/project/2020Teaching_CCE/Test5_redC10000G7000R10/mergedD5C10000G7000R10_fround_ByG10.feather")

#df_test5_R100_fround = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5_redC10000G2000R100/mergedD5C10000G2000R100_fround.csv.gz",usecols=["Generation", "Teaching_phase", "Chain", "Reward"],dtype='float32')
#df_test5_R100_fround_ByG10 = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5_redC10000G2000R100/mergedD5C10000G2000R100_fround_ByG10.csv.gz",usecols=["Generation", "Teaching_phase", "Chain", "Reward"],dtype='float32')
#df_test5_R100_fround.to_feather("/Users/user/Dropbox/project/2020Teaching_CCE/Test5_redC10000G2000R100/mergedD5C10000G2000R100_fround.feather")
#df_test5_R100_fround_ByG10.to_feather("/Users/user/Dropbox/project/2020Teaching_CCE/Test5_redC10000G2000R100/mergedD5C10000G2000R100_fround_ByG10.feather")
df_test5_R100_fround = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G100R100/mergedD5C10000G100R100_fround.csv.gz")
df_test5_R100_fround_ByG10 = pd.read_feather("/Users/user/Dropbox/project/2020Teaching_CCE/Test5_redC10000G2000R100/mergedD5C10000G2000R100_fround_ByG10.feather")

#df_test5_R400_fround = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5_redC10000G1000R400/mergedD5C10000G1000R400_fround.csv.gz",usecols=["Generation", "Teaching_phase", "Chain", "Reward"],dtype='float32')
df_test5_R400_fround = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5_redC10000G1000R400/mergedD5C10000G1000R400_fround.csv.gz")
df_test5_R400_fround_ByG10 = pd.read_feather("/Users/user/Dropbox/project/2020Teaching_CCE/Test5_redC10000G1000R400/mergedD5C10000G1000R400_fround_ByG10.feather")

df_test5_R5000_fround = pd.read_feather("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G100R5000/mergedD5C10000G100R5000_fround.feather")

df_test5_R20000_fround = pd.read_feather("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G100R20000/mergedD5C10000G100R20000_fround.feather")

#df_test5_individual = pd.read_feather("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G1R40000/mergedD5C10000G1R40000.feather")

df_test5_individual_ByR10 = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G1R2000000/mergedD5C10000G1R1000000_ByR10.csv.gz",usecols=["Generation", "Round", "Teaching_phase", "Chain", "Reward"],dtype='float32')
df_test5_individual_ByR100 = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G1R2000000/mergedD5C10000G1R1000000_ByR100.csv.gz",usecols=["Generation", "Round", "Teaching_phase", "Chain", "Reward"],dtype='float32')
df_test5_individual_ByR400 = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G1R2000000/mergedD5C10000G1R1000000_ByR400.csv.gz",usecols=["Generation", "Round", "Teaching_phase", "Chain", "Reward"],dtype='float32')
df_test5_individual_ByR5000 = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G1R2000000/mergedD5C10000G1R1000000_ByR5000.csv.gz",usecols=["Generation", "Round", "Teaching_phase", "Chain", "Reward"],dtype='float32')
df_test5_individual_ByR20000 = pd.read_csv("/Users/user/Dropbox/project/2020Teaching_CCE/Test5C10000G1R2000000/mergedD5C10000G1R1000000_ByR20000.csv.gz",usecols=["Generation", "Round", "Teaching_phase", "Chain", "Reward"],dtype='float32')

#%%
#Fig. 5&7 Frequency of the agents who acquired each reward through individual learning at arbitrary rounds.
sns.set_style("ticks")
for r in [1,10,100,400,5000,20000,40000]:
    temp = df_test5_individual.query(f"Round=={r}")["Reward"].value_counts()
    for rw in [1.0,4.0,9.0,16.0,25.0,36.0]:
        if temp.index.isin([rw]).any():
            pass
        else:
            temp[rw] = 0
    temp = temp.sort_index()
    temp.index = ["1","2","3","4","5","6"]
    temp.plot.bar(color=paird,rot=0)
    plt.ylim(0,10000)
    plt.xlabel("Goal", fontsize=11)
    plt.ylabel("Frequency of agents who reached each goal", fontsize=11)
    plt.savefig(f"Individual/hist_reward_test5R{r}.png",bbox_inches="tight",dpi=600)
    plt.show()
    print("Round=",r)
    print(temp)


#%%
#Fig. 6. Frequency transition of the agents who acquired each reward among 40,000 rounds.
sns.set_style("ticks")
for i, r in enumerate([1,4,9,16,25,36]):
    sns.lineplot(x=df_test5_individual.query(f"Reward=={r}").groupby("Round")["Reward"].count().index
                 ,y=df_test5_individual.query(f"Reward=={r}").groupby("Round")["Reward"].count().values
                 ,color=paird[i]
                 ,legend=None
                 )
plt.ylabel("Frequency of agents who reached each goal", fontsize=11)
plt.ylim(-200,10000)
plt.legend([1,2,3,4,5,6],title="Goal",fontsize=11,loc='upper left', bbox_to_anchor=(1,1),frameon=False).get_title().set_fontsize(11)
plt.savefig("Individual/Freq_byReward_test5.png",bbox_inches="tight",dpi=600)
plt.show()


sns.set_style("ticks")
for i, r in enumerate([1,4,9,16,25,36]):
    sns.lineplot(x=df_test5_individual_ByR10.query(f"Reward=={r}").groupby("Round")["Reward"].count().index
                 ,y=df_test5_individual_ByR10.query(f"Reward=={r}").groupby("Round")["Reward"].count().values
                 ,color=paird[i]
                 ,legend=None
                 )
plt.ylabel("Frequency of agents who reached each goal", fontsize=11)
plt.ylim(-200,10000)
plt.legend([1,2,3,4,5,6],title="Goal",fontsize=11,loc='upper left', bbox_to_anchor=(1,1),frameon=False).get_title().set_fontsize(11)
plt.savefig("Individual/Freq_byReward_test5R1000000.png",bbox_inches="tight",dpi=600)
plt.show()

#%%
#Fig. ?
#R=10, G=100
sns.set_style("white")
plt.figure(figsize=(9, 10))
for t in range(1,10):
    for g in range(20,101,20):
        temp = df_test5_R10_fround.query(f"Teaching_phase=={t}&Generation=={g}")["Reward"].value_counts()
        for rw in [1.0,4.0,9.0,16.0,25.0,36.0]:
            if temp.index.isin([rw]).any():
                pass
            else:
                temp[rw] = 0
        temp = temp.sort_index()
        temp.index = [1,4,9,16,25,36]
        plt.subplot(9,5,1+int((t-1)*5)+int((g-1)/20))
        temp.plot(kind="bar",color=paird,rot=0,sharex=True,sharey=True)
        plt.ylim(0,10000)
        plt.tick_params(labelsize=9)
#plt.xlabel("Reward")
#plt.ylabel("Frequency")
#fig.tight_layout()
plt.savefig("Teaching/hist_reward_test5R10G--T--.png"
            ,bbox_inches="tight"
            ,dpi=600)
plt.show()

sns.set_style("ticks")
for t in range(1,10):
    for g in range(20,101,20):
        temp = df_test5_R10_fround_ByG10.query(f"Teaching_phase=={t}&Generation=={g}")["Reward"].value_counts()
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
        plt.title(f"T={t}, Generation {g}")
        plt.savefig(f"Teaching/hist_reward_test5R10G{g}T{t}.png",bbox_inches="tight",dpi=600)
        plt.show()
'''
sns.set_style("ticks")
for t in range(1,10):
    for g in [1000]:
        temp = df_test5_R10_fround_ByG10.query(f"Teaching_phase=={t}&Generation=={g}")["Reward"].value_counts()
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
        plt.title(f"T={t}, Generation {g}")
        plt.savefig(f"Teaching/hist_reward_test5R10G{g}T{t}.png",bbox_inches="tight",dpi=600)
        plt.show()
'''
#R=100, G=100
sns.set_style("ticks")
for t in range(10,100,10):
    for g in range(20,101,20):
        temp = df_test5_R100_fround_ByG10.query(f"Teaching_phase=={t}&Generation=={g}")["Reward"].value_counts()
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
        plt.title(f"T={t}, Generation {g}")
        plt.savefig(f"Teaching/hist_reward_test5R100G{g}T{t}.png",bbox_inches="tight",dpi=600)
        plt.show()

"""
sns.set_style("ticks")
for t in range(10,100,10):
    for g in [2000]:
        temp = df_test5_R100_fround_ByG10.query(f"Teaching_phase=={t}&Generation=={g}")["Reward"].value_counts()
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
        plt.title(f"T={t}, Generation {g}")
        plt.savefig(f"Teaching/hist_reward_test5R100G{g}T{t}.png",bbox_inches="tight",dpi=600)
        plt.show()
"""

#R=400, G=100
sns.set_style("ticks")
for t in range(40,400,40):
    for g in range(20,101,20):
        temp = df_test5_R400_fround_ByG10.query(f"Teaching_phase=={t}&Generation=={g}")["Reward"].value_counts()
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
        plt.title(f"T={t}, Generation {g}")
        plt.savefig(f"Teaching/hist_reward_test5R400G{g}T{t}.png",bbox_inches="tight",dpi=600)
        plt.show()
"""
sns.set_style("ticks")
for t in range(40,400,40):
    for g in [1000]:
        temp = df_test5_R400_fround_ByG10.query(f"Teaching_phase=={t}&Generation=={g}")["Reward"].value_counts()
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
        plt.title(f"T={t}, Generation {g}")
        plt.savefig(f"Teaching/hist_reward_test5R400G{g}T{t}.png",bbox_inches="tight",dpi=600)
        plt.show()
"""
#R=5000, G=100
sns.set_style("ticks")
for t in range(500,5000,500):
    for g in range(20,101,20):
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
        plt.title(f"T={t}, Generation {g}")
        plt.savefig(f"Teaching/hist_reward_test5R5000G{g}T{t}.png",bbox_inches="tight",dpi=600)
        plt.show()


#R=20000, G=100
sns.set_style("ticks")
for t in range(2000,20000,2000):
    for g in range(20,101,20):
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
        plt.title(f"T={t}, Generation {g}")
        plt.savefig(f"Teaching/hist_reward_test5R20000G{g}T{t}.png",bbox_inches="tight",dpi=600)
        plt.show()

"""
sns.set_style("ticks")
for t in range(2000,20000,2000):
    for g in [50]:
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
        plt.title(f"T={t}, Generation {g}")
        plt.savefig(f"Teaching/hist_reward_test5R20000G{g}T{t}.png",bbox_inches="tight",dpi=600)
        plt.show()
"""

#%%
#Fig. 7A The effect of teaching on cumulative cultural evolution.

#R=10, G=100
#drawing line plot
sns.lineplot(x="Generation", y="Reward", data=df_test5_R10_fround.query("Generation<=100"), ci=None, hue="Teaching_phase", palette=cycle[1:])
plt.legend(["10%","20%","30%","40%","50%","60%","70%","80%","90%"],title="Teaching phase",fontsize=10
           ,frameon=False).get_title().set_fontsize(10)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR10.query("Round==10")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(3,18)
plt.savefig("Teaching/Line_reward_test5R10G100_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#%%
#R=10, G=100
#Fig. 7B
sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R10_fround_ByG10.query("Generation==100"),
            palette=cycle[1:],ci="sd")
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR10.query("Round==10")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.ylim(0,36.5)
plt.savefig("Teaching/hist_reward_test5R10G100_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#%%
#Fig. 8

#R=10, G=7000
#drawing line plot
sns.lineplot(x="Generation", y="Reward", data=df_test5_R10_fround_ByG10, ci=None, hue="Teaching_phase", palette=cycle[1:])
plt.legend(["10%","20%","30%","40%","50%","60%","70%","80%","90%"],title="Teaching phase",fontsize=10
           ,loc='upper left'
           ,bbox_to_anchor=(1.0,1.0)
           ,frameon=False).get_title().set_fontsize(10)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR10.query("Round==10")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("Teaching/Line_reward_test5R10G7000_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

'''
sns.lineplot(x="Generation", y="Reward", data=df_test5_R10_fround_ByG10.query("Generation<=1000"), ci=None, hue="Teaching_phase", palette=cycle[1:])
plt.legend(["10%","20%","30%","40%","50%","60%","70%","80%","90%"],title="Teaching phase",fontsize=10
           ,loc='upper left'
           ,bbox_to_anchor=(1.0,1.0)
           ,frameon=False).get_title().set_fontsize(10)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR10.query("Round==10")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("Teaching/Line_reward_test5R10G1000_ymod.png",bbox_inches="tight",dpi=600)
plt.show()
'''

'''
sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R10_fround_ByG10.query("Generation==500"),
            palette=cycle[1:], ci='sd').set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%"])
#drawing a reference line
mean = df_test5_individual_ByR10.query("Round==10")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("Teaching/hist_reward_test5R10G500_ymod.png",bbox_inches="tight",dpi=600)
plt.show()
'''

'''
sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R10_fround_ByG10.query("Generation==1000"),
            palette=cycle[1:], ci='sd').set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%"])
#drawing a reference line
mean = df_test5_individual_ByR10.query("Round==10")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("Teaching/hist_reward_test5R10G1000_ymod.png",bbox_inches="tight",dpi=600)
plt.show()
'''

'''
sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R10_fround_ByG10.query("Generation==3000"),
            palette=cycle[1:], ci='sd').set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%"])
#drawing a reference line
mean = df_test5_individual_ByR10.query("Round==10")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("Teaching/hist_reward_test5R10G3000_ymod.png",bbox_inches="tight",dpi=600)
plt.show()
'''

sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R10_fround_ByG10.query("Generation==7000"),
            palette=cycle[1:], ci='sd').set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%"])
#drawing a reference line
mean = df_test5_individual_ByR10.query("Round==10")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("Teaching/hist_reward_test5R10G7000_ymod.png",bbox_inches="tight",dpi=600)
plt.show()


#R=100,G=100
#drawing line plot
sns.lineplot(x="Generation", y="Reward", data=df_test5_R100_fround, ci=None, hue="Teaching_phase", palette=cycle[1:]
             ,legend=False)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR100.query("Round==100")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("Teaching/Line_reward_test5R100G100_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R100_fround_ByG10.query("Generation==100"),
            palette=cycle[1:], ci='sd').set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%"])
#drawing a reference line
mean = df_test5_individual_ByR100.query("Round==100")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teachingphase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("Teaching/hist_reward_test5R100G100_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#R=100,G=500
sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R100_fround_ByG10.query("Generation==500"),
            palette=cycle[1:], ci='sd').set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%"])
#drawing a reference line
mean = df_test5_individual_ByR100.query("Round==100")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teachingphase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("Teaching/hist_reward_test5R100G500_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#R=100,G=2000
#drawing line plot
sns.lineplot(x="Generation", y="Reward", data=df_test5_R100_fround_ByG10, ci=None, hue="Teaching_phase", palette=cycle[1:]
             ,legend=False)
plt.legend(["10%","20%","30%","40%","50%","60%","70%","80%","90%"],title="Teaching phase",fontsize=10
           ,loc='upper left'
           ,bbox_to_anchor=(1.0,1.0)
           ,frameon=False).get_title().set_fontsize(10)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR100.query("Round==100")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("Teaching/Line_reward_test5R100G2000_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R100_fround_ByG10.query("Generation==2000"),
            palette=cycle[1:], ci='sd').set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%"])
#drawing a reference line
mean = df_test5_individual_ByR100.query("Round==100")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teaching_phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("Teaching/hist_reward_test5R100G2000_ymod.png",bbox_inches="tight",dpi=600)
plt.show()


#R=400, G=100
#drawing line plot
sns.lineplot(x="Generation", y="Reward", data=df_test5_R400_fround.query("Generation<=100"), ci=None, hue="Teaching_phase", palette=cycle[1:]
             ,legend=False)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR400.query("Round==400")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("Teaching/Line_reward_test5R400G100_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R400_fround_ByG10.query("Generation==100"),
            palette=cycle[1:], ci="sd").set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%"])
#drawing a reference line
mean = df_test5_individual_ByR400.query("Round==400")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("Teaching/hist_reward_test5R400G100_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#R=400, G=500
sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R400_fround_ByG10.query("Generation==500"),
            palette=cycle[1:], ci="sd").set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%"])
#drawing a reference line
mean = df_test5_individual_ByR400.query("Round==400")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("Teaching/hist_reward_test5R400G500_ymod.png",bbox_inches="tight",dpi=600)
plt.show()


#R=400, G=1000
#drawing line plot
sns.lineplot(x="Generation", y="Reward", data=df_test5_R400_fround_ByG10, ci=None, hue="Teaching_phase", palette=cycle[1:]
             ,legend=False)
plt.legend(["10%","20%","30%","40%","50%","60%","70%","80%","90%"],title="Teaching phase",fontsize=10
           ,loc='upper left'
           ,bbox_to_anchor=(1.0,1.0)
           ,frameon=False).get_title().set_fontsize(10)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR400.query("Round==400")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("Teaching/Line_reward_test5R400G1000_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R400_fround_ByG10.query("Generation==1000"),
            palette=cycle[1:], ci="sd").set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%"])
#drawing a reference line
mean = df_test5_individual_ByR400.query("Round==400")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("Teaching/hist_reward_test5R400G1000_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#R=5000
sns.lineplot(x="Generation", y="Reward", data=df_test5_R5000_fround, ci=None, hue="Teaching_phase", palette=cycle[1:]
             ,legend=False)
plt.legend(["10%","20%","30%","40%","50%","60%","70%","80%","90%"],title="Teaching phase",fontsize=10
           ,loc='upper left'
           ,bbox_to_anchor=(1.0,1.0)
           ,frameon=False).get_title().set_fontsize(10)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR5000.query("Round==5000")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("Teaching/Line_reward_test5R5000G100_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R5000_fround.query("Generation==100"),
            palette=cycle[1:], ci="sd").set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%"])
#drawing a reference line
mean = df_test5_individual_ByR5000.query("Round==5000")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("Teaching/hist_reward_test5R5000G100_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#R=5000, G=20
sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R5000_fround.query("Generation==20"),
            palette=cycle[1:], ci="sd").set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%"])
#drawing a reference line
mean = df_test5_individual_ByR5000.query("Round==5000")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("Teaching/hist_reward_test5R5000G20_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#R=20000
sns.lineplot(x="Generation", y="Reward", data=df_test5_R20000_fround.query("Generation<=50"), ci=None, hue="Teaching_phase", palette=cycle[1:]
             ,legend=False)
plt.legend(["10%","20%","30%","40%","50%","60%","70%","80%","90%"],title="Teaching phase",fontsize=10
           ,loc='upper left'
           ,bbox_to_anchor=(1.0,1.0)
           ,frameon=False).get_title().set_fontsize(10)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR20000.query("Round==20000")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("Teaching/Line_reward_test5R20000G50_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R20000_fround.query("Generation==50"),
            palette=cycle[1:], ci="sd").set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%"])
#drawing a reference line
mean = df_test5_R20000_fround.query("Generation==1")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("Teaching/hist_reward_test5R20000G50_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#R=20000, G=10
sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R20000_fround.query("Generation==10"),
            palette=cycle[1:], ci="sd").set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%"])
#drawing a reference line
mean = df_test5_R20000_fround.query("Generation==1")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("Teaching/hist_reward_test5R20000G10_ymod.png",bbox_inches="tight",dpi=600)
plt.show()


#%%
#Fig.10 added individual only

#R=10, G=7000
#drawing line plot
palette = cycle[1:] + ["k"]
sns.lineplot(x="Generation", y="Reward", data=df_test5_R10_fround_ByG10
             , ci=None
             , hue="Teaching_phase"
             , palette=palette[:-1]
             ,legend=None)
y=df_test5_individual_ByR10.query("Round<=70000").groupby("Round")["Reward"].mean().values.tolist()
plt.plot([g for g in range(1,7001)],y,color="k",linewidth=3)
plt.legend(["10%","20%","30%","40%","50%","60%","70%","80%","90%","Immortal"]
           ,ncol=2
           ,title="Teaching phase"
           ,fontsize=12
           ,frameon=False).get_title().set_fontsize(12)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR10.query("Round==10")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("T0/Line_reward_test5R10G7000_T0_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#drawing bar plot
palette = cycle[1:] + ["k"]
df_test5_R10_T0 = df_test5_individual_ByR10.query("Round==70000")
df_test5_R10_T0 = df_test5_R10_T0.append(df_test5_R10_fround_ByG10.query("Generation==7000"), ignore_index=True)
sns.barplot(x="Teaching_phase", y="Reward",data=df_test5_R10_T0
            ,order=[t for t in range(1,10,1)]+[0]
            ,ci="sd"
            ,palette=palette).set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%","Immortal"])
#drawing a reference line
mean = df_test5_individual_ByR10.query("Round==10")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.ylim(0,36.5)
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.savefig("T0/hist_reward_test5R10G7000_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

'''
palette = cycle[1:] + ["k"]
sns.lineplot(x="Generation", y="Reward", data=df_test5_R10_fround_ByG10.query("Generation<=100")
             ,ci=None
             ,hue="Teaching_phase"
             ,palette=palette[:-1]
             ,legend=None)
y=df_test5_individual_ByR10.query("Round<=1000").groupby("Round")["Reward"].mean().values.tolist()
plt.plot([g for g in range(1,101)],y,color="k",linewidth=3)
plt.legend(["10%","20%","30%","40%","50%","60%","70%","80%","90%","Immortal"]
           ,ncol=2
           ,title="Teaching phase"
           ,fontsize=12
           ,frameon=False).get_title().set_fontsize(12)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR10.query("Round==10")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("T0/Line_reward_test5R10G100_T0_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#drawing bar plot
palette = cycle[1:] + ["k"]
df_test5_R10_T0 = df_test5_individual_ByR10.query("Round==1000")
df_test5_R10_T0 = df_test5_R10_T0.append(df_test5_R10_fround_ByG10.query("Generation==100"), ignore_index=True)
sns.barplot(x="Teaching_phase", y="Reward",data=df_test5_R10_T0
            ,order=[t for t in range(1,10,1)]+[0]
            ,ci="sd"
            ,palette=palette).set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%","Immortal"])
#drawing a reference line
mean = df_test5_individual_ByR10.query("Round==10")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.ylim(0,36.5)
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.savefig("T0/hist_reward_test5R10G100_ymod.png",bbox_inches="tight",dpi=600)
plt.show()
'''

#R=100, G=2000
#drawing line plot
sns.lineplot(x="Generation", y="Reward", data=df_test5_R100_fround_ByG10, ci=None, hue="Teaching_phase", palette=cycle[1:]
             ,legend=False)
y=df_test5_individual_ByR100.query("Round<=200000").groupby("Round")["Reward"].mean().values.tolist()
plt.plot([g for g in range(1,2001)],y,color="k",linewidth=3)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR100.query("Round==100")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("T0/Line_reward_test5R100G2000_T0_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#drawing bar plot
palette = cycle[1:] + ["k"]
df_test5_R100_T0 = df_test5_R100_fround_ByG10.query("Generation==2000")
df_test5_R100_T0 = df_test5_R100_T0.append(df_test5_individual_ByR100.query("Round==200000"), ignore_index=True)
sns.barplot(x="Teaching_phase", y="Reward",data=df_test5_R100_T0
            ,ci="sd"
            ,order=[t for t in range(10,100,10)]+[0]
            ,palette=palette).set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%","Immortal"])
#drawing a reference line
mean = df_test5_individual_ByR100.query("Round==100")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.ylim(0,36.5)
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.savefig("T0/hist_reward_test5R100G2000_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

'''
sns.lineplot(x="Generation", y="Reward", data=df_test5_R100_fround_ByG10.query("Generation<=100"), ci=None, hue="Teaching_phase", palette=cycle[1:]
             ,legend=False)
y=df_test5_individual_ByR100.query("Round<=10000").groupby("Round")["Reward"].mean().values.tolist()
plt.plot([g for g in range(1,101)],y,color="k",linewidth=3)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR100.query("Round==100")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("T0/Line_reward_test5R100G100_T0_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#drawing bar plot
palette = cycle[1:] + ["k"]
df_test5_R100_T0 = df_test5_R100_fround_ByG10.query("Generation==100")
df_test5_R100_T0 = df_test5_R100_T0.append(df_test5_individual_ByR100.query("Round==10000"), ignore_index=True)
sns.barplot(x="Teaching_phase", y="Reward",data=df_test5_R100_T0
            ,ci="sd"
            ,order=[t for t in range(10,100,10)]+[0]
            ,palette=palette).set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%","Immortal"])
#drawing a reference line
mean = df_test5_individual_ByR100.query("Round==100")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.ylim(0,36.5)
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.savefig("T0/hist_reward_test5R100G100_ymod.png",bbox_inches="tight",dpi=600)
plt.show()
'''

#R=400, G=1000
#drawing line plot
sns.lineplot(x="Generation", y="Reward", data=df_test5_R400_fround_ByG10, ci=None, hue="Teaching_phase", palette=cycle[1:]
             ,legend=False)
y=df_test5_individual_ByR400.query("Round<=400000").groupby("Round")["Reward"].mean().values.tolist()
plt.plot([g for g in range(1,1001)],y,color="k",linewidth=3)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR400.query("Round==400")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("T0/Line_reward_test5R400G1000_T0_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#drawing bar plot
palette = cycle[1:] + ["k"]
df_test5_R400_T0 = df_test5_R400_fround_ByG10.query("Generation==1000")
df_test5_R400_T0 = df_test5_R400_T0.append(df_test5_individual_ByR400.query("Round==400000"), ignore_index=True)
sns.barplot(x="Teaching_phase", y="Reward",data=df_test5_R400_T0
            ,order=[t for t in range(40,400,40)]+[0]
            ,palette=palette, ci ="sd").set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%","Immortal"])
#drawing a reference line
mean = df_test5_individual_ByR400.query("Round==400")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.ylim(0,36.5)
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.savefig("T0/hist_reward_test5R400G1000_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#drawing line plot
sns.lineplot(x="Generation", y="Reward", data=df_test5_R400_fround_ByG10.query("Generation<=100"), ci=None, hue="Teaching_phase", palette=cycle[1:]
             ,legend=False)
y=df_test5_individual_ByR400.query("Round<=40000").groupby("Round")["Reward"].mean().values.tolist()
plt.plot([g for g in range(1,101)],y,color="k",linewidth=3)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR400.query("Round==400")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("T0/Line_reward_test5R400G100_T0_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#drawing bar plot
palette = cycle[1:] + ["k"]
df_test5_R400_T0 = df_test5_R400_fround_ByG10.query("Generation==100")
df_test5_R400_T0 = df_test5_R400_T0.append(df_test5_individual_ByR400.query("Round==40000"), ignore_index=True)
sns.barplot(x="Teaching_phase", y="Reward",data=df_test5_R400_T0
            ,order=[t for t in range(40,400,40)]+[0]
            ,palette=palette, ci ="sd").set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%","Immortal"])
#drawing a reference line
mean = df_test5_individual_ByR400.query("Round==400")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.ylim(0,36.5)
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.savefig("T0/hist_reward_test5R400G100_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#R=5000, G=100
sns.lineplot(x="Generation", y="Reward", data=df_test5_R5000_fround, ci=None, hue="Teaching_phase", palette=cycle[1:]
             ,legend=False)
y=df_test5_individual_ByR5000.query("Round<=500000").groupby("Round")["Reward"].mean().values.tolist()
plt.plot([g for g in range(1,101)],y,color="k",linewidth=3)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR5000.query("Round==5000")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("T0/Line_reward_test5R5000G100_T0_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

palette = cycle[1:] + ["k"]
df_test5_R5000_T0 = df_test5_R5000_fround.query("Generation==100")
df_test5_R5000_T0 = df_test5_R5000_T0.append(df_test5_individual_ByR5000.query("Round==500000"), ignore_index=True)
sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R5000_T0
            ,order=[t for t in range(500,5000,500)]+[0]
            ,palette=palette, ci ="sd").set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%","Immortal"])
#drawing a reference line
mean = df_test5_individual_ByR5000.query("Round==5000")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("T0/hist_reward_test5R5000G100_T0_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#R=20000, G=50
sns.lineplot(x="Generation", y="Reward", data=df_test5_R20000_fround.query("Generation<=50"), ci=None, hue="Teaching_phase", palette=cycle[1:]
             ,legend=False)
y=df_test5_individual_ByR20000.query("Round<=1000000").groupby("Round")["Reward"].mean().values.tolist()
plt.plot([g for g in range(1,51)],y,color="k",linewidth=3)
plt.xlabel("Generation",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
#drawing a reference line
mean = df_test5_individual_ByR20000.query("Round==20000")["Reward"].mean()
plt.axhline(y=mean, xmin=-5, xmax=105, color='k', linestyle='dashed')
plt.ylim(1,36.5)
plt.savefig("T0/Line_reward_test5R20000G50_T0_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

palette = cycle[1:] + ["k"]
df_test5_R20000_T0 = df_test5_individual_ByR20000.query("Round==1000000")
df_test5_R20000_T0 = df_test5_R20000_T0.append(df_test5_R20000_fround.query("Generation==50"), ignore_index=True)
sns.barplot(x="Teaching_phase", y="Reward", data=df_test5_R20000_T0
            ,order=[t for t in range(2000,20000,2000)]+[0]
            ,palette=palette,ci="sd").set_xticklabels(["10%","20%","30%","40%","50%","60%","70%","80%","90%","Immortal"])
#drawing a reference line
mean = df_test5_individual_ByR20000.query("Round==20000")["Reward"].mean()
plt.axhline(y=mean, color='k', linestyle='dashed')
plt.xlabel("Teaching phase",fontsize=16)
plt.ylabel("Mean reward",fontsize=16)
plt.ylim(0,36.5)
plt.savefig("T0/hist_reward_test5R20000G50_T0_ymod.png",bbox_inches="tight",dpi=600)
plt.show()

#%%

