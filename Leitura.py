import numpy as np
import pandas as pd
import os, sys
import matplotlib.pyplot as plt

def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

df = pd.read_csv(resource_path("Sim1/Simulação teste.txt"), sep=' ', engine='python', on_bad_lines='skip')

Teste   = df.iloc[:,5]
Fitness = df.iloc[:,11]

df.plot.scatter('Inc', 'Fit')
plt.show()