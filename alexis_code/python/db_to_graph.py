#!/usr/bin/python3

import sqlite3 as sql
import numpy as np
import matplotlib.pyplot as plt

con=sql.connect("alexis_code/php/files/sae23.sqlite")
cur=con.cursor()

info_to_catch="air_temperature" #choose between air_temperature and relative_humidity
#info_to_catch="air_temperature"
query="select date, " + info_to_catch + " from weather"

cur.execute(query)
res=cur.fetchall()

con.close()

date=[]
air_temperature=[]

for row in res:
	(d,a)=row
	date.append(d)
	air_temperature.append(a)

tuple=(date,air_temperature)

fig, ax=plt.subplots()
ax.plot(date, air_temperature)
plt.xticks(rotation=90)
plt.show()
