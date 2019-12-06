#!/usr/bin/python3
import sys
from python.downloadfile import maindownloadFile
from python.histoGrammesGen import mainhistoGrammesGen
from python.mapGen import mainmapGen

def choix():    
    Choix = input('Que souhaitez vous faire ?\n1- Créer un histogramme\n2- Créer une carte\n3- Quitter\nVotre choix: ')
    while(not Choix.isdigit() and Choix!= "1" and Choix != "2" and Choix !="3"):
        Choix = input("Choix incorrect, votre choix: ")

    if Choix == "1":        
        print("---------------------------------------")
        mainhistoGrammesGen()
        
        Choix2 = input('Souhaitez vous faire autres choses ? (O/N)\nVotre choix: ')
        if(Choix2 =="O" or Choix2 == "o"):
            choix()                
    elif Choix == "2":
        print("---------------------------------------")
        mainmapGen()

        Choix2 = input('Souhaitez vous faire autres choses ? (O/N)\nVotre choix: ')
        if(Choix2 =="O" or Choix2 == "o"):
            choix()    

def main():
    try:
        maindownloadFile()
    except:
        print("Impossible de télécharger les données")
        return 0 
    print("Bienvenue sur le projet python ESIEE")
    choix()  
    print("Merci d'avoir utilisé notre programme, à bientôt !")


if __name__ == '__main__':
    main()