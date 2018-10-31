import paho.mqtt.client as mqtt
import time
import Adafruit_DHT as dht
from variables import *

def on_message(client, userdata, message):
    print("message topic: ", message.topic, " - data: ", str(message.payload.decode("utf-8")))
    # print("message topic = ",message.topic)
    # print("message qos = ",message.qos)
    # print("message retain flag = ",message.retain)

# def on_connect(client, userdata, flags, rc):
#     # print("Connected with result code "+str(rc))
#     client.subscribe(temperature_topic)
#     client.subscribe(humidity_topic)

def mqtt_client_connect():
    client.on_message = on_message 
    # client.on_connect = on_connect
    print("connected to: ", broker_url)
    client.connect(broker_url)
    client.loop_start()

client = mqtt.Client("client_name")
mqtt_client_connect()

while True:
    humidity, temperature = dht.read_retry(dht.DHT11, 4)
    print('Temperature: {}   Humidity: {}'.format(temperature, humidity))
    client.publish(temperature_topic, temperature)
    client.publish(humidity_topic, humidity)
    time.sleep(3)


