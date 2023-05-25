#!/usr/bin/python3

import json, random
from paho.mqtt import client as mqtt_client

##create a python program that can publish
##a json message to a mqtt broker

json_message=""

broker='test.mosquitto.org'
port=1883
topic="/adehu-sae23"
client_id = f'python-mqtt-{random.randint(0, 1000)}'