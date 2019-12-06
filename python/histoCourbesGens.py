import pandas as pd
import matplotlib.pyplot as plt
import os, math, sys, time
from pathlib import Path

def CreateHistoFile():
    file_path=("data/HistoCourbes")
    file_data= Path(file_path)
    if not file_data.exists():
        os.makedirs(file_path)
        print('Creation du repertoire "'+file_path+'"')


def GenHistoData(pays):
    data = pd.read_csv('data/data.csv', skiprows=5,sep=',')

    data_pays = data[data['Country Name']==pays]

    valueAnnee = [] 								# X -> Déclaration de la liste des années
    valuePop = data_pays.iloc[0,4::].tolist() 		# Y -> Déclaration de la liste des données de population
    compteur=0 										# Comme son nom l'indique c'est un compteur

    for col in data.columns: #Grace à cette boucle on recupère les années du csv sous forme de liste
        compteur+=1
        if compteur>=5:
            valueAnnee.append(col) #On ajoute l'année à la liste valueAnnee

    # On supprime les 2 derniers elements de chaque liste qui sont des erreurs
    del valueAnnee[-2]
    del valueAnnee[-1]
    del valuePop[-1]
    del valuePop[-1]

    # On s'assure que chaque liste ne contient que des INT
    for i in range(0, len(valueAnnee)):
        valueAnnee[i] = int(valueAnnee[i])
        if(math.isnan(valuePop[i])):
            valuePop[i] = None
        else:
            valuePop[i] = int(valuePop[i]) / 1000000

    # Création de l'histogramme
    #plt.bar(valueAnnee,valuePop, color = 'red', align='center', width=0.7)
    plt.plot(valueAnnee,valuePop, color = 'red', linestyle = 'dashed', linewidth = 2,
      markerfacecolor = 'blue', markersize = 5)
    plt.xlabel('Années')
    plt.ylabel('Population en Million')
    plt.title('Evolution de la Population en '+ pays)
    plt.savefig('data/HistoCourbes/'+pays+'.png') #Sauvegarde de l'histogramme dans le fichier HistoData + le nom du pays
    #Fermeture de l'histogramme
    plt.close()
    plt.clf()
    plt.cla()


def listpays():
    data = pd.read_csv('data/data.csv', skiprows=5,sep=',')
    return data['Country Name'].tolist()

def progressbar(i):
    sys.stdout.write("\r[%.2f" %i + "%]" + "=" * (int)(i)+ ">")


def main():
    i = 0.0 							#Pourcentage pour barre de progression
    CreateHistoFile() 					#Création du dossier pour les histogrammes
    nb_pays =  100 / len(listpays())	#Evaluation du nombre de pays à traité

    print("Génération des histocourbes en cours")
    for pays in listpays():
        GenHistoData(pays)
        i+=nb_pays
        progressbar(i)
    print("\nTous les pays ont été générés")
    pass

if __name__ == '__main__':
    main()
