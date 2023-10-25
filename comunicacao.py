"""
    Universidade Federal de Santa Catarina
    Laboratory of Applications and Research in Space - LARS
    Orbital Mechanics Division
    Título do Algoritmo = Código de cálculo de comunicação
    Autor= Guilherme Peinador Gomes
    Versão = 0.1.0
    Data = 13/06/2023
"""

import numpy as np
import pandas as pd
import os, sys
from tqdm import tqdm
'''
Coordenadas Antena INPE Natal
Latitude: -5.871778
Longitude: -35.206864
'''

def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
df = pd.read_csv(resource_path("results\ECEF_R.csv"), sep=',', engine='python', on_bad_lines='skip')

#posicao_gs = [R_E * np.cos(lat_gs) * np.cos(long_gs), R_E * np.cos(lat_gs) * np.sin(long_gs), R_E * np.sin(lat_gs)]

#df=dataframe

#todo def

def calculacomunicacao(df, lat_gs, long_gs):
    """

    :param df = DataFrame de rx, ry e rz do CubeSat
    :param lat_gs = Latitude da Groundd Station em Graus (Norte)
    :param long_gs = Longitude da Groundd Station em Graus (Leste)

    """
    for i in range(df[df.columns[0]].count()):

        R_E = 6371.00  # raio da Terra em km

        VetorTerraEstacao = np.array([R_E * np.cos(lat_gs) * np.cos(long_gs), R_E * np.cos(lat_gs) * np.sin(long_gs), R_E * np.sin(lat_gs)])

        VetorSatelite = np.array([df.iloc[i, df.columns.get_loc('rx')], df.iloc[i, df.columns.get_loc('ry')], df.iloc[i, df.columns.get_loc('rz')]])

        VetorSateliteEstacao = VetorSatelite - VetorTerraEstacao

        # Critério de Comunicação
        AComunicacao = np.pi \
                       - np.arccos((np.dot(VetorSatelite, VetorSateliteEstacao)) / (np.linalg.norm(VetorSatelite) * np.linalg.norm(VetorSateliteEstacao))) \
                       - np.arccos((np.dot(VetorTerraEstacao, VetorSatelite)) / (np.linalg.norm(VetorTerraEstacao) * np.linalg.norm(VetorSatelite)))

        df6 = pd.DataFrame(AComunicacao, columns=['Ângulo de Comunicação'])
        df = pd.concat([df, df6], axis=1)
        df["end"] = None
        df.to_csv("Tempo de comunicação.csv", sep=',')
        print (df)
        return df

'''
def calculacomunicacao(df):
    Contato = []
    for i in range (df[df.columns[0]].count()):
        lat_gs = np.radians(-5.871778)
        long_gs = np.radians(-35.206864)
        R_E = 6371.00  # raio da Terra em km

        VetorTerraEstacao = np.array([R_E * np.cos(lat_gs) * np.cos(long_gs), R_E * np.cos(lat_gs) * np.sin(long_gs), R_E * np.sin(lat_gs)])
        VetorSatelite = np.array([df.iloc[i, df.columns.get_loc('rx')], df.iloc[i, df.columns.get_loc('ry')], df.iloc[i, df.columns.get_loc('rz')]])

        VetorSateliteEstacao = VetorSatelite - VetorTerraEstacao

        #Critério de Comunicação
        AComunicacao = np.pi \
                - np.arccos((np.dot(VetorSatelite,VetorSateliteEstacao))/(np.linalg.norm(VetorSatelite)*np.linalg.norm(VetorSateliteEstacao))) \
                - np.arccos((np.dot(VetorTerraEstacao,VetorSatelite))/(np.linalg.norm(VetorTerraEstacao)*np.linalg.norm(VetorSatelite)))


        if AComunicacao >= np.radians(105): #90 graus (horizonte) + 15 (elevação)
            Contato.append(1)
            #print("1") #Tem comunicação
        else:
            Contato.append(0)
            #print("0") # não tem comunicação

    df6 = pd.DataFrame(Contato, columns=['Contato'])
    df = pd.concat([df,df6], axis=1)
    df["end"] = None
    df.to_csv("Tempo de comunicação.csv", sep=',')
    #print (df)
    return df
'''