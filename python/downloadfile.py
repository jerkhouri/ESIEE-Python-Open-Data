#!/usr/bin/python3

#Importation des librairies
from zipfile import ZipFile
import os, urllib.request
from pathlib import Path

def testLink():
	#TEST DU LIEN
	ShortUrl = 'api.worldbank.org'
	print('Test host : ' + ShortUrl)
	response = os.system("sudo ping -c 1 " + ShortUrl)
	if response == 256:
		print("Host OK")
		return True
	else:
		print("api.worldbank.org is unreachable")
		return False
	#ELSE continuer l'execution du programme


def downloadDataFile():
	#Creation du dossier s'il n'existe pas
	file_path=("data")
	file_data= Path(file_path)
	if not file_data.exists():
		os.system('mkdir '+file_path)
		print('Creation du fichier "'+file_path+'"')


	#TELECHARGEMENT DU FICHIER
	url = 'http://api.worldbank.org/v2/fr/indicator/SP.POP.TOTL?downloadformat=csv'
	urllib.request.urlretrieve(url, 'data/data.zip')
	print('Téléchargment du fichier terminé')

	#DEZIPPAGE DU FICHIER
	# spécifiant le nom du fichier zip
	file = "data/data.zip"
	# ouvrir le fichier zip en mode lecture
	with ZipFile(file, 'r') as zip:
	    # extraire tous les fichiers
	    zip.extractall('')
	    print('Extraction du zip terminé!')



	#SUPPRESSION DES FICHIERS INUTILES	
	os.system('rm data/data.zip')
	os.system('rm Metadata_*')
	print('Fichiers inutiles supprimés')

	#RENOMMER FICHIER DATA
	os.system('mv API* data/data.csv')	
	print('Nom du fichier modifié en data.csv')

def editFile(): #on modifie le debut du fichier pour ajouter le séparateur ","
	line_to_replace = 0 #La ligne à remplacer
	my_file = 'data/data.csv' #Path du fichier

	with open(my_file, 'r') as file: 
	    lines = file.readlines() 
	
	if len(lines) > int(line_to_replace):
	    lines[line_to_replace] = 'Sep=,\r'+lines[0] #On remplace la ligne

	with open(my_file, 'w') as file:
	    file.writelines( lines ) #Applique les modifs
	
	print('Ajout de "Sep=," au debut de data.csv')

def main():
	if testLink():
		downloadDataFile()
		editFile()
	pass

if __name__ == '__main__':
    main()
