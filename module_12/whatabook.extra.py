#--------------------------------------------------------------------------------#
# Delete from table
#cursor.execute("DELETE FROM `store` WHERE `store_id` = 1")
#db.commit()
#print(cursor.rowcount, "was deleted")

#--------------------------------------------------------------------------------#
# TO INSERT INTO WISHLIST
#sql = "INSERT wishlist (book_id, user_id) VALUES (%s, %s)"
#val = [
#    ("101", "11"),
#    ("104", "13"),
#    ("108", "12"),
#]
#cursor.executemany(sql, val)
#db.commit()
#print(cursor.rowcount, "was inserted.")

#--------------------------------------------------------------------------------#
# THIS WORKS FOR ENTERING USERS INTO THE DATABASE ***SAVE***
#sql = "INSERT users (first_name, last_name, user_id) VALUES (%s, %s, %s)"
#val = [
#    ("George", "Rockwell", "11",),
#    ("Matt", "Koehl", "12",),
#    ("Rocky", "Suhayda", "13",),
#]
#cursor.executemany(sql, val)
#db.commit()
#print(cursor.rowcount, "was inserted.")

#--------------------------------------------------------------------------------#
# INSERT ONE STORE LOCATION
#insert_Location = "INSERT store (store_id, locale) VALUES (%s, %s)"
#insert_val = ("1", "1234 Foxconn Rd SuperSmallTown, NE 68999")
#cursor.execute(insert_Location, insert_val)
#db.commit()
#print(cursor.rowcount, "was inserted.")

#--------------------------------------------------------------------------------#
# THIS WORKS FOR THE DATABASE ***SAVE*** FOR MULTIPLE ENTRIES
#sql = "INSERT books (author, book_id, book_name, details) VALUES (%s, %s, %s, %s)"
#val = [
#    ("James McPherson", "100", "Battle Cry of Freedom: The Civil War Era", "very long list",),
#    ("Michael Shaara", "101", "The Killer Angels", "still to long to list",),
#    ("Tony Horwitz", "102", "Confederates in the Attic", "thought you knew",),
#    ("Eric Foner", "103", "The Fiery Trial", "fine it has a picture of Abe Lincoln on the cover",),
#    ("David Blight", "104", "Race and Reunion", "nope",),
#    ("Ron Chernow", "105", "Grant", "Along time ago in the Milky Way",),
#    ("S.C. Gwynne", "106", "Rebel Yell", "a little of this, a little of that",),
#    ("Shelby Foote", "107", "The Civil War", "a book on the civil war",),
#    ("Stephen Crane", "108", "The Red Badge of Courage", "not the cowardly lion",),
#]
#cursor.executemany(sql, val)
#db.commit()
#print(cursor.rowcount, "was inserted.")

#--------------------------------------------------------------------------------#
# CREATE A TABLE
#cursor.execute("CREATE TABLE wishlist (user_id INT(75), book_id VARCHAR(75))")

#--------------------------------------------------------------------------------#
# JUST TO SHOW TABLES
#cursor.execute("SHOW TABLES")
#for x in cursor:
#    print(x)

#--------------------------------------------------------------------------------#

