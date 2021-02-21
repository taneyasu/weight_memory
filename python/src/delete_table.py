import sqlite3

dbname = 'data/weight.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

try:
  id_value = int(input('idを入れてください。\n'))
except:
  print("数字を入れてください。")
  sys.exit()

cur.execute('DELETE FROM weight where id = ?', (id_value,))

conn.commit()

cur.close()
conn.close()