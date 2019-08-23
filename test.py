import Adafruit_DHT as DHT
import time, sqlite3
from datetime import datetime
import RPi.GPIO as GPIO

conn = sqlite3.connect('gardenData.db')
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while True:
	c = conn.cursor()
	humidity, temperature = DHT.read_retry(DHT.DHT22, 3)
	if temperature > 25:
		GPIO.output(17, GPIO.HIGH)
	else:
		GPIO.output(17, GPIO.LOW)
	print('Humidity: {} Temperature: {}'.format(humidity, temperature))
	c.execute("INSERT INTO dhtreadings (timestamp,temperature,humidity) VALUES(?,?,?)",  (datetime.now(), humidity, temperature))
	conn.commit()
	c.close()
	time.sleep(1)
