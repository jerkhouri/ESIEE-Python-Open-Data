import folium,json,math, os, sys
from pathlib import Path
import pandas as pd

def createMapdirectory():
    file_path=("data/Map")
    file_data = Path(file_path)
    if not file_data.exists():
        os.makedirs(file_path)        
        print('Creation du repertoire '+file_path)
    return 1

def progressbar(i):
	sys.stdout.write("\r[%.2f" %i + "%]" + "=" * (int)(i)+ ">")


def mainmapGen():
    createMapdirectory()
    ################## Traitement du fichier geojson ##################
    geo_data = {"type": "FeatureCollection", "features": []} # master dict structure

    f = open('data/data.json', 'r', encoding='utf8')#ouvre le fichier
    g = json.loads(f.read())#stock son contenue dans g
    f.close()#ferme le fichier
    list_country_code_json = [] #création de la liste des country code du fichier geojson
    for i in range(0, len(g['features'])):#parcours le geojson
        list_country_code_json.append(g['features'][i]['id'])#stock tout les country code du geojson dans une liste
        
    geo_data["features"].extend((g["features"]))# add current geojson data to master dict
    

    ################## Traitement du fichier csv ##################
    data = pd.read_csv('data/data.csv', skiprows=5, sep=',')# stocks les données du scv a partir de la ligne 5(format panda)
    rep = 0
    debut = 0
    fin = 0
    
    tab_annee= data.columns #stock les années du fichier csv

    first_anne_valid = int(tab_annee[4])
    last_annee_valid = int(tab_annee[len(tab_annee) - 2])

    
    debut = "pas un digit"
    fin = "pas un digit"
    int_debut = 0
    int_fin = 0
    while(not debut.isdigit() or (int_debut < first_anne_valid or int_debut > last_annee_valid-1)):
        debut = input("Entrez l'année de départ (comprise entre "+ str(first_anne_valid) +" et "+ str(last_annee_valid-1) +") : ")
        if(debut.isdigit()):
            int_debut = int(debut)
    while(not fin.isdigit() or (int_fin < int_debut or int_fin > last_annee_valid-1)):
        fin = input("Entrez l'année de la derniere map à génerer (comprise entre "+ str(int_debut) +" et "+ str(last_annee_valid-1) +") : ")
        if(fin.isdigit()):
            int_fin = int(fin)
    int_debut -= 1960   #Range de 
    int_fin -= 1959


    i = 0.0 							#Pourcentage pour barre de progression
    nb_année =  100 / (int_fin-int_debut)	#Evaluation du nombre de pays à traité
    print("Génération des maps en cours")
    for a in range(4 + int_debut,int_fin + 4):#on fait une boucle pour chaque année (on commence a 4 car les 4 premiere donnée ne correspondent pas a des années)
        df_tmp = data #on copie les données de pandas pour ne pas les modifiers
        df_tmp = df_tmp.loc[:, ('Country Code', tab_annee[a])]#on garde seulement les colonnes country code et l'année actuel car c'est les données utiles pour le choropleth
        list_country_code_csv = df_tmp['Country Code'] #on stock les country code du fichier csv dans une liste
        len_list_country_code_csv = len(list_country_code_csv)#on utilise 2 fois cette donnée donc on la stock pour éviter de refaire un len(list_country_code_csv) et donc optimiser le temps
        index_good_country = []#on stock les index
        for j in range(0, len_list_country_code_csv):#on parcours les country code du csv
            for k in range(0, len(list_country_code_json)):#on parcours les country code du geojson
                if(list_country_code_csv[j] == list_country_code_json[k]): # si les codes sont dans csv et geojson
                    index_good_country.append(j)#on ajoute les codes dans la liste des bon code
                    break#sors de la boucle k si on trouve un résultat

        final = pd.DataFrame(columns=['Country Code',tab_annee[a]])#initialise les donnees final avec country code et l'annee en tête
        for m in range(0,len_list_country_code_csv):#boucle de la taille des country code du fichier csv
            for n in range(0,len(index_good_country)):#boucle de la taille des bon index
                if m == index_good_country[n]:#si m(la ligne du csv) est égal a l'index d'une bonne country
                    final.loc[len(final)] = [df_tmp['Country Code'][m],math.log(df_tmp[tab_annee[a]][m])]#on ajoute le country code et sa population lié a l'année

        ################## Creation de la map ##################

        coords = (48.8566969, 2.3514616)#position de départ lors de l'ouverture de la map
        map = folium.Map(location=coords, tiles="OpenStreetMap", zoom_start=1)#position, titre et zoom


        binse = final[tab_annee[a]].quantile([0,0.05,0.2,0.4,0.65,0.8,0.97,1]) #modification de l'echelle

        folium.Choropleth(
            geo_data=geo_data,#donnees geojson
            name='choropleth',
            data=final,#donnees csv
            columns=['Country Code',tab_annee[a]], # data key/value pair
            key_on='feature.id', # corresponding layer in GeoJSON
            fill_color='YlGn',#colorie de la map
            fill_opacity=0.7,#opacité de la surcouche
            line_opacity=0.1,#opacité des lignes séparatrices
            legend_name='Population par pays en log',#pour l'échelle
            bins=binse,#pour l'échelle
            reset=True#pour l'echelle
        ).add_to(map)
        map.save(outfile='data/Map/'+tab_annee[a]+'.html')#emplacement de la map et nom du fichier
            
        i+=nb_année
        progressbar(i)
    print("\nToutes les années ont été générées")
    pass

if __name__ == '__main__':    
    mainmapGen()
