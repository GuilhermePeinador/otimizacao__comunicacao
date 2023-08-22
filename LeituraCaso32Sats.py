import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import csv
teste = []
generation = []
best = []
max = []
min = []
avg = []
std = []
with open('2Sats/run01.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] =='Generation':
            gen = a
            generation.append(int(a[2]))
            best.append(float(a[5]))
            max.append(float(a[8]))
            min.append(float(a[11]))
            avg.append(float(a[14]))
            std.append((float(a[17])))



'''Plots'''

plt.figure(figsize=(10, 6))

#plt.plot(best , label='Best fitness'     ,  color='black',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
#plt.plot(max , label='Max value'         ,  color='red',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
#plt.plot(min , label='Min value'         ,  color='royalblue',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
#plt.plot(avg , label='Average value'     ,  color='gold',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(std , label='Standart Deviation',  color='gray',     marker='s', markersize='0', linestyle='-',  linewidth = 2)

plt.xlabel('Generations'     , labelpad=20)
plt.ylabel('Std value'    , labelpad=20)

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
plt.savefig('readrun1.png', format='png', dpi=300)

plt.show()
