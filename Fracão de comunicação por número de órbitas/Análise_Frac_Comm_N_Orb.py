import pandas as pd
import matplotlib.pyplot as plt
import csv

a = [50,75,100,125,150,175,200,225,250,275,300,325,350,375,400,425,450,475,500,525]
b = [0.01136078558,0.01060830506,0.01005268251,0.01000616426,0.01050078846,0.01029080483,0.01016924855,0.01046494959,0.01041480005,0.01021079725,0.01012448034,0.01012312052,0.01028061786,0.01015434606,0.01013345519,0.01014027735,0.01013443558,0.01013675375,0.01015317569,0.010092908]

c = [50,75,100,125,150,175,200,225,250,275,300,325,350,375,400,425,450,475,500,525]
d = [0.007203526503,0.006761599847,0.006576353797,0.006479636452,0.006773546137,0.006676223633,0.006621211171,0.006586387601,0.006723387785,0.006672531196,0.006594351794,0.006489603952,0.00659946037,0.00656748245,0.006589573279,0.006514232227,0.006598333891,0.006560407432,0.006526273537,0.00650560793]

e = [50,75,100,125,150,175,200,225,250,275,300,325,350,375,400,425,450,475,500,525]
f = [0.004945704763,0.005232474793,0.005124896964,0.004931404734,0.005208582214,0.005140282613,0.005223499476,0.005176725442,0.005311332994,0.005212914997,0.005142877622,0.005188374952,0.005252945182,0.005184689635,0.005084647054,0.005004785536,0.005041334162,0.00507403565,0.005035373048,0.004956003522]

fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(a, b, color='black',   marker='s',  label='30 degree inclination')
ax.scatter(c, d, color='red',     marker='o',  label='50 degree inclination')
ax.scatter(e, f, color='gold',    marker='^',  label='98 degree inclination')

plt.axhline(y=b[-1], color="black", linestyle="--")
plt.axhline(y=d[-1], color="red", linestyle="--")
plt.axhline(y=f[-1], color="gold", linestyle="--")

ax.set_title('Fraction of Communication by Orbits')
ax.set_xlabel('Number of Orbits')
ax.set_ylabel('Fraction of Communication [s/s]')

plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.25),
          ncol=3, fancybox=True, shadow=True)
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