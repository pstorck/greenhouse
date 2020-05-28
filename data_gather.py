import Adafruit_DHT as DHT
import time, sqlite3
from datetime import datetime
import RPi.GPIO as GPIO

#how often measurement is taken
interval = 30
db = 'gardenData.db'

def create_connection(db_file):
	conn = None
	try:
		#will create new .db file if the file does not exist
		conn = sqlite3.connect(db_file)
	except Error as e:
		print(e)
	return conn

def take_measurement(connection):
	cur = connection.cursor()
	#makes sure that table dhtreadings exists
	cur.execute("CREATE TABLE IF NOT EXISTS dhtreadings (id integer PRIMARY KEY, dt TEXT, temperature REAL, humidity REAL)")
	humidity, temperature = DHT.read_retry(DHT.DHT22, 3)
	cur.execute("INSERT INTO dhtreadings (dt,temperature,humidity) VALUES(?, ?,?)", (datetime.now(), temperature, humidity))
	connection.commit()
	cur.close()

def main():
	conn = create_connection(db)
	while True:
		take_measurement(conn)
		time.sleep(interval)

if __name__ == "__main__":
	main()
