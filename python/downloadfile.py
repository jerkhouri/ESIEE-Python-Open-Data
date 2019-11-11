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
	file_data= Path("data")
	if not file_data.exists():
		os.system('mkdir data')
		print('Creation du fichier "Data"')


	#TELECHARGEMENT DU FICHIER
	print('Debut du téléchargement du fichier avec urllib2...')
	url = 'http://api.worldbank.org/v2/fr/indicator/SP.POP.TOTL?downloadformat=csv'
	urllib.request.urlretrieve(url, 'data/data.zip')
	print('Téléchargment terminé')

	#DEZIPPAGE DU FICHIER
	# spécifiant le nom du fichier zip
	file = "data/data.zip"
	# ouvrir le fichier zip en mode lecture
	with ZipFile(file, 'r') as zip:
	    # extraire tous les fichiers
	    print('Extraction du zip...')
	    zip.extractall('')
	    print('Extraction terminé!')



	#SUPPRESSION DES FICHIERS INUTILES
	print('Suppression des fichiers inutiles')
	os.system('rm data/data.zip')
	os.system('rm Metadata_*')

	#RENOMMER FICHIER DATA
	print('Nom du fichier modifié en data.csv')
	os.system('mv API* data/data.csv')


def main():
    if testLink(): downloadDataFile()
    pass

if __name__ == '__main__':
    main()
