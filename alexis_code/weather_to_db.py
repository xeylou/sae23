#!/usr/bin/python3
import sqlite3, datetime, json_weather_function as current_data

##catching date + if we want 
##to sort them  it will work
date = datetime.datetime.now()

##catching array of current weather data
lat=43.88566272770907
lon=-0.5092243304975015
results=current_data.get_info(lat, lon)

##connection to the db & creating a cursor
db_name="alexis_code/sae23.sqlite"
connection=sqlite3.connect(db_name)
cursor=connection.cursor()

cursor.execute(
    "INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    (date, lat, lon, results[1], results[2], results[3], results[4], results[5])
)
# # new_tank_number = 2
# # moved_fish_name = "Sammy"
# # cursor.execute(
# #     "UPDATE fish SET tank_number = ? WHERE name = ?",
# #     (new_tank_number, moved_fish_name)
# # )

##save (commit) the changes & close connection
connection.commit()
connection.close()

