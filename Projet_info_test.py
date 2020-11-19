# -*- coding: utf-8 -*-



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Mesurer les similarités des capteurs pour chaque dimension, qu’en concluez-vous ? Proposez et
# implémentez un algorithme permettant de mesurer la similarité automatiquement et de la
# montrer sur les courbes.
# Bonus : Trouvez automatiquement les périodes horaires d’occupations des bureaux

info=pd.read_csv("donnee_projet_info.csv",sep=";",header=0,index_col=0)
# print(info.shape)#donne la taille du tableau
# print(info.id==1)



enregistrement_total=info.loc[:,"sent_at"].to_numpy()#convertit les enregistrements (type serie) en tableaux numpy
# print(len(enregistrement_total))
L=[]
for i in range(len(enregistrement_total)):
    [date,time]=enregistrement_total[i].split()#sépare la date de l'heure(ici seulement pour le premier enregistrement)
    [heure,fuseau]=time.split('+')
    L.append([date,heure,fuseau])
# print(L)

enregistrement=pd.DataFrame(L,index=[i for i in range(len(L))],columns=['date','heure','fuseau'])
# print(enregistrement)
# print(date,heure,fuseau)

info2=info.copy()#créer un copie du dataframe original
del info2['sent_at']
info3=pd.concat([info2,enregistrement],axis=1)#concaténation du nouveau tableau avec les dates, heures, fuseau séparés
del info3['fuseau']#on a pas besoin de la colonne "fuseau"...
print(info3)
# info_df=pd.DataFrame(info3,columns=['','capteurs','Bruit','temperature','humidite','lum','CO2','date','heure','fuseau'])
# print(info_df)

"""Désormais on travaille avec ce nouveau tableau(DataFrame)"""

capteur1=info3[info3["id"]==1]
capteur2=info3[info3["id"]==2]
capteur3=info3[info3["id"]==3]
capteur4=info3[info3["id"]==4]
capteur5=info3[info3["id"]==5]
capteur6=info3[info3["id"]==6]#sélectionne les données pour chaque capteur
# print(type(capteur2))
# print(capteur3.loc[:,"temp"])#sélect données de températures du capteur 3
#print(capteur4.loc[:,"noise"])
# X=pd.concat(capteur3["temp"],capteur4["temp"])
# print(X)
# LCapteurs=np.array[capteur1,capteur2,capteur3,capteur4,capteur5,capteur6]
# print(capteur1.loc[:,"temp"])
# print(capteur2.loc[:,"temp"].shape)
# print(capteur3.loc[:,"temp"].shape)
# print(capteur4.loc[:,"temp"].shape)
# print(capteur5.loc[:,"temp"].shape)
# print(capteur6.loc[:,"temp"].shape)

# essai=capteur3[(capteur3["temp"]==25) & (capteur3["noise"]==40)]
# print(essai)# sélectionne les ddonnées du capteur 3 où temp=25°C

# print(capteur2.loc[:,["temp","sent_at"]])# capteur2 bruit et enregistrement


# L=list([k for k in range(len(capteur2))])
# capteur2.reindex(L)
# print(capteur2)





# group=capteur2.groupby(["date"])

# x=pd.concat([capteur1,capteur3],axis=1)
# x1=pd.merge(capteur1)
# print(x)
# print(x.groupby(["temp"]).count())# compte le nombre de mesures effectuées chaque jour pour chaque

"""calcul de distance"""

X=[i for i in range (6)]#[0,1,2,3,4,5]
Y=[1,66,8,9,7,5]
# df1 = pd.DataFrame({'x': [1, 2, 3], 'y': ['a', 'b', 'c']})
# df2 = pd.DataFrame({'y': ['b', 'c', 'd'], 'z': [4, 5, 6]})
Xf=pd.DataFrame(X)
Yf=pd.DataFrame(Y)
print(len(Xf & Yf))

J=pd.merge(Xf,Yf,how='inner')
print(len(J))

def distance(vect1,vect2):
    dim1=len(vect1)
    dim2=len(vect2)
    if dim1==dim2:
        d=0
        for i in range (dim1):
                d+=(vect2[i]-vect1[i])**2
        D=np.sqrt(d)/(len(vect1)+len(vect2))
    else:
        Vf1=pd.DataFrame(vect1)
        Vf2=pd.DataFrame(vect2)
        J=pd.merge(Vf1,Vf2,how='inner')
        D=len(J)/(len(Vf1)+len(Vf2)-len(J))
    return(D)

print(distance(X,Y))
        
    

