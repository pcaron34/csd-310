# Paul Caron
# 4/9/2022
# Module 5.3 Assignment

#import pymongo and friends
import pymongo
from pymongo import MongoClient

# next 3 lines connect to the database
cluster = MongoClient("mongodb+srv://admin:admin@cluster0.lk4hy.mongodb.net/students?retryWrites=true&w=majority")
db = cluster["pytech"]
collection = db["students"]

# test connection to database...uncomment to test and comment it back out when done
# print(db)

#print(collection)
#db.collection.find({"first_name": "Abigail"})
myquery = {"first_name": "Abigail"}
student_update = {"$set": {"first_name": "Abigale"}}

#snatch = db.collection.find_one_and_update({"first_name": "Abigail"}, {"$set": student_update})

snatch = db.collection.update_one(myquery, student_update)
print(student_update)