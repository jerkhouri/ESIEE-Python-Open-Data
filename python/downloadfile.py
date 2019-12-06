#Programmes qui télécharge le dataset et le geojson dynamiquement

#Importation des librairies
from zipfile import ZipFile
import os, urllib.request, shutil
from pathlib import Path

def downloadDataFile():
    #Creation du dossier s'il n'existe pas
    file_path=("data")
    file_data= Path(file_path)
    if not file_data.exists():
         os.makedirs(file_path)

    file_path_csv=("data/data.csv")
    file_data_csv= Path(file_path_csv)    
    if not file_data_csv.exists():
        #TELECHARGEMENT DU FICHIER
        urlCSV = 'http://api.worldbank.org/v2/fr/indicator/SP.POP.TOTL?downloadformat=csv'
        urllib.request.urlretrieve(urlCSV, 'data/dataCSV.zip')    
        print('Téléchargment du csv terminé')

        #DEZIPPAGE DU FICHIER
        # spécifiant le nom du fichier zip
        fileCSV = "data/dataCSV.zip"    
    
        # ouvrir le fichier zip en mode lecture
        with ZipFile(fileCSV, 'r') as zip:
            # extraire tous les fichiers
            zip.extractall('')
 
        #SUPPRESSION DES FICHIERS INUTILES
        os.remove('data/dataCSV.zip') 
    
        l = os.listdir()
        for i in l:
            if "Metadata_" in i : os.remove(i) 

        #RENOMMER FICHIER DATA
        l = os.listdir()
        for i in l:
            if "API" in i : os.rename(i, "data/data.csv")


    file_path_json=("data/data.json")
    file_data_json= Path(file_path_json)
    if not file_data_json.exists():
        #TELECHARGEMENT DU FICHIER
        urlJSON = 'https://github.com/johan/world.geo.json/archive/master.zip'
        urllib.request.urlretrieve(urlJSON, 'data/dataJSON.zip')    
        print('Téléchargment du json terminé')

        #DEZIPPAGE DU FICHIER
        # spécifiant le nom du fichier zip
        fileJSON = "data/dataJSON.zip"   
    
        # ouvrir le fichier zip en mode lecture
        with ZipFile(fileJSON, 'r') as zip:
            # extraire tous les fichiers
            zip.extract('world.geo.json-master/countries.geo.json')

        #RENOMMER FICHIER DATA
        os.rename('world.geo.json-master/countries.geo.json', 'data/data.json')
                
        #SUPPRESSION DES FICHIERS INUTILES
        os.remove('data/dataJSON.zip')
        shutil.rmtree('world.geo.json-master', ignore_errors=True)

    return 1

def editFile(): #on modifie le debut du fichier pour ajouter le séparateur ","
    line_to_replace = 0 #La ligne à remplacer
    my_file = 'data/data.csv' #Path du fichier

    with open(my_file, 'r') as file: 
        lines = file.readlines() 
    
    if len(lines) > int(line_to_replace):
        lines[line_to_replace] = 'Sep=,\r'+lines[0] #On remplace la ligne

    with open(my_file, 'w') as file:
        file.writelines( lines ) #Applique les modifs

def maindownloadFile():
    print("---------------------------------------")
    print("Programme de téléchargement des données")
    
    downloadDataFile()
    editFile()

    print("---------------------------------------")
    pass

if __name__ == '__main__':    
    maindownloadFile()
