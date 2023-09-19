import pandas as pd
import matplotlib.pyplot as plt
import csv

df6800 = pd.read_csv('2Sats-vsraan/2sat-6800.plot')
df6800.columns = ['Gen', 'Inc', 'SMA', 'Fitness']
df6900 = pd.read_csv('2Sats-vsraan/2sat-6900.plot')
df6900.columns = ['Gen', 'Inc', 'SMA', 'Fitness']
df7000 = pd.read_csv('2Sats-vsraan/2sat-7000.plot')
df7000.columns = ['Gen', 'Inc', 'SMA', 'Fitness']
df7100 = pd.read_csv('2Sats-vsraan/2sat-7100.plot')
df7100.columns = ['Gen', 'Inc', 'SMA', 'Fitness']

fig, ax = plt.subplots(figsize=(10, 6))
#plt.figure()
plt.rcParams['figure.figsize'] = [4, 3]
ax.plot(df6800["Fitness"].tolist(), color='black',     marker='.', label="6800")
ax.plot(df6900["Fitness"].tolist(), color='red',     marker='.', label="6900")
ax.plot(df7000["Fitness"].tolist(), color='gold',     marker='.', label="7000")
ax.plot(df7100["Fitness"].tolist(), color='gray',     marker='.', label="7100")

ax.set_title('Inclination x Fitness')
ax.set_xlabel('Inclination')
ax.set_ylabel('Fitness')
#plt.legend(ncol=2, bbox_to_anchor=(0.5, -0.2), loc='upper center')
ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.175),
          ncol=4, fancybox=True, shadow=True)
plt.tight_layout()
plt.grid()

SIZE = 20
plt.rc('font',   size=SIZE)             # controls default text sizes
plt.rc('axes',   titlesize=SIZE)        # fontsize of the axes title
plt.rc('axes',   labelsize=SIZE)        # fontsize of the x and y labels
plt.rc('xtick',  labelsize=SIZE)        # fontsize of the tick labels
plt.rc('ytick',  labelsize=SIZE)        # fontsize of the tick labels
plt.rc('legend', fontsize=15)           # legend fontsize
plt.rc('figure', titlesize=SIZE)        # title fontsize
plt.rcParams["font.family"] = "arial"

plt.show()