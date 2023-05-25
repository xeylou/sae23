CREATE TABLE "weather" (
	"date"	TEXT NOT NULL,
	"latitude"	REAL,
	"longitude"	REAL,
	"air_temperature"	REAL,
	"cloud_area_fraction"	REAL,
	"relative_humidity"	REAL,
	"wind_from_direction"	REAL,
	"wind_speed"	REAL
);

# /!\ CREATING DB ONCE IN WRONG PATH AND 
# CREATING A SECOND ONE IN THE RIGHT ONE
# AND ONLY USE IT AFTER EVEN IF THE FIRST
# ONE IS DELETED
# (or just precise the path like i did?)