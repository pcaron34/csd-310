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

snatch = db.collection.update_one({"first_name": "Abigail"},{set:{"age": "Deceased"}})
print(snatch)