from flask import Flask,render_template
from datetime import datetime
import logging
import sqlite3

app = Flask(__name__)
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def get_time_data():
    conn = create_connection('gardenData.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM dhtreadings")
    rows = cur.fetchall()
    times = []
    for i in range(25):
        print(type(rows[i][1]))
        times.append(datetime.strptime(rows[i][1], "%Y-%m-%d %H:%M:%S.%f").strftime('%m/%d/%y %H:%M:%S %p'))
    return times

def get_temp_data():
    conn = create_connection('gardenData.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM dhtreadings")
    rows = cur.fetchall()
    temps = []
    for i in range(25):
        temps.append(rows[i][2])
    return temps

def get_humid_data():
    conn = create_connection('gardenData.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM dhtreadings")
    rows = cur.fetchall()
    humids = []
    for i in range(25):
        humids.append(rows[i][3])
    return humids

@app.route("/")
def index():
    return render_template('index.html', labels=get_time_data(), temps=get_temp_data(), humids=get_humid_data())
 
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')
