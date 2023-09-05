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

fig = plt.figure()
plt.grid()
plt.plot(df6800["Fitness"].tolist(), label="6800")
plt.plot(df6900["Fitness"].tolist(), label="6900")
plt.plot(df7000["Fitness"].tolist(), label="7000")
plt.plot(df7100["Fitness"].tolist(), label="7100")
plt.legend()
plt.show()
