import paho.mqtt.client as mqtt
import time
import Adafruit_DHT as dht
import datetime
from variables import *

def mqtt_client_connect():
    print("connected to: ", broker_url)
    client.connect(broker_url)
    client.loop_start()

client = mqtt.Client("client_name")
mqtt_client_connect()

while True:
    humidity, temperature = dht.read_retry(dht.DHT11, 4)
    print('Sending... Temperature: {}   Humidity: {} / {}'.format(temperature, humidity, str(datetime.datetime.now())))
    client.publish(temperature_topic, temperature)
    client.publish(humidity_topic, humidity)
    time.sleep(3)
