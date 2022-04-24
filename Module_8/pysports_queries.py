import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "BigBadWolfEater9/er",
    database = "pysports"
)
cursor = db.cursor()

#cursor.execute("CREATE DATABASE mydatabase")

#cursor.execute("CREATE TABLE team (team_id INT(50), team_name VARCHAR(255), mascot VARCHAR(255))")
#cursor.execute("CREATE TABLE player (player_id INT(50), first_name VARCHAR(255), last_name VARCHAR(255), team_id INT(50))")

#cursor.execute("SHOW DATABASE")

#cursor.execute("SHOW TABLES")

#cursor.execute("ALTER TABLE <example> ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#sql = "DROP TABLE player"
#sql = "INSERT INTO team (team_id, team_name, mascot) VALUES (%s, %s, %s)"
#val = ("2", "Team Sauron", "Orcs")
#sql = "INSERT INTO player (Player_id, first_name, last_name, team_id) VALUES (%s, %s, %s, %s)"
#val = ("1", "Thorin", "Oakenshield", "1")
#cursor.execute(sql, val)
#cursor.execute()
#db.commit()
#print(cursor.rowcount, "record inserted.")



#cursor.execute("SELECT * FROM team")

#rows = cursor.fetchall()



print('-- DISPLAYING TEAM RECORDS --')
cursor.execute("SELECT Team_id, team_name, mascot FROM team")
teams = cursor.fetchall()
#for team in teams:
    #print("Team ID: {}".format([1]), "Team Name: {}".format([]), "Mascot: {}".format([]))
for row in teams:
    print("Team ID: ", row[0])
    print("Team Name: ", row[1])
    print("Mascot: ", row[2])
    print()

print('-- DISPLAYING PLAYER RECORDS --')
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player ORDER BY player_id ASC")
player = cursor.fetchall()
for row in player:
    print("Player ID: ", row[0])
    print("First Name: ", row[1])
    print("Last Name: ", row[2])
    print("Team ID: ", row[3])
    print()

print("Press any key to continue...")