#!/usr/bin/env python

import sqlite3 as sql
import numpy as np
import matplotlib.pyplot as plt

con = sql.connect ("alexis_code/php/files/sae23.sqlite") # on se connecte \u00e0 la bdd
cur = con.cursor() # on cr\u00e9e un curseur pour agir sur cette bdd

cur.execute("select date, relative_humidity from weather;") # on ex\u00e9cute une action sur la bdd

res = cur.fetchall() # on rassemble les \u00e9l\u00e9ments du cur sous forme de tableau dans la variable res
#print(res)

con.close()  # on ferme la connection

date=[]
air_temperature=[]

for row in res:			# pour chaque ligne
	(d,a) = tuple(row)	# on met les r\u00e9sultats sous forme de tuple 
	#print (d,a)
	date.append(d)		# on extrait les valeurs du tuple pour les mettre dans un tableau
	air_temperature.append(a)
	
#print (date,air_temperature)

tuple = (date,air_temperature)
#print(tuple)

fig, ax = plt.subplots() # subplots est un tuple avec fig qui correspond au dessin et ax aux valeurs
ax.plot(date, air_temperature) # on ajoute les valeurs de nos tableaux \u00e0 ax
plt.title('Humidité')
# plt.xticks(rotation = 45)
plt.xticks(rotation = 'vertical')


ax.set_ylabel("Taux d'humidité (en %)")
ax.set_xlabel('Date et heure')
plt.tight_layout()
#plt.xticks([]) # retire graduation en x
ax.xaxis.set_tick_params(labelsize=6)


plt.savefig("alexis_code/php/files/humidite.png", bbox_inches='tight') # on fait afficher le graphe
