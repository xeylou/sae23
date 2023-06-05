#!/usr/bin/python3

import json, random, requests, time
from paho.mqtt import client as mqtt_client

#catching json info from the api
def catching_json_from_api():
    url="https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=43.88566272770907&lon=-0.5092243304975015"

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Cache-Control': 'no-cache, no-store, must-revalidate', 'Pragma': 'no-cache', 'Expires': '0'}

    query=requests.get(url, headers=headers)
    text=query.text
    data=json.loads(text)
    return(data)

# units=data["properties"]["meta"]["units"]
# weather=data["properties"]["timeseries"][0]["data"]["instant"]["details"]

# json_data=[]
# for key in weather.keys():
#     json_data.append(weather[key])
# print(json_data)

#publishing on the mqtt broker
broker_url = 'test.mosquitto.org'
port = 1883
topic = "/adehutest"
# generate client ID with pub prefix randomly
client_id=f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker_url, port)
    return client

def publish(client):
    time.sleep(2)

    #forcing the json to be a sting    
    data=str(catching_json_from_api())
    result = client.publish(topic, data)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send json to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()

