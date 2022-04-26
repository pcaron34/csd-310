#Paul Caron
#4/23/2022
#Module 9.2 Assignment

import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "BigBadWolfEater9/er",
    database = "pysports"
)

cursor = db.cursor()

print('-- DISPLAYING PLAYER RECORDS --')
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id ORDER BY player_id ASC")
player = cursor.fetchall()
for row in player:
    print("Player ID: ", row[0])
    print("First Name: ", row[1])
    print("Last Name: ", row[2])
    print("Team Name: ", row[3])
    print()


input("\n\n Press any key to continue...")

