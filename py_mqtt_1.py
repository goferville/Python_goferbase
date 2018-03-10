"""
Server 	m10.cloudmqtt.com
User 	vasdqkul
Password 	IXAeordypugS
Port 	18322
SSL Port 	28322
Websockets Port (TLS only) 	38322
Connection limit 	10
"""
import paho.mqtt.client as mqtt
import os, time
from urllib import parse as urlparse

#region Event Callbacks
#  Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)

def on_publish(client, obj, mid):
    print("mid: " + str(mid))
    time.sleep(1)

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

#endregion

mtsvr='m10.cloudmqtt.com'
mtport=18322
mtusr="vasdqkul"
mtusr="vasdqkul"
mtpd="IXAeordypugS"
#client
client=mqtt.Client("Python1",clean_session=True)
# Assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe

# Connect
client.username_pw_set(mtusr,mtpd)
client.connect(mtsvr, mtport)
topic='light'

# Start subscribe, with QoS level 0
client.subscribe(topic, 0)

# Publish a message
client.publish(topic, "Light is ON")

# Continue the network loop, exit when an error occurs
client.loop_forever()