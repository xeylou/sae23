import sqlite3 as sql
import numpy as np
import matplotlib.pyplot as plt

plt.axes(projection = 'polar')
plt.title("Direction et vitesse du vent")

tab = [241.1, 241.1, 241.1, 349.7, 3.1, 357.2, 93.3, 96.0, 241.1]
speed = [3.0, 3.0, 3.0, 2.4, 2.1, 2.1, 2.4, 3.3, 3.2]
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

plt.show() 


