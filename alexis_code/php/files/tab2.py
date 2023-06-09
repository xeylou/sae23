#!/usr/bin/env python

import sqlite3 as sql
import numpy as np
import matplotlib.pyplot as plt

con = sql.connect ("alexis_code/php/files/sae23.sqlite")
cur = con.cursor()

#on récupère toutes les dates sans les heures pour nom des graphiques
cur.execute("SELECT DISTINCT SUBSTR(date, 1, 5) FROM weather ORDER BY date DESC;")

#res le tableau des jours
res = cur.fetchall()

tableau_des_jours=[]
for row in res:
    tableau_des_jours.append(row[0])

#on va créer un tableau de tuples pour (date+h, temperature) & (date+h, humidite)
tableau_association_temperatures=[]
tableau_association_humidite=[]
tableau_association_windspeed=[]
tableau_association_windorientation=[]


# pour toutes les dates sans les heures, je récupère sous forme de tableaux
# les informations qu'il me faut pour les tableaux de tuples
for row in res:			# pour toutes les dates
    requete = "SELECT * FROM weather WHERE date LIKE '" + str(row[0]) + "%';"
    cur.execute(requete)
    res2 = cur.fetchall()
    #print(f"exemple de {res2}")
    for row2 in res2:
        tableau_association_temperatures.append((row[0], row2[0], row2[3]))
        tableau_association_humidite.append((row[0], row2[0], row2[5]))
        tableau_association_windspeed.append((row[0], row2[0], row2[7]))
        tableau_association_windorientation.append((row[0], row2[0], row2[6]))
    #print(f"fin de tableau association temp {tableau_association_temperatures}")

for row in res:
    t_temp_tab=[] #axe des y avec températures
    h_temp_tab=[] #axe des x avec heures
    hu_temp_tab=[] #y humidité
    ws_temp_tab=[] #thésée vitesse du vent
    wo_temp_tab=[] #théesée orientation du vent
    for i in range(len(tableau_association_temperatures)):
        if row[0] == tableau_association_temperatures[i][0]:
            t_temp_tab.append(tableau_association_temperatures[i][2])
            h_temp_tab.append(tableau_association_temperatures[i][1])
            hu_temp_tab.append(tableau_association_humidite[i][2])
            ws_temp_tab.append(tableau_association_windspeed[i][2])
            wo_temp_tab.append(tableau_association_windspeed[i][2])
    #tableaux thesee
    vents=[] #orientation du vent en degrès
    for i in range (len(wo_temp_tab)):
	    conv = wo_temp_tab[i]*3.14/180
	    vents.append(conv)
    polaire=[]
    for i in range (len(vents)):
	    polaire.append((vents[i],ws_temp_tab[i]))
    for i in range (len(polaire)):
	    plt.polar(polaire[i][0],polaire[i][1],'g.')
	    #print (polaire[i][0],polaire[i][1])
    angles = 2*np.pi*np.linspace(0, 1, 9)
    radDeg = 180/np.pi 
    etoile = np.array([6, 1, 6, 1, 6, 1, 6, 1, 6])
    courbes = plt.polar(angles, etoile,'gray')
    axes = plt.gca()
    axes.set_thetagrids(angles=radDeg*angles[0:-1], labels=("E", "NE", "N", "NO", "O", "SO", "S", "SE"))
    #plt.show()
    file_name="alexis_code/php/files/" + str(row[0]) + "_polaire.png"
    plt.savefig(file_name)