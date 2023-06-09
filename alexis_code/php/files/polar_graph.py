import sqlite3 as sql
import numpy as np
import matplotlib.pyplot as plt


con = sql.connect ("alexis_code/php/files/sae23.sqlite") # on se connecte \u00e0 la bdd
cur = con.cursor() # on cr\u00e9e un curseur pour agir sur cette bdd

cur.execute("select wind_from_direction, wind_speed from weather;") # on ex\u00e9cute une action sur la bdd
res = cur.fetchall()
con.close()

tab=[] #direction vent non converti (radian)
speed=[]

for row in res:
    (direction_vent, vitesse_vent) = tuple(row)
    tab.append(direction_vent)
    speed.append(vitesse_vent)



plt.axes(projection = 'polar')
plt.title("Direction et vitesse des vents")


vents = []

for i in range (len(tab)):
	conv = tab[i]*3.14/180
	vents.append(conv)
	
polaire=[]
for i in range (len(vents)):
	polaire.append((vents[i],speed[i]))

for i in range (len(polaire)):
	plt.polar(polaire[i][0],polaire[i][1],'g.')
	print (polaire[i][0],polaire[i][1])

angles = 2*np.pi*np.linspace(0, 1, 9)
radDeg = 180/np.pi 
etoile = np.array([6, 1, 6, 1, 6, 1, 6, 1, 6])
courbes = plt.polar(angles, etoile,'gray')

axes = plt.gca()
axes.set_thetagrids(angles=radDeg*angles[0:-1], labels=("E", "NE", "N", "NO", "O", "SO", "S", "SE"))

plt.savefig("alexis_code/php/files/polar.png")


