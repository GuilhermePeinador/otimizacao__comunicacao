import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import plotly.express as px

generation1 = []
best1 = []
max1 = []
min1 = []
avg1 = []
std1 = []
generationT1 = []
FitTot_1 = []
Rsat2_1 = []
Fitsat1_1 = []
Fitsat2_1 = []
with open('2Sats/run01.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT1.append(float(a[1]))
            Rsat2_1.append(float(a[5]))
            FitTot_1.append(float(a[7]))
            Fitsat1_1.append(float(a[13]))
            Fitsat2_1.append(float(a[16]))
        if a[0] == 'Generation':
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
FitTot_2 = []
Rsat2_2 = []
Fitsat1_2 = []
Fitsat2_2 = []
with open('2Sats/run02.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT2.append(float(a[1]))
            Rsat2_2.append(float(a[5]))
            FitTot_2.append(float(a[7]))
            Fitsat1_2.append(float(a[13]))
            Fitsat2_2.append(float(a[16]))
        if a[0] == 'Generation':
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
FitTot_3 = []
Rsat2_3 = []
Fitsat1_3 = []
Fitsat2_3 = []
with open('2Sats/run03.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT3.append(float(a[1]))
            Rsat2_3.append(float(a[5]))
            FitTot_3.append(float(a[7]))
            Fitsat1_3.append(float(a[13]))
            Fitsat2_3.append(float(a[16]))
        if a[0] == 'Generation':
            gen = a
            generation3.append(int(a[2]))
            best3.append(float(a[5]))
            max3.append(float(a[8]))
            min3.append(float(a[11]))
            avg3.append(float(a[14]))
            std3.append((float(a[17])))

generation4 = []
best4 = []
max4 = []
min4 = []
avg4 = []
std4 = []
generationT4 = []
FitTot_4 = []
Rsat2_4 = []
Fitsat1_4 = []
Fitsat2_4 = []
with open('2Sats/run04.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT4.append(float(a[1]))
            Rsat2_4.append(float(a[5]))
            FitTot_4.append(float(a[7]))
            Fitsat1_4.append(float(a[13]))
            Fitsat2_4.append(float(a[16]))
        if a[0] == 'Generation':
            gen = a
            generation4.append(int(a[2]))
            best4.append(float(a[5]))
            max4.append(float(a[8]))
            min4.append(float(a[11]))
            avg4.append(float(a[14]))
            std4.append((float(a[17])))

generation5 = []
best5 = []
max5 = []
min5 = []
avg5 = []
std5 = []
generationT5 = []
FitTot_5 = []
Rsat2_5 = []
Fitsat1_5 = []
Fitsat2_5 = []
with open('2Sats/run05.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT5.append(float(a[1]))
            Rsat2_5.append(float(a[5]))
            FitTot_5.append(float(a[7]))
            Fitsat1_5.append(float(a[13]))
            Fitsat2_5.append(float(a[16]))
        if a[0] == 'Generation':
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
FitTot_6 = []
Rsat2_6 = []
Fitsat1_6 = []
Fitsat2_6 = []
with open('2Sats/run06.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT6.append(float(a[1]))
            Rsat2_6.append(float(a[5]))
            FitTot_6.append(float(a[7]))
            Fitsat1_6.append(float(a[13]))
            Fitsat2_6.append(float(a[16]))
        if a[0] == 'Generation':
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
FitTot_7 = []
Rsat2_7 = []
Fitsat1_7 = []
Fitsat2_7 = []
with open('2Sats/run07.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT7.append(float(a[1]))
            Rsat2_7.append(float(a[5]))
            FitTot_7.append(float(a[7]))
            Fitsat1_7.append(float(a[13]))
            Fitsat2_7.append(float(a[16]))
        if a[0] == 'Generation':
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
FitTot_8 = []
Rsat2_8 = []
Fitsat1_8 = []
Fitsat2_8 = []
with open('2Sats/run08.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT8.append(float(a[1]))
            Rsat2_8.append(float(a[5]))
            FitTot_8.append(float(a[7]))
            Fitsat1_8.append(float(a[13]))
            Fitsat2_8.append(float(a[16]))
        if a[0] == 'Generation':
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
FitTot_9 = []
Rsat2_9 = []
Fitsat1_9 = []
Fitsat2_9 = []
with open('2Sats/run09.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT9.append(float(a[1]))
            Rsat2_9.append(float(a[5]))
            FitTot_9.append(float(a[7]))
            Fitsat1_9.append(float(a[13]))
            Fitsat2_9.append(float(a[16]))
        if a[0] == 'Generation':
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
FitTot_10 = []
Rsat2_10 = []
Fitsat1_10 = []
Fitsat2_10 = []
with open('2Sats/run10.out', 'r') as arquivo_csv:

    read = csv.reader(arquivo_csv, delimiter="\n")

    for linha in read:
        a = linha[0].split()
        if a[0] == 'Gen':
            generationT10.append(float(a[1]))
            Rsat2_10.append(float(a[5]))
            FitTot_10.append(float(a[7]))
            Fitsat1_10.append(float(a[13]))
            Fitsat2_10.append(float(a[16]))
        if a[0] == 'Generation':
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
dfbest4 = pd.DataFrame(best2, columns=['Caso4'])
dfbest = pd.concat([dfbest, dfbest4], axis=1)
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

'''Criando Dataframe Min'''

dfmin = pd.DataFrame(min1, columns=['Caso1'])
dfmin2 = pd.DataFrame(min2, columns=['Caso2'])
dfmin = pd.concat([dfmin, dfmin2], axis=1)
dfmin3 = pd.DataFrame(min3, columns=['Caso3'])
dfmin = pd.concat([dfmin, dfmin3], axis=1)
dfmin4 = pd.DataFrame(min4, columns=['Caso4'])
dfmin = pd.concat([dfmin, dfmin4], axis=1)
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
dfavg4 = pd.DataFrame(avg4, columns=['Caso4'])
dfavg = pd.concat([dfavg, dfavg4], axis=1)
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
dfstd4 = pd.DataFrame(std4, columns=['Caso4'])
dfstd = pd.concat([dfstd, dfstd4], axis=1)
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


''' GRÁFICOS '''
''' Plot Scatter Raan x Fitness '''

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(Rsat2_1, FitTot_1,   color='black',     marker='.',  label='Simulation 1')
ax.scatter(Rsat2_2, FitTot_2,   color='black',     marker='.',  label='Simulation 2')
ax.scatter(Rsat2_3, FitTot_3,   color='red',       marker='.',  label='Simulation 3')
ax.scatter(Rsat2_4, FitTot_4,   color='red',       marker='.',  label='Simulation 4')
ax.scatter(Rsat2_5, FitTot_5,   color='royalblue', marker='.',  label='Simulation 5')
ax.scatter(Rsat2_6, FitTot_6,   color='royalblue', marker='.',  label='Simulation 6')
ax.scatter(Rsat2_7, FitTot_7,   color='gold',      marker='.',  label='Simulation 7')
ax.scatter(Rsat2_8, FitTot_8,   color='gold',      marker='.',  label='Simulation 8')
ax.scatter(Rsat2_9, FitTot_9,   color='gray',      marker='.',  label='Simulation 9')
ax.scatter(Rsat2_10, FitTot_10, color='gray',      marker='.',  label='Simulation 10')

ax.set_title('Raan x Fitness')
ax.set_xlabel('Raan')
ax.set_ylabel('Fitness')
ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.25),
          ncol=5, fancybox=True, shadow=True)
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
# Plot BEST SOLUTION Média por Geração e Desvio Padrão por Geração

dfmeanbest = pd.DataFrame(dfbest.mean(axis=1), columns=['Média_por_Geração'])
dfbest = pd.concat([dfbest, dfmeanbest], axis=1)
dfstdbest = pd.DataFrame(dfbest.std(axis=1), columns=['Desvio_Padrão_por_Geração'])
dfbest = pd.concat([dfbest, dfstdbest], axis=1)

print(dfbest.to_markdown())
fig, ax = plt.subplots(figsize=(10, 6))
x = dfbest.index
y = dfbest["Média_por_Geração"].tolist()
yerr = dfbest["Desvio_Padrão_por_Geração"].tolist()
ax.set_title('Best Solution x Generations')
ax.set_xlabel('Generations')
ax.set_ylabel('Best Solution Mean')
plt.errorbar(x, y, yerr=yerr)
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

'''
# Plot MINIMUM VALUE Média por Geração e Desvio Padrão por Geração 

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

# Plot AVERAGE VALUE Média por Geração e Desvio Padrão por Geração

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

# Plot AVERAGE VALUE Média por Geração e Desvio Padrão por Geração 

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


plt.plot(best1 , label='Best fitness'     ,  color='black',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(best2 , label='Best fitness'     ,  color='black',     marker='s', markersize='0', linestyle='-.',  linewidth = 2)
plt.plot(best3 , label='Best fitness'     ,  color='royalblue',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(best4 , label='Best fitness'     ,  color='royalblue',     marker='s', markersize='0', linestyle='-.',  linewidth = 2)
plt.plot(best5 , label='Best fitness'     ,  color='red',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(best6 , label='Best fitness'     ,  color='red',     marker='s', markersize='0', linestyle='-.',  linewidth = 2)
plt.plot(best7 , label='Best fitness'     ,  color='gray',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(best8 , label='Best fitness'     ,  color='gray',     marker='s', markersize='0', linestyle='-.',  linewidth = 2)
plt.plot(best9 , label='Best fitness'     ,  color='gold',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(best10 , label='Best fitness'     ,  color='gold',     marker='s', markersize='0', linestyle='-.',  linewidth = 2)

plt.plot(max1 , label='Max value'         ,  color='black',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(max2 , label='Max value'         ,  color='black',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(max3 , label='Max value'         ,  color='royalblue',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(max4 , label='Max value'         ,  color='royalblue',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(max5 , label='Max value'         ,  color='red',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(max6 , label='Max value'         ,  color='red',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(max7 , label='Max value'         ,  color='gray',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(max8 , label='Max value'         ,  color='gray',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(max9 , label='Max value'         ,  color='gold',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(max10 , label='Max value'         ,  color='gold',     marker='s', markersize='0', linestyle='--',  linewidth = 2)

plt.plot(min1 , label='Min value'         ,  color='black',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(min2 , label='Min value'         ,  color='black',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(min3 , label='Min value'         ,  color='royalblue',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(min4 , label='Min value'         ,  color='royalblue',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(min5 , label='Min value'         ,  color='red',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(min6 , label='Min value'         ,  color='red',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(min7 , label='Min value'         ,  color='gray',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(min8 , label='Min value'         ,  color='gray',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(min9 , label='Min value'         ,  color='gold',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(min10, label='Min value'         ,  color='gold',     marker='s', markersize='0', linestyle='--',  linewidth = 2)

plt.plot(avg1 , label='Average value'     ,  color='black',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(avg2 , label='Average value'     ,  color='black',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(avg3 , label='Average value'     ,  color='royalblue',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(avg4 , label='Average value'     ,  color='royalblue',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(avg5 , label='Average value'     ,  color='red',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(avg6 , label='Average value'     ,  color='red',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(avg7 , label='Average value'     ,  color='gray',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(avg8 , label='Average value'     ,  color='gray',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(avg9 , label='Average value'     ,  color='gold',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(avg10, label='Average value'     ,  color='gold',     marker='s', markersize='0', linestyle='--',  linewidth = 2)

plt.plot(std1 , label='Standart Deviation',  color='black',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(std2 , label='Standart Deviation',  color='black',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(std3 , label='Standart Deviation',  color='royalblue',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(std4 , label='Standart Deviation',  color='royalblue',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(std5 , label='Standart Deviation',  color='red',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(std6 , label='Standart Deviation',  color='red',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(std7 , label='Standart Deviation',  color='gray',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(std8 , label='Standart Deviation',  color='gray',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(std9 , label='Standart Deviation',  color='gold',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
plt.plot(std10 , label='Standart Deviation',  color='gold',     marker='s', markersize='0', linestyle='--',  linewidth = 2)
'''
