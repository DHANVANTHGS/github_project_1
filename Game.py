import sqlite3
connection=sqlite3.connect("Game.db")
cursor=connection.cursor()
import Game_start_point
bol=True
cursor.execute("SELECT *FROM score")
row=cursor.fetchall()
print("Points Table")
for i in row:
    print(i)
user=list(row[len(row)-1])
cursor.execute("SELECT * FROM log")
log_data=cursor.fetchall()
log_data=list(log_data)
if log_data[len(log_data)-1] in row:
    bol=False
if bol:
   if user[3]==1:
       import number_guesser
connection.close()
