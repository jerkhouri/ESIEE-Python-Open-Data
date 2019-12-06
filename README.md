
# Projet Python Open Data 2019 !

Ce repo GitHub sert de solution de versionning pour l'évaluation du projet.
Les deux élèves du projet sont : *Khouri Jérémy* et *Chenuet Laurent* E3FI ESIEE Paris. 

# Le projet

L’objectif du mini projet est de recueillir, d’analyser et de présenter des données publiques dans un secteur d’intérêt général tel que la météorologie, la santé publique, la démographie, la finance, l’économie, la politique, le sport, la culture, etc… 
Nous avons choisi le thème de la population mondiale en fonction des pays *([Liens du dataset](https://donnees.banquemondiale.org/indicateur/SP.POP.TOTL))*
Le résultat attendu est un histogramme de ces données et une représentation géolocalisée

## Histogramme

Un histogramme possède différentes caractéristiques :

 - L'année des données 
 - La tranche de population 
 
 ![2018 de 1 à 69M](https://user-images.githubusercontent.com/39912632/70306664-ba709700-1807-11ea-99a1-62b3129fceab.png)
## Représentation géolocalisée

Chaque carte représente une année. (celle-ci l'année 2018)
Elles sont dynamiques et permettent ainsi d'agrandir (zoom) les différents pays.

![Map 2018](https://user-images.githubusercontent.com/39912632/70307018-8649a600-1808-11ea-9a78-20dc224a2b4a.png)

## Comment faire fonctionner le programme.

**Afin de permettre une exécution du programme simple, ils vous suffit de suivre ces quelques étapes :**

Pour chacune de ces étapes vous devrez être dans le fichier racines du projet:

1. Cloner le repo GitHub sur votre répertoire :
	-	Sous Linux : 
		-	Télécharger Git `apt install git`
		-	Cloner le repo `git clone https://github.com/jerkhouri/ESIEE-Python-Open-Data.git`
	- Sous Windows :
		- Télécharger le projet Git grâce à [ce lien](https://github.com/jerkhouri/ESIEE-Python-Open-Data.git) puis décompresser le fichier dans un répertoire ([WinRAR](https://www.win-rar.com/postdownload.html?&L=10), [WinZip](https://download.winzip.com/gl/gad/winzip24.exe)..)

Vous devez maintenant avoir cette architecture :
<p align="center">
<img src ="https://user-images.githubusercontent.com/39912632/70307722-189e7980-180a-11ea-816f-1e7f36e15544.png">
</p


2. Installer python3 :
	 - Sous Linux : `sudo apt install python3`
	 - Sous Windows : [Liens de téléchargement](https://www.python.org/ftp/python/3.8.0/python-3.8.0.exe)
3. Installer pip :
	 - Sous Linux : `sudo apt install python3-pip`
	 - Sous Windows : *Déjà présent lors du téléchargement de python3 (étape 1)*
4. Installer les dépendances liés au projet :
	 - Sous Linux : `pip3 install -r requirement.txt`
	 - Sous Windows : `pip.exe install -r .\requirement.txt`
5. Lancer le main.py:
	 -  Sous Linux : `python3 main.py`
	 - Sous Windows : `py.exe .\main.py`
6. Laissez vous guidez par le programme.

**Vous pouvez retrouver tous les histogrammes et cartes générés dans le répertoire "data/HistoGrammes" et "data/Map".**

![Archi2](https://user-images.githubusercontent.com/39912632/70308863-8186f100-180c-11ea-8935-ecff0f27ac40.png)

## Bonus
Nous avons souhaité avoir des informations sur l'évolution de la population par pays.
Le programme "histoCourbesGen.py" permet de généré une carte par pays.
Exemple pour la France:

![France](https://user-images.githubusercontent.com/39912632/68996442-4d1db600-089a-11ea-9000-2a7d5c2757fd.png)
Pour essayer, lancer la commande suivante dans le répertoire racine du projet :

 - Sous Linux : `python3 python/histoCourbesGens.py`
 - Sous Windows : `py.exe .\python\histoCourbesGens.py`
 
 Vos courbes apparaîtront dans le répertoire "data/HistoCourbes".

## COPYRIGHT ESIEE PARIS

<p align="center">
<img  height = 200 src ="https://user-images.githubusercontent.com/39912632/70309553-15a58800-180e-11ea-9cc2-f77e48f07965.png">
</p
