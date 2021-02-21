import sqlite3

dbname = 'data/weight.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute(
    'CREATE TABLE weight(id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, weight REAL)'
)

conn.commit()
conn.close()