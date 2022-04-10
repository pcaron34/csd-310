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
doc1 = db.students.find_one()

print(doc1)
print()
print()

print("-- DISPLAYING STUDENT DOCUMENT FROM find() QUERY")
doc = db.students.find()

for doc in doc:
    print(doc)
    
print()
print()

print("End of program, press any key to continue...")



