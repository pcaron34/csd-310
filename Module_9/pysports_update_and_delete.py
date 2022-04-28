#Paul Caron
#4/25/2022
#Module 9.3 Assignment
#This assignment was to learn how 
#to add, update, and delete queries in a MySQL database

import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "BigBadWolfEater9/er",
    database = "pysports"
)

cursor = db.cursor()

# THIS PART I USED FOR UPDATING**********************8
#update = "UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer', player_id = 21 WHERE first_name = 'Smeagol'"
#cursor.execute(update)
#db.commit()
#print(cursor.rowcount, "records(s) committed")


print('-- DISPLAYING PLAYER AFTER DELETE --')
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id ASC")
player = cursor.fetchall()
for row in player:
    print("Player ID: ", row[0])
    print("First Name: ", row[1])
    print("Last Name: ", row[2])
    print("Team Name: ", row[3])
    print()
#print('-- DISPLAYING PLAYERS AFTER INSERT --')

#cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES ('Smeagol', 'Shire Folk', '1')")
#player = cursor.fetchall()
#for row in player:
#    print("First Name: ", row[2])
#    print("Last Name: ", row[3])
#    print("Team ID: ", row[4])

#db.commit()

# THIS PART I USED FOR INSERTING***************************
#sql = "INSERT INTO player (Player_id, first_name, last_name, team_id) VALUES (%s, %s, %s, %s)"
#val = ("21", "Smeagol", "Shirefolk", "1")
#cursor.execute(sql, val)
#db.commit()





#cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id ASC")
#player = cursor.fetchall()
#for row in player:
#    print("Player ID: ", row[0])
#    print("First Name: ", row[1])
#    print("Last Name: ", row[2])
#    print("Team Name: ", row[3])
#    print()

# THIS PART IS WHAT I USED FOR DELETING****************************
sql = "DELETE FROM player WHERE first_name = 'Gollum'"
cursor.execute(sql)
db.commit()
print(cursor.rowcount, "record(s) deleted")

#sql2 = "ALTER TABLE player ADD CONSTRAINT player_id UNIQUE(player_id)"
#cursor.execute(sql2)
#db.commit()
#print("Updated hopefully")



input("\n\n Press any key to continue...")

