from flask import Flask,render_template
from datetime import datetime
import sqlite3

app = Flask(__name__)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def get_rows():
    conn = create_connection('gardenData.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM (SELECT * FROM dhtreadings ORDER BY id DESC LIMIT 25) ORDER BY id ASC")
    rows = cur.fetchall()
    return rows

def get_time_data():
    rows = get_rows()
    times = []
    for i in range(len(rows)):
        times.append(datetime.strptime(rows[i][1], "%Y-%m-%d %H:%M:%S.%f").strftime('%H:%M:%S'))
    return times

def get_temp_data():
    rows = get_rows()
    temps = []
    for i in range(len(rows)):
        temps.append(round(float(rows[i][2]), 1))
    return temps

def get_cur_temp():
    return round(float(get_rows()[-1][2]), 1)

def get_humid_data():
    rows = get_rows()
    humids = []
    for i in range(len(rows)):
        humids.append(round(float(rows[i][3]), 1))
    return humids

def get_cur_humid():
    return round(float(get_rows()[-1][3]), 1)

@app.route("/conditions")
def conditions():
    return render_template('index.html', labels=get_time_data(), temps=get_temp_data(), humids=get_humid_data(), cur_temp=get_cur_temp(), cur_humid=get_cur_humid())
 
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')
