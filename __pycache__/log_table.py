import sqlite3
connection=sqlite3.connect("Game.db")
cursor=connection.cursor()
cmd='''CREATE TABLE log (
name VARCHAR(25));'''
cursor.execute(cmd)
connection.close()