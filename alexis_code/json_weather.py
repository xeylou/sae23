## alexis' contribution to mr. munier code

import json, requests

##latitude & longitude of the asked place
lat=43.88566272770907
lon=-0.5092243304975015

##getting wanted url by putting lat & long by get method
url="https://api.met.no/weatherapi/locationforecast/2.0/compact?lat="+str(lat)+"&lon="+str(lon)

##creating http header manually for requets library
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0',
           'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache', 'Expires': '0'}

##asking data
query=requests.get(url, headers=headers)
text=query.text

##getting data in json plain text format
data = json.loads(text)
#print(data)

##extracting wanted json data
#catching all units
units = data["properties"]["meta"]["units"]
#timeseries for all days, 0 is today, catching data for today w/ 0
#details is all the data for the time
weather = data["properties"]["timeseries"][0]["data"]["instant"]["details"]

##printing all data with associate units

for key in weather.keys():
    print("%s = %2.2f %s" %(key, weather[key], units[key]))
print("\n")

##adding the output to a variable
json_data=""
for key in weather.keys():
    json_data+=("%s = %2.2f %s" %(key, weather[key], units[key])+"\n")
print(json_data)