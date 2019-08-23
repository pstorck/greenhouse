import Adafruit_DHT as DHT
import time, sqlite3
from datetime import datetime

conn = sqlite3.connect('gardenData.db')

for i in range(10):
	c = conn.cursor()
	humidity, temperature = DHT.read_retry(DHT.DHT22, 3)
	print('Humidity: {} Temperature: {}'.format(humidity, temperature))
	c.execute("INSERT INTO dhtreadings (timestamp,temperature,humidity) VALUES(?,?,?)",  (datetime.now(), humidity, temperature))
	conn.commit()
	c.close()
	time.sleep(5)
