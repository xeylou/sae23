#!/usr/bin/python3
import sqlite3, datetime, json, requests

##catching date + if we want 
##to sort them it will work
date=datetime.datetime.now()
lat=43.88566272770907
lon=-0.5092243304975015

##catching array of current weather data
# results=get_info(lat, lon)
url="https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=43.88566272770907&lon=0.5092243304975015"

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0',
        'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache', 'Expires': '0'}

query=requests.get(url, headers=headers)
text=query.text
data=json.loads(text)

units=data["properties"]["meta"]["units"]
weather=data["properties"]["timeseries"][0]["data"]["instant"]["details"]

results=[]
for key in weather.keys():
    results.append(weather[key])
print('a')    
##connection to the db & creating a cursor
#db_name="alexis_code/sae23.sqlite"
db_path='alexis_code/sqlite3/sae23.sqlite'
connection=sqlite3.connect(db_path)
cursor=connection.cursor()

cursor.execute(
    "INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    (date, lat, lon, results[1], results[2], results[3], results[4], results[5])
)

##commit the changes & close connection + cursor
connection.commit()
cursor.close()
connection.close()




