import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

generation1 = []
best1 = []
max1 = []
min1 = []
avg1 = []
std1 = []
generationT1 = []
Inc_1 = []
SMA_1 = []
Fit_1 = []
with open('2varcaso1/run01.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT1.append(float(a[1]))
            Inc_1.append(float(a[3]))
            SMA_1.append(float(a[4]))
            Fit_1.append(float(a[6]))
        if a[0] =='Generation':
            gen = a
            generation1.append(int(a[2]))
            best1.append(float(a[5]))
            max1.append(float(a[8]))
            min1.append(float(a[11]))
            avg1.append(float(a[14]))
            std1.append((float(a[17])))

generation2 = []
best2 = []
max2 = []
min2 = []
avg2 = []
std2 = []
generationT2 = []
Inc_2 = []
SMA_2 = []
Fit_2 = []
with open('2varcaso1/run02.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT2.append(float(a[1]))
            Inc_2.append(float(a[3]))
            SMA_2.append(float(a[4]))
            Fit_2.append(float(a[6]))
        if a[0] =='Generation':
            gen = a
            generation2.append(int(a[2]))
            best2.append(float(a[5]))
            max2.append(float(a[8]))
            min2.append(float(a[11]))
            avg2.append(float(a[14]))
            std2.append((float(a[17])))

generation3 = []
best3 = []
max3 = []
min3 = []
avg3 = []
std3 = []
generationT3 = []
Inc_3 = []
SMA_3 = []
Fit_3 = []
with open('2varcaso1/run03.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT3.append(float(a[1]))
            Inc_3.append(float(a[3]))
            SMA_3.append(float(a[4]))
            Fit_3.append(float(a[6]))
        if a[0] =='Generation':
            gen = a
            generation3.append(int(a[2]))
            best3.append(float(a[5]))
            max3.append(float(a[8]))
            min3.append(float(a[11]))
            avg3.append(float(a[14]))
            std3.append((float(a[17])))
'''
generation4 = []
best4 = []
max4 = []
min4 = []
avg4 = []
std4 = []
generationT4 = []
Inc_4 = []
SMA_4 = []
Fit_4 = []
with open('2varcaso1/run04.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT4.append(float(a[1]))
            Inc_4.append(float(a[3]))
            SMA_4.append(float(a[4]))
            Fit_4.append(float(a[6]))
        if a[0] =='Generation':
            gen = a
            generation4.append(int(a[2]))
            best4.append(float(a[5]))
            max4.append(float(a[8]))
            min4.append(float(a[11]))
            avg4.append(float(a[14]))
            std4.append((float(a[17])))
'''
generation5 = []
best5 = []
max5 = []
min5 = []
avg5 = []
std5 = []
generationT5 = []
Inc_5 = []
SMA_5 = []
Fit_5 = []
with open('2varcaso1/run05.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT5.append(float(a[1]))
            Inc_5.append(float(a[3]))
            SMA_5.append(float(a[4]))
            Fit_5.append(float(a[6]))
        if a[0] =='Generation':
            gen = a
            generation5.append(int(a[2]))
            best5.append(float(a[5]))
            max5.append(float(a[8]))
            min5.append(float(a[11]))
            avg5.append(float(a[14]))
            std5.append((float(a[17])))

generation6 = []
best6 = []
max6 = []
min6 = []
avg6 = []
std6 = []
generationT6 = []
Inc_6 = []
SMA_6 = []
Fit_6 = []
with open('2varcaso1/run06.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT6.append(float(a[1]))
            Inc_6.append(float(a[3]))
            SMA_6.append(float(a[4]))
            Fit_6.append(float(a[6]))
        if a[0] =='Generation':
            gen = a
            generation6.append(int(a[2]))
            best6.append(float(a[5]))
            max6.append(float(a[8]))
            min6.append(float(a[11]))
            avg6.append(float(a[14]))
            std6.append((float(a[17])))

generation7 = []
best7 = []
max7 = []
min7 = []
avg7 = []
std7 = []
generationT7 = []
Inc_7 = []
SMA_7 = []
Fit_7 = []
with open('2varcaso1/run07.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT7.append(float(a[1]))
            Inc_7.append(float(a[3]))
            SMA_7.append(float(a[4]))
            Fit_7.append(float(a[6]))
        if a[0] =='Generation':
            gen = a
            generation7.append(int(a[2]))
            best7.append(float(a[5]))
            max7.append(float(a[8]))
            min7.append(float(a[11]))
            avg7.append(float(a[14]))
            std7.append((float(a[17])))

generation8 = []
best8 = []
max8 = []
min8 = []
avg8 = []
std8 = []
generationT8 = []
Inc_8 = []
SMA_8 = []
Fit_8 = []
with open('2varcaso1/run08.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT8.append(float(a[1]))
            Inc_8.append(float(a[3]))
            SMA_8.append(float(a[4]))
            Fit_8.append(float(a[6]))
        if a[0] =='Generation':
            gen = a
            generation8.append(int(a[2]))
            best8.append(float(a[5]))
            max8.append(float(a[8]))
            min8.append(float(a[11]))
            avg8.append(float(a[14]))
            std8.append((float(a[17])))

generation9 = []
best9 = []
max9 = []
min9 = []
avg9 = []
std9 = []
generationT9 = []
Inc_9 = []
SMA_9 = []
Fit_9 = []
with open('2varcaso1/run09.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT9.append(float(a[1]))
            Inc_9.append(float(a[3]))
            SMA_9.append(float(a[4]))
            Fit_9.append(float(a[6]))
        if a[0] =='Generation':
            gen = a
            generation9.append(int(a[2]))
            best9.append(float(a[5]))
            max9.append(float(a[8]))
            min9.append(float(a[11]))
            avg9.append(float(a[14]))
            std9.append((float(a[17])))

generation10 = []
best10 = []
max10 = []
min10 = []
avg10 = []
std10 = []
generationT10 = []
Inc_10 = []
SMA_10 = []
Fit_10 = []
with open('2varcaso1/run10.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT10.append(float(a[1]))
            Inc_10.append(float(a[3]))
            SMA_10.append(float(a[4]))
            Fit_10.append(float(a[6]))
        if a[0] =='Generation':
            gen = a
            generation10.append(int(a[2]))
            best10.append(float(a[5]))
            max10.append(float(a[8]))
            min10.append(float(a[11]))
            avg10.append(float(a[14]))
            std10.append((float(a[17])))

'''Criando DataFrame Best'''

dfbest = pd.DataFrame(best1, columns=['Caso1'])
dfbest2 = pd.DataFrame(best2, columns=['Caso2'])
dfbest = pd.concat([dfbest, dfbest2], axis=1)
dfbest3 = pd.DataFrame(best3, columns=['Caso3'])
dfbest = pd.concat([dfbest, dfbest3], axis=1)
# dfbest4 = pd.DataFrame(best2, columns=['Caso4'])
# dfbest = pd.concat([dfbest, dfbest4], axis=1)
dfbest5 = pd.DataFrame(best2, columns=['Caso5'])
dfbest = pd.concat([dfbest, dfbest5], axis=1)
dfbest6 = pd.DataFrame(best2, columns=['Caso6'])
dfbest = pd.concat([dfbest, dfbest6], axis=1)
dfbest7 = pd.DataFrame(best2, columns=['Caso7'])
dfbest = pd.concat([dfbest, dfbest7], axis=1)
dfbest8 = pd.DataFrame(best2, columns=['Caso8'])
dfbest = pd.concat([dfbest, dfbest8], axis=1)
dfbest9 = pd.DataFrame(best2, columns=['Caso9'])
dfbest = pd.concat([dfbest, dfbest9], axis=1)
dfbest10 = pd.DataFrame(best2, columns=['Caso10'])
dfbest = pd.concat([dfbest, dfbest10], axis=1)
print(dfbest)

'''Criando Dataframe Min'''

dfmin = pd.DataFrame(min1, columns=['Caso1'])
dfmin2 = pd.DataFrame(min2, columns=['Caso2'])
dfmin = pd.concat([dfmin, dfmin2], axis=1)
dfmin3 = pd.DataFrame(min3, columns=['Caso3'])
dfmin = pd.concat([dfmin, dfmin3], axis=1)
# dfmin4 = pd.DataFrame(min4, columns=['Caso4'])
# dfmin = pd.concat([dfmin, dfmin4], axis=1)
dfmin5 = pd.DataFrame(min5, columns=['Caso5'])
dfmin = pd.concat([dfmin, dfmin5], axis=1)
dfmin6 = pd.DataFrame(min6, columns=['Caso6'])
dfmin = pd.concat([dfmin, dfmin6], axis=1)
dfmin7 = pd.DataFrame(min7, columns=['Caso7'])
dfmin = pd.concat([dfmin, dfmin7], axis=1)
dfmin8 = pd.DataFrame(min8, columns=['Caso8'])
dfmin = pd.concat([dfmin, dfmin8], axis=1)
dfmin9 = pd.DataFrame(min9, columns=['Caso9'])
dfmin = pd.concat([dfmin, dfmin9], axis=1)
dfmin10 = pd.DataFrame(min10, columns=['Caso10'])
dfmin = pd.concat([dfmin, dfmin10], axis=1)
# print(dfmin)

'''Criando Dataframe Avg'''

dfavg = pd.DataFrame(avg1, columns=['Caso1'])
dfavg2 = pd.DataFrame(avg2, columns=['Caso2'])
dfavg = pd.concat([dfavg, dfavg2], axis=1)
dfavg3 = pd.DataFrame(avg3, columns=['Caso3'])
dfavg = pd.concat([dfavg, dfavg3], axis=1)
# dfavg4 = pd.DataFrame(avg4, columns=['Caso4'])
# dfavg = pd.concat([dfavg, dfavg4], axis=1)
dfavg5 = pd.DataFrame(avg5, columns=['Caso5'])
dfavg = pd.concat([dfavg, dfavg5], axis=1)
dfavg6 = pd.DataFrame(avg6, columns=['Caso6'])
dfavg = pd.concat([dfavg, dfavg6], axis=1)
dfavg7 = pd.DataFrame(avg7, columns=['Caso7'])
dfavg = pd.concat([dfavg, dfavg7], axis=1)
dfavg8 = pd.DataFrame(avg8, columns=['Caso8'])
dfavg = pd.concat([dfavg, dfavg8], axis=1)
dfavg9 = pd.DataFrame(avg9, columns=['Caso9'])
dfavg = pd.concat([dfavg, dfavg9], axis=1)
dfavg10 = pd.DataFrame(avg10, columns=['Caso10'])
dfavg = pd.concat([dfavg, dfavg10], axis=1)
# print(dfavg)

'''Criando Dataframe STD'''

dfstd = pd.DataFrame(std1, columns=['Caso1'])
dfstd2 = pd.DataFrame(std2, columns=['Caso2'])
dfstd = pd.concat([dfstd, dfstd2], axis=1)
dfstd3 = pd.DataFrame(std3, columns=['Caso3'])
dfstd = pd.concat([dfstd, dfstd3], axis=1)
# dfstd4 = pd.DataFrame(std4, columns=['Caso4'])
# dfstd = pd.concat([dfstd, dfstd4], axis=1)
dfstd5 = pd.DataFrame(std5, columns=['Caso5'])
dfstd = pd.concat([dfstd, dfstd5], axis=1)
dfstd6 = pd.DataFrame(std6, columns=['Caso6'])
dfstd = pd.concat([dfstd, dfstd6], axis=1)
dfstd7 = pd.DataFrame(std7, columns=['Caso7'])
dfstd = pd.concat([dfstd, dfstd7], axis=1)
dfstd8 = pd.DataFrame(std8, columns=['Caso8'])
dfstd = pd.concat([dfstd, dfstd8], axis=1)
dfstd9 = pd.DataFrame(std9, columns=['Caso9'])
dfstd = pd.concat([dfstd, dfstd9], axis=1)
dfstd10 = pd.DataFrame(std10, columns=['Caso10'])
dfstd = pd.concat([dfstd, dfstd10], axis=1)

''' DataFrame de Inclinação '''

dfInc = pd.DataFrame(Inc_1, columns=['Caso1'])
dfInc_2 = pd.DataFrame(Inc_2, columns=['Caso2'])
dfInc = pd.concat([dfInc, dfInc_2], axis=1)
dfInc_3 = pd.DataFrame(Inc_3, columns=['Caso3'])
dfInc = pd.concat([dfInc, dfInc_3], axis=1)
# dfInc_4 = pd.DataFrame(Inc4, columns=['Caso4'])
# dfInc = pd.concat([dfInc, dfInc4], axis=1)
dfInc_5 = pd.DataFrame(Inc_5, columns=['Caso5'])
dfInc = pd.concat([dfInc, dfInc_5], axis=1)
dfInc_6 = pd.DataFrame(Inc_6, columns=['Caso6'])
dfInc = pd.concat([dfInc, dfInc_6], axis=1)
dfInc_7 = pd.DataFrame(Inc_7, columns=['Caso7'])
dfInc = pd.concat([dfInc, dfInc_7], axis=1)
dfInc_8 = pd.DataFrame(Inc_8, columns=['Caso8'])
dfInc = pd.concat([dfInc, dfInc_8], axis=1)
dfInc_9 = pd.DataFrame(Inc_9, columns=['Caso9'])
dfInc = pd.concat([dfInc, dfInc_9], axis=1)
dfInc_10 = pd.DataFrame(Inc_10, columns=['Caso10'])
dfInc = pd.concat([dfInc, dfInc_10], axis=1)

''' DataFrame de SMA'''

dfSMA = pd.DataFrame(SMA_1, columns=['Caso1'])
dfSMA_2 = pd.DataFrame(SMA_2, columns=['Caso2'])
dfSMA = pd.concat([dfSMA, dfSMA_2], axis=1)
dfSMA_3 = pd.DataFrame(SMA_3, columns=['Caso3'])
dfSMA = pd.concat([dfSMA, dfSMA_3], axis=1)
# dfSMA_4 = pd.DataFrame(SMA_4, columns=['Caso4'])
# dfSMA = pd.concat([dfSMA, dfSMA_4], axis=1)
dfSMA_5 = pd.DataFrame(SMA_5, columns=['Caso5'])
dfSMA = pd.concat([dfSMA, dfSMA_5], axis=1)
dfSMA_6 = pd.DataFrame(SMA_6, columns=['Caso6'])
dfSMA = pd.concat([dfSMA, dfSMA_6], axis=1)
dfSMA_7 = pd.DataFrame(SMA_7, columns=['Caso7'])
dfSMA = pd.concat([dfSMA, dfSMA_7], axis=1)
dfSMA_8 = pd.DataFrame(SMA_8, columns=['Caso8'])
dfSMA = pd.concat([dfSMA, dfSMA_8], axis=1)
dfSMA_9 = pd.DataFrame(SMA_9, columns=['Caso9'])
dfSMA = pd.concat([dfSMA, dfSMA_9], axis=1)
dfSMA_10 = pd.DataFrame(SMA_10, columns=['Caso10'])
dfSMA = pd.concat([dfSMA, dfSMA_10], axis=1)

''' DataFrame de Fitness'''

dfFit = pd.DataFrame(Fit_1, columns=['Caso1'])
dfFit_2 = pd.DataFrame(Fit_2, columns=['Caso2'])
dfFit = pd.concat([dfFit, dfFit_2], axis=1)
dfFit_3 = pd.DataFrame(Fit_3, columns=['Caso3'])
dfFit = pd.concat([dfFit, dfFit_3], axis=1)
# dfFit_4 = pd.DataFrame(Fit_4, columns=['Caso4'])
# dfFit = pd.concat([dfFit, dfFit_4], axis=1)
dfFit_5 = pd.DataFrame(Fit_5, columns=['Caso5'])
dfFit = pd.concat([dfFit, dfFit_5], axis=1)
dfFit_6 = pd.DataFrame(Fit_6, columns=['Caso6'])
dfFit = pd.concat([dfFit, dfFit_6], axis=1)
dfFit_7 = pd.DataFrame(Fit_7, columns=['Caso7'])
dfFit = pd.concat([dfFit, dfFit_7], axis=1)
dfFit_8 = pd.DataFrame(Fit_8, columns=['Caso8'])
dfFit = pd.concat([dfFit, dfFit_8], axis=1)
dfFit_9 = pd.DataFrame(Fit_9, columns=['Caso9'])
dfFit = pd.concat([dfFit, dfFit_9], axis=1)
dfFit_10 = pd.DataFrame(Fit_10, columns=['Caso10'])
dfFit = pd.concat([dfFit, dfFit_10], axis=1)

'''Plots'''

'''Plots RAAN por FITNESS'''

plt.scatter(Inc_1, Fit_1, marker='.', label='Simulation 1')
plt.scatter(Inc_2, Fit_2, marker='.', label='Simulation 2')
plt.scatter(Inc_3, Fit_3, marker='.', label='Simulation 3')
# plt.scatter(Inc_4, Fit_4, marker='.')
plt.scatter(Inc_5, Fit_5, marker='.', label='Simulation 5')
plt.scatter(Inc_6, Fit_6, marker='.', label='Simulation 6')
plt.scatter(Inc_7, Fit_7, marker='.', label='Simulation 7')
plt.scatter(Inc_8, Fit_8, marker='.', label='Simulation 8')
plt.scatter(Inc_9, Fit_9, marker='.', label='Simulation 9')
plt.scatter(Inc_10, Fit_10, marker='.', label='Simulation 10')
plt.title('Inclination x Fitness')
plt.xlabel('Inclination')
plt.ylabel('Fitness')
plt.legend()
plt.grid()
plt.show()

''' Plot BEST SOLUTION Média por Geração e Desvio Padrão por Geração '''

dfmeanbest = pd.DataFrame(dfbest.mean(axis=1), columns=['Média_por_Geração'])
dfbest = pd.concat([dfbest, dfmeanbest], axis=1)
dfstdbest = pd.DataFrame(dfbest.std(axis=1), columns=['Desvio_Padrão_por_Geração'])
dfbest = pd.concat([dfbest, dfstdbest], axis=1)

print(dfbest.to_markdown())
fig = plt.figure()
x = dfbest.index
y = dfbest["Média_por_Geração"].tolist()
yerr = dfbest["Desvio_Padrão_por_Geração"].tolist()
plt.grid()
plt.errorbar(x, y, yerr=yerr)
plt.show()

''' Plot MINIMUM VALUE Média por Geração e Desvio Padrão por Geração '''

dfmeanmin = pd.DataFrame(dfmin.mean(axis=1), columns=['Média_por_Geração'])
dfmin = pd.concat([dfmin, dfmeanmin], axis=1)
dfstdmin = pd.DataFrame(dfmin.std(axis=1), columns=['Desvio_Padrão_por_Geração'])
dfmin = pd.concat([dfmin, dfstdmin], axis=1)

print(dfmin.to_markdown())
fig2 = plt.figure()
x = dfmin.index
y = dfmin["Média_por_Geração"].tolist()
yerr = dfmin["Média_por_Geração"].tolist()
plt.grid()
plt.errorbar(x, y, yerr=yerr)
plt.show()

''' Plot AVERAGE VALUE Média por Geração e Desvio Padrão por Geração '''

dfmeanavg = pd.DataFrame(dfavg.mean(axis=1), columns=['Média_por_Geração'])
dfavg = pd.concat([dfavg, dfmeanavg], axis=1)
dfstdavg = pd.DataFrame(dfavg.std(axis=1), columns=['Desvio_Padrão_por_Geração'])
dfavg = pd.concat([dfavg, dfstdavg], axis=1)

print(dfavg.to_markdown())
fig3 = plt.figure()
x = dfavg.index
y = dfavg["Média_por_Geração"].tolist()
yerr = dfavg["Média_por_Geração"].tolist()
plt.grid()
plt.errorbar(x, y, yerr=yerr)
plt.show()

''' Plot STANDART DEVIATION Média por Geração e Desvio Padrão por Geração '''

dfmeanstd = pd.DataFrame(dfstd.mean(axis=1), columns=['Média_por_Geração'])
dfstd = pd.concat([dfstd, dfmeanstd], axis=1)
dfstdstd = pd.DataFrame(dfstd.std(axis=1), columns=['Desvio_Padrão_por_Geração'])
dfstd = pd.concat([dfstd, dfstdstd], axis=1)

print(dfstd.to_markdown())
fig4 = plt.figure()
x = dfstd.index
y = dfstd["Média_por_Geração"].tolist()
yerr = dfstd["Média_por_Geração"].tolist()
plt.grid()
plt.errorbar(x, y, yerr=yerr)
plt.show()
