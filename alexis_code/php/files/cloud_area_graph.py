#!/usr/bin/env python

import sqlite3 as sql
import numpy as np
import matplotlib.pyplot as plt

con = sql.connect ("alexis_code/php/files/sae23.sqlite") 
cur = con.cursor()

cur.execute("select date, cloud_area_fraction from weather;")

res = cur.fetchall()

con.close()  # on ferme la connection

date=[]
cloud_area_fraction=[]

for row in res:		
	(d,a) = tuple(row)	
	#print (d,a)
	date.append(d)		
	cloud_area_fraction.append(a)
	
#print (date,cloud_area_fraction)

tuple = (date,cloud_area_fraction)
#print(tuple)

fig, ax = plt.subplots() 
ax.plot(date, cloud_area_fraction)
plt.title('Recouvrement des nuages')
plt.xticks(rotation = 45)
plt.tight_layout()
ax.fill_between(date, cloud_area_fraction, alpha=0.7)
ax.set_ylabel('Couverture des nuages (en %)')
ax.set_xlabel('Date et heure')

plt.savefig("alexis_code/php/files/cloud_area_fraction.png", bbox_inches='tight') # on fait afficher le graphe
#plt.show()