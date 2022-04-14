# Paul Caron
# 4/12/2022
# Module 6.2 Assignment

#import pymongo and friends
import pymongo
from pymongo import MongoClient

# next 3 lines connect to the database
cluster = MongoClient("mongodb+srv://admin:admin@cluster0.lk4hy.mongodb.net/students?retryWrites=true&w=majority")
db = cluster["pytech"]
collection = db["students"]

print()

print("-- DISPLAYING STUDENT DOCUMENT FROM find() QUERY")
snatch = db.students.find()

for snatch in snatch:
    print(snatch)
print()
print()
# test connection to database...uncomment to test and comment it back out when done
# print(db)
print("-- DISPLAYING STUDENT DOCUMENTS FROM update_one() QUERY --")
# print(collection) # prints out all the gobblygook

#>>>>>> = {"first_name": "updating this"}
myquery = {"first_name": "Abigale"}

snatch = collection.update_one(myquery, {"$set":{"first_name": "Abigail"}})

#snatch = collection.update_many(myquery, {"$set":{"": ""}})

print(snatch.modified_count, "documents updated.")
print()
print()
print("-- DISPLAYING STUDENT DOCUMENTS FROM find_one() QUERY --")
snatch = db.students.find_one()

print(snatch)

print()
print()

print("End of program, no need to press any key to continue...")