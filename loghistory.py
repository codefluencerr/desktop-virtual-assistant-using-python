#the inserthistory method logs the commands in the postgress databas inside a table called history
import psycopg2
from datetime import date
from datetime import datetime
import sqlite3

def inserthistory(search_text):
    conn = sqlite3.connect('historydb.sqlite')
    cur = conn.cursor()
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    cur.execute('''
        CREATE TABLE IF NOT EXISTS history ( t TEXT, d TEXT);''')
    cur.execute('''INSERT INTO history (t,d)
               VALUES ( ?, ? )''', (dt_string, search_text))
    print("succesfull")
    conn.commit()
    return