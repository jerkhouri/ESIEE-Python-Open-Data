#!/usr/bin/python3

#TELECHARGEMENT DU FICHIER
import urllib.request
print('Debut du téléchargement du fichier avec urllib2...')
url = 'http://api.worldbank.org/v2/fr/indicator/SP.POP.TOTL?downloadformat=csv'
urllib.request.urlretrieve(url, 'data/data.zip')
print('Téléchargment terminé')

#DEZIPPAGE DU FICHIER
from zipfile import ZipFile
# spécifiant le nom du fichier zip
file = "data/data.zip"
# ouvrir le fichier zip en mode lecture
with ZipFile(file, 'r') as zip:
    # extraire tous les fichiers
    print('Extraction du zip...')
    zip.extractall('')
    print('Extraction terminé!')



#SUPPRESSION DES FICHIERS INUTILES
import os
print('Suppression des fichiers inutiles')
os.system('rm data/data.zip')
os.system('rm Metadata_*')

#RENOMMER FICHIER DATA
print('Nom du fichier modifié en data.csv')
os.system('mv API* data/data.csv')
