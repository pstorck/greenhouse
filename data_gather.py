import Adafruit_DHT as DHT
import time, sqlite3
from datetime import datetime
import RPi.GPIO as GPIO

db = 'gardenData.db'

def create_connection(db_name):
	conn = None
	try:
		conn = sqlite3.connect(db_name)
	except Error as e:
		print(e)
	return conn

def take_measurement(connection):
	cur = connection.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS dhtreadings (id integer PRIMARY KEY, dt TEXT, temperature REAL, humidity REAL)")
	humidity, temperature = DHT.read_retry(DHT.DHT22, 3)
	cur.execute("INSERT INTO dhtreadings (dt,temperature,humidity) VALUES(?, ?,?)", (datetime.now(), temperature, humidity))
	connection.commit()
	cur.close()

def main():
	conn = create_connection(db)
	while True:
		take_measurement(conn)
		time.sleep(1)

if __name__ == "__main__":
	main()
