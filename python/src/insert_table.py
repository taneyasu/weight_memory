import sqlite3
import datetime
import sys

try:
  weight_value = float(input('体重を入れてください 。\n'))
except:
  print("エラー：体重は数字入力してください。")
  sys.exit()

try:
  date_text = str(input('日付を入れてください。yyyyy.MM.dd\n'))
  date_value = datetime.datetime.strptime(date_text, '%Y.%m.%d').date()
except:
  print("エラー：日付を入れてください。")
  sys.exit()

dbname = 'data/weight.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('INSERT INTO weight(date, weight) values(?,?)',(date_value,weight_value))

conn.commit()

cur.close()
conn.close()