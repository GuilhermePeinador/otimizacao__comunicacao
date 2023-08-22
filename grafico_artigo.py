# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:44:12 2023

@author: Damylle Donati
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


FractionComm 		= pd.read_csv('FracCom.csv')
Orbit		= (FractionComm['Orb'].values)
Frac	= (FractionComm['Frac Comunicacao'].values)

model30 = np.poly1d(np.polyfit(Orbit[:20], Frac[:20], 1))
polyline30 = np.linspace(50, 525, 20)
model50 = np.poly1d(np.polyfit(Orbit[21:40], Frac[21:40], 1))
polyline50 = np.linspace(75, 525, 19)
model98 = np.poly1d(np.polyfit(Orbit[41:], Frac[41:], 1))
polyline98 = np.linspace(75, 525, 19)
# fig, axs = plt.subplots(3)


# fig.set_figheight(20)
# fig.set_figwidth(15)
# fig.tight_layout(pad=6.0)

plt.figure(figsize=(10,6))

# plt.set_title("Parallel Configuration")
plt.plot(Orbit[:20] ,Frac[:20], color='black',marker='s',markersize='10',linestyle='-',label='30$^{\circ}$',linewidth = 0)
plt.plot(polyline30 ,model30(polyline30), color='black',marker='s',markersize='0',linestyle='--',label='30$^{\circ}$ - fit',linewidth = 2)
plt.plot(Orbit[21:40] ,Frac[21:40],color='red',marker='o',markersize='10',linestyle='-',label='50$^{\circ}$',linewidth = 0)
plt.plot(polyline50 ,model50(polyline50), color='red',marker='s',markersize='0',linestyle='--',label='50$^{\circ}$ - fit',linewidth = 2)
plt.plot(Orbit[41:] ,Frac[41:],color='royalblue',marker='^',markersize='10',linestyle='-',label='98$^{\circ}$',linewidth = 0)
plt.plot(polyline98 ,model98(polyline98), color='royalblue',marker='s',markersize='0',linestyle='--',label='98$^{\circ}$ - fit',linewidth = 2)


plt.ylabel('Fraction of Communication [s/s]',  labelpad=20)
plt.xlim([0,600])
plt.xticks([0,100,200,300,400,500,600])
plt.yticks([0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.01, 0.011, 0.012])
plt.ylim([0.0030, 0.0125])
plt.xlabel('Altitude [km]', labelpad=20)
plt.legend(bbox_to_anchor=(0.5, -0.20), ncol=3, loc='upper center')
plt.grid()

SIZE = 20
plt.rc('font', size=SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=15)    # legend fontsize
plt.rc('figure', titlesize=SIZE)
plt.rcParams["font.family"] = "arial"
plt.savefig('FractionCommunication.png', format='png', dpi=300)

plt.show()

# plt.set_title("Counterflow Configuration - Intern Channel Constriction")
# plt.plot(Rein_Estrang_Hot ,fAgulha_Estrang_Hot, color='black',marker='s',markersize='10',linestyle='-',label='Intern, Needle',linewidth = 0)
# plt.plot(Rein_Estrang_Hot ,fHaste_Estrang_Hot,color='black',marker='o',markersize='10',linestyle='--',label='Intern, Rod',linewidth = 0)
# plt.plot(Rein_Expand_Cold ,fAgulha_Expand_Cold,color='royalblue',marker='s',markersize='10',linestyle='-',label='Extern, Needle',linewidth = 0)
# plt.plot(Rein_Expand_Cold ,fHaste_Expand_Cold,color='royalblue',marker='o',markersize='10',linestyle='--',label='Extern, Rod',linewidth = 0)

# plt.set_xlabel('${Re}_{in}$')
# plt.set_xlim([1000,16000])
# plt.set_ylim([0, 1.0])
# plt.set_ylabel('f')
# plt.legend(bbox_to_anchor=(0.5, -0.20), ncol=4, loc='upper center')
# plt.grid()

# SIZE = 20
# plt.rc('font', size=SIZE)          # controls default text sizes
# plt.rc('axes', titlesize=SIZE)     # fontsize of the axes title
# plt.rc('axes', labelsize=SIZE)    # fontsize of the x and y labels
# plt.rc('xtick', labelsize=SIZE)    # fontsize of the tick labels
# plt.rc('ytick', labelsize=SIZE)    # fontsize of the tick labels
# plt.rc('legend', fontsize=15)    # legend fontsize
# plt.rc('figure', titlesize=SIZE)
# plt.rcParams["font.family"] = "arial"
# plt.savefig('GenerationXFit.png', format='png', dpi=300)

# plt.show()