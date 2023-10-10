import numpy as np
import pandas as pd
import os, sys
import matplotlib.pyplot as plt

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("..")
    return os.path.join(base_path, relative_path)


df1 = pd.read_csv(resource_path("posproc.run01.out"), sep=',', engine='python', on_bad_lines='skip')
Fitness1 = df1.iloc[:, 1]

df2 = pd.read_csv(resource_path("posproc.run02.out"), sep=',', engine='python', on_bad_lines='skip')
Fitness2 = df2.iloc[:, 1]

df3 = pd.read_csv(resource_path("posproc.run03.out"), sep=',', engine='python', on_bad_lines='skip')
Fitness3 = df3.iloc[:, 1]

df4 = pd.read_csv(resource_path("posproc.run04.out"), sep=',', engine='python', on_bad_lines='skip')
Fitness4 = df4.iloc[:, 1]

df5 = pd.read_csv(resource_path("posproc.run05.out"), sep=',', engine='python', on_bad_lines='skip')
Fitness5 = df5.iloc[:, 1]

df6 = pd.read_csv(resource_path("posproc.run06.out"), sep=',', engine='python', on_bad_lines='skip')
Fitness6 = df6.iloc[:, 1]

df7 = pd.read_csv(resource_path("posproc.run07.out"), sep=',', engine='python', on_bad_lines='skip')
Fitness7 = df7.iloc[:, 1]

df8 = pd.read_csv(resource_path("posproc.run08.out"), sep=',', engine='python', on_bad_lines='skip')
Fitness8 = df8.iloc[:, 1]

df9 = pd.read_csv(resource_path("posproc.run09.out"), sep=',', engine='python', on_bad_lines='skip')
Fitness9 = df9.iloc[:, 1]

df10 = pd.read_csv(resource_path("posproc.run10.out"), sep=',', engine='python', on_bad_lines='skip')
Fitness10 = df10.iloc[:, 1]

'''Plots'''

plt.figure(figsize=(10, 6))

plt.plot(Fitness1 , label='Case 1',  color='black',     marker='s', markersize='0', linestyle=':',  linewidth = 2)          #/df1.iloc[-1,1]
plt.plot(Fitness2 , label='Case 2',  color='black',     marker='s', markersize='0', linestyle='--', linewidth = 2)          #/df2.iloc[-1,1]
plt.plot(Fitness3 , label='Case 3',  color='red',       marker='o', markersize='0', linestyle=':',  linewidth = 2)          #/df3.iloc[-1,1]
plt.plot(Fitness4 , label='Case 4',  color='red',       marker='s', markersize='0', linestyle='--', linewidth = 2)          #/df4.iloc[-1,1]
plt.plot(Fitness5 , label='Case 5',  color='royalblue', marker='^', markersize='0', linestyle=':',  linewidth = 2)          #/df5.iloc[-1,1]
plt.plot(Fitness6 , label='Case 6',  color='royalblue', marker='s', markersize='0', linestyle='--', linewidth = 2)          #/df6.iloc[-1,1]
plt.plot(Fitness7 , label='Case 7',  color='gold',      marker='s', markersize='0', linestyle=':',  linewidth = 2)          #/df7.iloc[-1,1]
plt.plot(Fitness8 , label='Case 8',  color='gold',      marker='s', markersize='0', linestyle='--', linewidth = 2)          #/df8.iloc[-1,1]
plt.plot(Fitness9 , label='Case 9',  color='gray',      marker='s', markersize='0', linestyle=':',  linewidth = 2)          #/df9.iloc[-1,1]
plt.plot(Fitness10, label='Case 10', color='gray',      marker='s', markersize='0', linestyle='--', linewidth = 2)          #/df10.iloc[-1,1]


plt.xlabel('Generations (log)', labelpad=20)
plt.ylabel('Fitness',           labelpad=20)
plt.xscale('log')
plt.ylim([0.065, 0.06675])
plt.xticks([3, 10, 30, 100, 300])

plt.legend(ncol=5, bbox_to_anchor=(0.5, -0.2), loc='upper center')
plt.grid()

SIZE = 20
plt.rc('font',   size=SIZE)             # controls default text sizes
plt.rc('axes',   titlesize=SIZE)        # fontsize of the axes title
plt.rc('axes',   labelsize=SIZE)        # fontsize of the x and y labels
plt.rc('xtick',  labelsize=SIZE)        # fontsize of the tick labels
plt.rc('ytick',  labelsize=SIZE)        # fontsize of the tick labels
plt.rc('legend', fontsize=15)           # legend fontsize
plt.rc('figure', titlesize=SIZE)
plt.rcParams["font.family"] = "arial"
plt.savefig('FractionCommunication.png', format='png', dpi=300)

plt.show()
