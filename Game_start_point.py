import sqlite3
connection=sqlite3.connect("Game.db")
cursor=connection.cursor()
def new_user():
    name=input("Enter your name :")
    cursor.execute("INSERT INTO log (name) VALUES (?)",(name,))
    connection.commit()
    cmd="INSERT INTO score (name) VALUES (?);"
    cursor.execute(cmd,(name,))
    connection.commit()
    
def existing_user():
    print("Welcime back !")
    name=input("Enter your name :")
    cursor.execute("INSERT INTO log (name) VALUES (?)",(name,))
    connection.commit()
    cmd="SELECT * FROM score WHERE name= ?;"
    cursor.execute(cmd,(name,))
    data=cursor.fetchall()
    if data:
        cursor.execute("DELETE FROM score WHERE name=?",(name,))
        connection.commit()
        cursor.execute("INSERT INTO score (no,name,points,lvl) VALUES (?,?,?,?)",data[0])
        connection.commit()
    else :
        print("No data found")
        return 0
    
print("Are you an existing user ")
print("If Yes choose log_in ,New user choose sign_up")
print("1)sign_in /n 2)Log_in ")
check=True
while check:
    entry=int(input(" Enter your choice (1/2)"))
    if entry==1:
        new_user()
        break
    elif entry==2:
        existing_user()
        break
    else :
        print("Wrong input")
        print("Do you want to exit ?(1.Yes/2.NO)")
        if int(input())==1:
            check=False
connection.close()