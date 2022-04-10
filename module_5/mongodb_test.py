# Paul Caron
# 4-5-2022
# Module 5.2 Assignment

# import mongoclient from pymongo
from pymongo import MongoClient

# store mongoDB connection url in a variable named url
url = "mongodb+srv://admin:admin@cluster0.lk4hy.mongodb.net/students?retryWrites=true&w=majority"

# assign MongoClient(url) to variable client
client = MongoClient(url)

# set client.pytech to db
db = client.pytech

# print out what was stated for deliverables
print("-- Pytech COllection List --")

# print the required info from the server with an added filter
# to get all the gobbledygook out of what was supposed to be printed
print(db.list_collection_names(filter=None))

# makes the enter key exit the program
a = input("End of program, press Enter key to exit...")
if a:
    exit(0) 














