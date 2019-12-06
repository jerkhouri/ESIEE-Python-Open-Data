import pandas as pd
import matplotlib.pyplot as plt
import os, math, sys, time, numpy
from pathlib import Path

def CreateHistoFile():
    file_path=("data/HistoGrammes")
    file_data = Path(file_path)
    if not file_data.exists():
        os.makedirs(file_path)        
        print('Creation du repertoire '+file_path)
    return 1
    
def OpenCSV(): #Permet de gerer les erreurs utilisateurs
    return pd.read_csv('data/data.csv', skiprows=5,sep=',')

def GetRangeyear(data): #Permet de gerer les erreurs utilisateurs
    valueAnnee = [] 
    compteur=0
    for col in data.columns: #Grace à cette boucle on recupère les années du csv sous forme de liste
        compteur+=1
        if compteur>=5:
            valueAnnee.append(col)

    del valueAnnee[-2]
    del valueAnnee[-1]

    MaxYear = max(valueAnnee)
    MinYear = min(valueAnnee)
    returnList=[MinYear,MaxYear]
    return returnList

def GenHistoData(data, annee, min_data ,max_data):    
    data_column = data[annee].tolist()                    #Liste des populations par années
    data_column = [i/1000000 for i in data_column]        #On Mets les valeurs en millions
    data_countrycode = data['Country Code']                #On recupère la liste des pays du csv
    
    GoodList = ['ABW', 'AFG', 'AGO', 'ALB', 'AND', 'ARE', 'ARG', 'ARM', 'ASM', 'ATG', 'AUS', 'AUT', 'AZE', 'BDI', 'BEL', 'BEN', 'BFA', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH', 'BLR', 'BLZ', 'BMU', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN', 'BWA', 'CAF', 'CAN', 'CHE', 'CHL', 'CHN', 'CIV', 'CMR', 'COD', 'COG', 'COL', 'COM', 'CPV', 'CRI', 'CUB', 'CUW', 'CYM', 'CYP', 'CZE', 'DEU', 'DJI', 'DMA', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ERI', 'ESP', 'EST', 'ETH', 'FIN', 'FJI', 'FRA', 'FRO', 'FSM', 'GAB', 'GBR', 'GEO', 'GHA', 'GIB', 'GIN', 'GMB', 'GNB', 'GNQ', 'GRC', 'GRD', 'GRL', 'GTM', 'GUM', 'GUY', 'HKG', 'HND', 'HRV', 'HTI', 'HUN', 'IDN', 'IMN', 'IND', 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ', 'KHM', 'KIR', 'KNA', 'KOR', 'KWT', 'LAO', 'LBN', 'LBR', 'LBY', 'LCA', 'LIE', 'LKA', 'LSO', 'LTU', 'LUX', 'LVA', 'MAC', 'MAF', 'MAR', 'MCO', 'MDA', 'MDG', 'MDV', 'MEX', 'MHL', 'MKD', 'MLI', 'MLT', 'MMR', 'MNE', 'MNG', 'MNP', 'MOZ', 'MRT', 'MUS', 'MWI', 'MYS', 'NAM', 'NCL', 'NER', 'NGA', 'NIC', 'NLD', 'NOR', 'NPL', 'NRU', 'NZL', 'OMN', 'PAK', 'PAN', 'PER', 'PHL', 'PLW', 'PNG', 'POL', 'PRI', 'PRK', 'PRT', 'PRY', 'PSE', 'PYF', 'QAT', 'ROU', 'RUS', 'RWA', 'SAU', 'SDN', 'SEN', 'SGP', 'SLB', 'SLE', 'SLV', 'SMR', 'SOM', 'SRB', 'SSD', 'STP', 'SUR', 'SVK', 'SVN', 'SWE', 'SWZ', 'SXM', 'SYC', 'SYR', 'TCA', 'TCD', 'TGO', 'THA', 'TJK', 'TKM', 'TLS', 'TON', 'TTO', 'TUN', 'TUR', 'TUV', 'TZA', 'UGA', 'UKR', 'URY', 'USA', 'UZB', 'VCT', 'VEN', 'VGB', 'VIR', 'VNM', 'VUT', 'WSM', 'YEM', 'ZAF', 'ZMB', 'ZWE']
    
    EndList = []             #Liste final
    
    compteur =0                #Compteur pour la boucle suivante
    for data in data_column:            
        if (data_countrycode[compteur] in GoodList) and data<max_data and data>min_data:    #On recupère les bon pays avec le bon range        
            EndList.append(data) #on l'ajoute à la liste
        compteur +=1    
    
    max_pop = 0     #Variable pour recuperer la valeur la plus grande
    for i in range(0,len(EndList)):
        EndList[i]=numpy.nan_to_num(EndList[i])
        EndList[i]=int(EndList[i])                    #on converti toutes les données en INT pour enelver la virgule
        if EndList[i] > max_pop:        
            max_pop = EndList[i]        #On ecrase par la valeur la plus grande 
        
    
    if(len(EndList) == 0):
        print('Aucune Information pour cette range')
        return 0
    
    # Création de l'histogramme
    plt.hist(EndList, bins = len(EndList) , color = 'red', edgecolor = 'red')
    plt.xlabel('Population en Million')
    plt.ylabel('Nombre de Pays')
    plt.title('Nombre de pays par échelle de Population en '+ annee +'\nde '+ str(min_data)+' à '+ str(max_pop)+' Millions d\'habitants')
    plt.savefig('data/HistoGrammes/'+ annee +' de '+ str(min_data)+' à '+ str(max_pop)+' Millions d\'habitants.png') #Sauvegarde de l'histogramme dans le fichier HistoData + le nom du pays

    return 1


