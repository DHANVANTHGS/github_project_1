import sqlite3
connection=sqlite3.connect("Game.db")
cursor=connection.cursor()
cmd='''CREATE TABLE score(
no INTEGER PRIMARY KEY,
name VARCHAR(25),
points INTEGER DEFAULT 0,
lvl INTEGER DEFAULT 1
);'''
cursor.execute(cmd)
connection.close()