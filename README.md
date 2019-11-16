# Projet Python Open Data 2019 !

Ce repo GitHub sert de solution de versionning pour l'évaluation du projet.
Les deux élèves du projet sont : *Khouri Jérémy* et *Chenuet Laurent* E3FI ESIEE Paris. 

# Le projet

L’objectif du mini projet est de recueillir, d’analyser et de présenter des données publiques dans un secteur d’intérêt général tel que la météorologie, la santé publique, la démographie, la finance, l’économie, la politique, le sport, la culture, etc… 
Nous avons choisi le thème de la population mondiale en fonction des pays *([Liens du dataset](https://donnees.banquemondiale.org/indicateur/SP.POP.TOTL))*
Le résultat attendu est un histogramme de ces données et une représentation géolocalisée

## Histogramme

Chaque Pays possède son propre Histogramme.
![France](https://user-images.githubusercontent.com/39912632/68996442-4d1db600-089a-11ea-9000-2a7d5c2757fd.png)

## Représentation géolocalisée

{TEXTE ET IMAGE ICI}

## Comment faire fonctionner le programme sous Linux

**Afin de permettre une exécution du programme simple, ils vous suffit:**

 1. Posséder une machine Linux
 2. Cloner le [repo](https://github.com/jerkhouri/ESIEE-Python-Open-Data.git) sur votre répertoire de test

**Étapes par étapes :**
1. Installer python3  `sudo apt install python3`
2. Installer pip `sudo apt install python3-pip`
3. Installer les dépendances liés au projet `pip3 install -r requirement.txt` (dans le fichier racine)
4. Télécharger le fichier dataset `python3 python/downloadfile.py`
5. Génération des histogrammes `python3 python/histogen.py`

**En une commande :**

 1. Lancer le script qui fera tout à votre place `bash launch.sh`

**Vous pouvez retrouver tous les histogrammes généré dans le répertoire "HistoData/".**

## {MODIFICATION A VENIR}
{TEXTE ICI}
