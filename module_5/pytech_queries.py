# Paul Caron
# 4/9/2022
# Module 5.3 Assignment

import os
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://admin:admin@cluster0.lk4hy.mongodb.net/students?retryWrites=true&w=majority")
db = cluster["pytech"]
collection = db["students"]

print("-- DISPLAYING STUDENT DOCUMENTS FROM find_one() QUERY --")
snatch = db.students.find_one()

print(snatch)
print()
print()

print("-- DISPLAYING STUDENT DOCUMENT FROM find() QUERY")
snatch = db.students.find()

for snatch in snatch:
    print(snatch)
    
print()
print()

print("-- DISPLAYING STUDENT DOCUMENTS FROM find_one() QUERY --")
snatch = db.students.find_one()


print("End of program, press any key to continue...")



