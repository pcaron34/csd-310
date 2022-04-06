from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.lk4hy.mongodb.net/students?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print("-- Pytech COllection List --")
print(db.list_collection_names(filter=None))

a = input("End of program, press Enter key to exit...")
if a:
    exit(0) 




