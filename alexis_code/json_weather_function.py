#!/usr/bin/python3

## alexis' contribution to mr. munier code
##doing it in a function

import json, requests

def get_info(lat, lon):
    url="https://api.met.no/weatherapi/locationforecast/2.0/compact?lat="+str(lat)+"&lon="+str(lon)

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0',
           'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache', 'Expires': '0'}
    
    query=requests.get(url, headers=headers)
    text=query.text
    data = json.loads(text)

    units = data["properties"]["meta"]["units"]
    weather = data["properties"]["timeseries"][0]["data"]["instant"]["details"]

    json_data=[]
    for key in weather.keys():
        json_data.append(weather[key])
    return(json_data)

#print(get_info(43.88566272770907, -0.5092243304975015))