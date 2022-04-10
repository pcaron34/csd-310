# Paul Caron
# 4/9/2022
# Module 5.3 Assignment
# I was not sure what the "Modeling assignment" is that you were talking about in the directions, I am assuming it was the example code
# above the instructions so I did the best I could. Before attempting anymore assignments I will have to get more clarification about
# what you are asking for because I felt I was just guessing. Hopefully I don't lose too many points for not including anything I missed.
# 
# If the database doesn't have an entry in it, any new students that are entered will be entered into the database
# with what I have below but if the program is run again it will show errors in the return message; I didn't know what you were looking
# for when it came to that. This part works like a charm if it is a new entry though, so there is that at least.
# 

import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://admin:admin@cluster0.lk4hy.mongodb.net/students?retryWrites=true&w=majority")
db = cluster["pytech"]
collection = db["students"]


#doc = {"_id": 1007, "student_id": 1007, "first_name": "Abigail", "last_name": "Adams"}
#doc = {"_id": 1008, "student_id": 1008, "first_name": "Patrick", "last_name": "Henry"}
#doc = {"_id": 1009, "student_id": 1009, "first_name": "Alexander", "last_name": "Hamilton"}

cursor = db.collection.find({})

#The next one isn't in the database so when "pytech_insert.py" ran it will insert George
#Washington just so you could see it works without having to delete a person from the database

doc = {"_id": 1010, "student_id": 1010, "first_name": "George", "last_name": "Washington"}

collection.insert_one(doc)

#new_student_Id = students.insert_one(doc).inserted_id

print("-- INSERTED STATEMENTS --")
print(cursor)
print("Inserted student record " + doc["first_name"] + " " + doc["last_name"] + " into the students collection with document_id " + str(doc["student_id"]))
print("End of program, press any key to exit...")
