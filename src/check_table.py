import sqlite3
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates


dbname = 'data/weight.db'
conn = sqlite3.connect(dbname)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute('SELECT * FROM weight')
all_list = []
date_list = []
weight_list = []
for row in cur:
  date_value = datetime.datetime.strptime(row['date'],"%Y-%m-%d")
  date_list.append(date_value)
  weight_list.append(row['weight'])
  all_list.append([row['id'],row['date'],row['weight']])

cur.close()
conn.close()

plt.plot(date_list,weight_list)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.savefig('data/result.png')
print(all_list)