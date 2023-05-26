#!/usr/bin/python3

##je récupère les données en JSON de l'API
##puis je les retourne dans une fonction

import json, requests

def get_info(lat, lon):
    url="https://api.met.no/weatherapi/locationforecast/2.0/compact?lat="+str(lat)+"&lon="+str(lon)

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0',
           'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache', 'Expires': '0'}
    
    ##on demande à l'api d'obtenir les données
    query=requests.get(url, headers=headers)
    text=query.text
    data=json.loads(text)

    return(data)

print(get_info(43.88566272770907, -0.5092243304975015))