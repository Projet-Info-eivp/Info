# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 14:55:06 2020

@author: Anthony Vaïtilingom
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fichier = pd.read_csv("donnee_projet_info.csv", sep=";", index_col = 'sent_at', parse_dates = True)
# print(fichier)


capt_1 = fichier[fichier['id']==1]
capt_2 = fichier[fichier['id']==2]
capt_3 = fichier[fichier['id']==3]
capt_4 = fichier[fichier['id']==4]
capt_5 = fichier[fichier['id']==5]
capt_6 = fichier[fichier['id']==6]

"""Sujet Groue B: calcul des similarrités entre les données"""

def min1(a,b,c):#fonction retournant le minimum entre 3 valeurs
    if a>b:
        if b>c:
            return c
        else :
            return b
    else :
        if a>c:
            return c
        else :
            return b

def DistanceTimeWarping (U,V):
    n=len(U)
    m=len(V)
    D=np.zeros((n,m))
    D[0,0]=np.abs(U[0]-V[0])
    for j in range (1,m): #initialisation 1ère ligne
        D[0,j]=np.abs(U[0]-V[j])+D[0,j-1]
    for i in range (1,n): #initialisation 1ère colonne
        D[i,0]=np.abs(U[i]-V[0])+D[i-1,0]
    for i in range (1,n): #remplissage du reste de la matrice
        for j in range (1,m):
            D[i,j]=np.abs(U[i]-V[j])+min1(D[i-1,j-1],D[i-1,j],D[i,j-1])
    L=[]
    i=n-1
    j=m-1
    while (i>0) and (j>0):
        if i==0:
            j=j-1
        elif j==0:
            i=i-1
        else :
            if D[i-1,j]==np.min((D[i-1,j],D[i,j-1],D[i-1,j-1])):
                i=i-1
            elif D[i,j-1]==np.min((D[i-1,j],D[i,j-1],D[i-1,j-1])):
                j=j-1
            else :
                i=i-1
                j=j-1
        L.append([i,j])
    x=[]
    y=[]
    List=[]
    for i in range(len(L)):
        x.append(L[i][0])#liste des coordonnées des vecteurs de U
        y.append(L[i][1])#liste des coordonnées des vecteurs de V
    for i in range(len(x)):
        List.append(np.abs(U[x[i]]-V[y[i]]))#liste des distances entre les vecteurs
    return (L,List)

def Norme(Vecteur):#normalise un vecteur
    s=0
    U=[]
    for i in range(len(Vecteur)):
        s+=Vecteur[i]**2
    s=np.sqrt(s)
    for i in range(len(Vecteur)):
        U.append(Vecteur[i]/s)
    return U




Z=capt_2['temp']
W=capt_1['temp']
plt.plot(Z)
plt.plot(W)
plt.xticks(rotation=40)
plt.title("Courbes des températures des capteurs 1 et 2")



g=plt.figure()
Dist=DistanceTimeWarping(W,Z)[1]
Q=[]
for i in range(len(Norme(Dist))):
    Q.append(1-Norme(Dist)[i])
b=[k for k in range(len(Norme(Dist)))]
plt.plot(b,Q)# affiche les distances normalisées entre W et Z
plt.title('Graphiques des similarités entre les données\n des températures des capteurs 1 et 2')

