import csv
from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/hello")
db=client["ImageMetaDB"]
collection = db["my_collection"]
print("MongoDB successfully connected")
with open("student.csv","r") as file:
    reader=csv.DictReader(file)
    data=list(reader)

collection.insert_many(data)

print("Metadata inserted successfully")