######################################################################################
#                                                                                    #
#THIS IS NOT COMPLETE BUT I HAD TO SUBMIT SOMETHING BEFORE IT GOT TO LATE IN THE WEEK#
#                                                                                    # 
######################################################################################
# does what it says
import os
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
                insertIntoWishlist = ("INSERT INTO wishlist (user_id, book_id) VALUES (%s, %s)")
                # variables holding user id(which was gotten earlier) and book id
                data = (access, book_id)
                # database execute command
                cursor.execute(insertIntoWishlist, data)
                # commit to the database
                db.commit()
                # mama always said to be polite (read this in Forrest Gump's voice...lol)
                print("Thank you, enjoy your book")
                #pauses until user hits enter
                os.system('pause')
                acct_option = 3

                                
            elif acct_option == 3:
                acct_option()
            # prints out when user doesn't do something right
            else:
                print("Make sure you are entering information correctly.")
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




