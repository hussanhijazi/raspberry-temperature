import time
import Adafruit_DHT as dht
import urllib3

urllib3.disable_warnings()

poolReq = urllib3.PoolManager()
apiKey = '<YOUR-THINGSPEAK-KEY>'

while True:
    humidity, temperature = dht.read_retry(dht.DHT11, 4)
    print('Temperature: {}   Umid: {}'.format(temperature, humidity))
    poolReq.request('POST', 'https://api.thingspeak.com/update?api_key={}&field1={}&field2={}'.format(apiKey, temperature, humidity))
    time.sleep(60)
   