# does what it says
import sys
import time
import mysql.connector
from mysql.connector import Error

# database connection requirements as db
db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "BigBadWolfEater9/er",
    database = "whatabook"
)

cursor = db.cursor()

def get_wishlist_book():
    cursor.execute("INSERT INTO wishlist() VALUES({}, {})".format(user_id, book_id))

# menu function, just prints the options
def menu():
    print()
    print()
    print("--------------------------------------")
    print("Welcome to the library with 9 books")
    print("--------------------------------------")
    print("[1] View Books")
    print("[2] View Store Locations")
    print("[3] My Account")
    print("[4] Exit the program")
    print()
    print()
# calls the menu function and asks for the users option
menu()

#cursor.execute("")
option = int(input("Enter your option: "))

# while not zero do something if zero quit
while option != 4:
    if option == 1:
        #print out list of books
        print("The books we have are: ")
        cursor.execute("SELECT * FROM books")
        result = cursor.fetchall()
        for row in result:
            print(row)

    elif option == 2:
        
        #print out list of stores and locations
        print("The stores we have in the city currently are: ")
        cursor.execute("SELECT * FROM store ORDER BY 'store_id'")
        result = cursor.fetchall()
        for row in result:
            print(row)

    elif option == 3:
        # prints user id just because we are dealing with fictitious people here
        print("User id numbers are 11, 12, and 13")
        cursor = db.cursor(buffered=True)

        access = int(input("Enter your user id: "))

        # struggled on this one for way to long for such an easy thing
        if access < 11 or access > 13:
            print("Not a valid user, see ya!")
            break

        #print out the my accounts options
        print("My Account")
        print("-------------------")
        print("[1] Wishlist")
        print("[2] Add Book")
        print("[3] Main Menu")
        # ask user what they want to do
        acct_option = int(input("Enter your option: "))
        while acct_option != 3:
            # if they press one nothing really happens
            if acct_option == 1:
                print("Wishlist")
                break
            # if the press two it prints a list of the books and asks more questions    
            elif acct_option == 2:
                #print out list of books
                print("The books we have are: ")
                cursor.execute("SELECT * FROM books")
                result = cursor.fetchall()
                for row in result:
                    print(row)
                # user id is already established                
                user_id = access #input("Enter your user id: ")
                # gets the book id for the database
                book_id = input("Enter the book id: ")
                # insert statement for the database
                insertStatement = ("INSERT INTO wishlist (user_id, book_id) VALUES (%s, %s)")
                # variables holding user id(which was gotten earlier) and book id
                data = (access, book_id)
                # database execute command
                cursor.execute(insertStatement, data)
                # commit to the database
                db.commit()
                # mama always said to be polite (read this in Forrest Gump's voice...lol)
                print("Thank you, enjoy your book")
                time.sleep(2)
                acct_option = 3

                # this was a failed attempt
                #if wantedBooks == True:
                #    sql = "INSERT wishlist (book_id, user_id) VALUES (%s, %s)"
                #    val = [
                #        ("101", "11"),
                #        ("104", "13"),
                #        ("108", "12"),
                #    ]
                #    cursor.executemany(sql, val)
                #    db.commit()
                #    print(cursor.rowcount, "were or was inserted.")
                #else:
                #    print("There was an issue")
                

                #print out list of books
                #print("The books we have are: ")
                #cursor.execute("SELECT book_id, book_name, author, details FROM books")
                #result2 = cursor.fetchall()
                #if result2:
                #    for x in result2:
                #        print(x)
                #    acct_option = 3
                                
            # returns
            elif acct_option == 3:
                acct_option()
            # prints out when user doesn't do something right
            else:
                print("For the security of our patrons you have been kicked out of the system, make sure you are "
                    "entering information correctly.")
                sys.exit()

    elif option == 4:
        # exits the program
        sys.exit()
    else:
        print("Invalid option")

    print()
    # re-prints the options menu and waits for user to enter a number
    menu()
    option = int(input("Enter your option: "))

print("Thank you, and have a nice day.")

#--------------------------------------------------------------------------------#
# Alter wishlist
#cursor.execute("ALTER TABLE `wishlist` ADD COLUMN `wishlist_id` INT AUTO_INCREMENT PRIMARY KEY")

#--------------------------------------------------------------------------------#
# Delete from table
#cursor.execute("DELETE FROM `wishlist` WHERE `user_id` = 13")
#db.commit()
#print(cursor.rowcount, "was deleted")

#--------------------------------------------------------------------------------#
# TO INSERT INTO WISHLIST
#sql = "INSERT INTO wishlist (book_id, user_id, wishlist_id) VALUES (%s, %s, %s)"
#val = [
#    ("101", "11", "1"),
#    ("104", "13", "2"),
#    ("108", "12", "3"),
#]
#cursor.executemany(sql, val)
#db.commit()
#print(cursor.rowcount, "were or was inserted.")

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
