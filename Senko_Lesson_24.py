# Senko_Timur group_208
# DZ


import random
import sqlite3

conn = sqlite3.connect('My_db.db')
cursor = conn.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT,
col_1, col_2) ''')
cursor.execute(''' INSERT INTO tab_1(col_1, col_2) VALUES (?,?) ''', (random.randint(1, 2), random.randint(1, 2)))
conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
cursor.execute('''DELETE FROM tab_1 WHERE id%2=0''')
conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
cursor.execute('''UPDATE tab_1 SET col_1='Колбаса', col_2='Васильки' ''')
conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
for i in k:
    print(i)
conn.close()
