import random
import time

from paho.mqtt import client as mqtt_client

# --------------------------------------------------
  #fonction qui récupère les données sur le service web

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

# --------------------------------------------------
  #création de mon topic
  
broker = 'test.mosquitto.org'
port = 1883
topic = "123"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

# --------------------------------------------------
  #connection mqtt
  
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# --------------------------------------------------
  #envoi sur mqtt

def publish(client):
    time.sleep(1)
    
    msg = str(get_info(43.88566272770907, -0.5092243304975015)) #il faut forcer python à prendre les données en chaines de caractère
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

# --------------------------------------------------

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

# --------------------------------------------------

if __name__ == '__main__':
    run()

