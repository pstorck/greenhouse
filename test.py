import sqlite3
from datetime import datetime

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def get_time_data(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM dhtreadings")
    rows = cur.fetchall()
    print(type(rows[0][1]))
    times = []
    for row in rows:
        times.append(datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S.%f").strftime('%m/%d/%y %H:%M:%S %p'))
    return times
    
def get_temp_data(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM dhtreadings")
    rows = cur.fetchall()
    temps = []
    for row in rows:
        temps.append(row[2])
    return temps

if __name__ == '__main__':
    conn = create_connection('gardenData.db')
    print(get_time_data(conn))