def verifAnnee(data, Année):
    MinYear = int(GetRangeyear(data)[0])
    MaxYear = int(GetRangeyear(data)[1])
    
    if (len(Année) < 4 or len(Année) > 4 or not Année.isdigit()):
        print("L'année n'est pas valide.")
        return 0
    elif(int(Année)<MinYear or int(Année)>MaxYear):
        print("Nous n'avons pas de donnée pour l'année "+ Année)
        return 0
    else:
        return 1

def verifRange(Range):    
    Range_Min = 0
    Range_Max = 100000
    if (len(Range) != 0):            
        if('-' not in Range):
            print("Merci de rentrer une range valide (ex: 0-200 en Millions)")
            return 0
        else:
            Range = Range.split('-')
            if (Range[0].isdigit() and Range[1].isdigit()):
                Range_Min = int(Range[0])    
                Range_Max = int(Range[1])                
                return [Range_Min,Range_Max]    
            else:
                print("Merci de rentrer une range valide (ex: 0-200 en Millions)")
                return 0
    else:            
        return [Range_Min,Range_Max]

def mainhistoGrammesGen():    
    print("Programme de Géneration d'Histogrammes")
    
    data = OpenCSV() #Ouverture du fichier CSV 1 seule fois.

    #Requetes utilisateurs avec filtres anti-crash
    if(len(sys.argv)==1):
        Année = input('Quelle année souhaitez vous obtenir ? ')        
        if(verifAnnee(data, Année)):
            Range = input('Quelle est le champs de population souhaitez ? (ex: 10-200 en Millions )')
            if(verifRange(Range)!=0):
                Range_Min = verifRange(Range)[0]
                Range_Max = verifRange(Range)[1]
            else:
                return 0
        else:
            return 0
        
    if(len(sys.argv)>=2): #VERIFIER SI ARG[1] EST UN INT
        Année = sys.argv[1]
        if(verifAnnee(data, Année)):
            if(len(sys.argv)>=3):
                Range = sys.argv[2]
                if(verifRange(Range)!=0):
                    Range_Min = verifRange(Range)[0]
                    Range_Max = verifRange(Range)[1]
                else:
                    return 0

                if(len(sys.argv)>=4):
                    print("Le programme de génération d'histogramme ne prend que 2 arguments (histoGrammesGen.py 1998 0-1000)")
                    return 0

            else:
                Range = input('Quelle est le champs de population souhaitez ? (ex: 10-200 en Millions )')
                if(verifRange(Range)!=0):
                    Range_Min = verifRange(Range)[0]
                    Range_Max = verifRange(Range)[1]
                else:
                    return 0
        else:
            return 0

    
    if Range_Min>Range_Max:
        print("La range Maximale ne peut pas être plus petite que la Minimale, merci d'écrire une range valide.")
        return 1


    print('Année choisie = ' + str(Année))
    print('Range choisie = ' + str(Range_Min) + ' à ' + str(Range_Max))    
    

    CreateHistoFile()                     #Création du dossier pour les histogrammes
    if (GenHistoData(data, Année, Range_Min,Range_Max)):
        print("L'histogramme à bien été généré.")
    else:
        print("Erreur lors de la création de l'histogramme.")
    
    print("---------------------------------------")
    pass

if __name__ == '__main__':
    mainhistoGrammesGen()
