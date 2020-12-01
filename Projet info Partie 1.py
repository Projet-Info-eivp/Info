

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr as pr

fichier = pd.read_csv("donnee_projet_info.csv", sep=";", index_col = 'sent_at', parse_dates = True)
# print(fichier)


capt_1 = fichier[fichier['id']==1]
capt_2 = fichier[fichier['id']==2]
capt_3 = fichier[fichier['id']==3]
capt_4 = fichier[fichier['id']==4]
capt_5 = fichier[fichier['id']==5]
capt_6 = fichier[fichier['id']==6]

"""1-Affichage courbe avec intervalle de temps
et ajout des Valeurs statistiques"""

capt_1_temp = capt_1['temp']#on sélectinne les températures du capteur 1
f = plt.figure()
ax = f.add_subplot(111)
min=np.min(capt_1_temp)#minimum
max=np.max(capt_1_temp)#max
var=round(np.var(capt_1_temp),2)#variance
mediane=round(np.median(capt_1_temp),2)#mediane
m=round(np.mean(capt_1_temp),2)#moyenne arrondie au centième
e=round(np.std(capt_1_temp),2)#écart type
plt.subplot(1,2,1)
plt.plot(capt_1['temp']['2019-08-11 09:03':'2019-08-12 12:48'],color='red',marker='+')
plt.xticks(rotation=40)#rotation de la légende abscice
plt.text(0.2,0.9,'min='+str(min),horizontalalignment='center',verticalalignment='center', transform = ax.transAxes)
plt.text(0.2,0.85,'max='+str(max),horizontalalignment='center',verticalalignment='center', transform = ax.transAxes)
plt.text(0.2,0.8,'moyenne='+str(m),horizontalalignment='center',verticalalignment='center', transform = ax.transAxes)
plt.text(0.2,0.75,'ecart-type='+str(e),horizontalalignment='center',verticalalignment='center', transform = ax.transAxes)
plt.text(0.2,0.7,'variance='+str(var),horizontalalignment='center',verticalalignment='center', transform = ax.transAxes)
plt.text(0.2,0.65,'mediane='+str(mediane),horizontalalignment='center',verticalalignment='center', transform = ax.transAxes)
plt.title('Relevé de températures \n pour le capteur 1 entre\n le 11/8 9:03 et le 12/8 12:48')

"""2-Indice de corrélation d un couple de variable"""

def indice_correlation (X,Y):#X et Y sont de même dimension
    n=len(X)
    Xb=0
    Yb=0
    for k in range (n):
        Xb+=X[k]
        Yb+=Y[k]
    Xb=Xb/n
    Yb=Yb/n
    SigmaX=0
    SigmaY=0
    SigmaXY=0
    for k in range (n):
        SigmaX+=(X[k]-Xb)**2
        SigmaY+=(Y[k]-Yb)**2
        SigmaXY+=(X[k]-Xb)*(Y[k]-Yb)
    SigmaX=np.sqrt(SigmaX/n)
    SigmaY=np.sqrt(SigmaY/n)
    SigmaXY=SigmaXY/n
    R=SigmaXY/(SigmaX*SigmaY)
    return R

capt_2= fichier[fichier['id']==2]
capt_2_temp=capt_2['temp']
X=capt_1_temp
Y=capt_2_temp
indc=indice_correlation(X,Y)
print(indc)# indice de correlation pour température et humidité
print(pr(X,Y))#affiche indice de correlation de pearson(on utilise la fonction
# déja programmée) afin de vérifier si la formule est juste => c'est le cas!

# affichage des 2 courbes et de l'indice de correlation

plt.subplot(1,2,2)
plt.style.use('grayscale')
plt.plot(capt_1['temp']['2019-08-11 09:03':'2019-08-12 12:48'],color='red',marker='+')
plt.plot(capt_2['temp']['2019-08-11 09:03':'2019-08-12 12:48'],color='blue',marker='+')
plt.text(0.85,0.9,'indice de\n correlation='+str(round(indc,2)),horizontalalignment='center',verticalalignment='center',transform=ax.transAxes)
plt.xticks(rotation=40)
plt.title('Relevés de température\n pour capteurs 1 et 2 entre\n le 11/8 9:03 et le 12/8 12:48')

"""3-Calcul d'humidex"""
capt_1_humidité = capt_1['humidity']

def fonctionalpha (t,h):
    return ((17.27*t)/(237.7+t)+np.log(h))

def trosee(t,h):
    return ((237.7*fonctionalpha(t,h))/(17.27-fonctionalpha(t,h)))

def calcul_de_l_humidex (temperature,humidity): #Listes de la température et de l'humidité
    humidex=[]
    for k in range (len(temperature)):
        hum=temperature[k]+0.5555*(6.11*np.exp(5417.7530*((1/273.16)-(1/273+trosee(temperature[k],humidity[k]))))-10)
        humidex.append(hum)
    return humidex

humidex=calcul_de_l_humidex(capt_1_temp,capt_1_humidité)
print(humidex)
a=[k for k in range(len(humidex))]
plt.plot(a,humidex,color='green')
plt.title("graphique de l'humidex du capteur 1")


