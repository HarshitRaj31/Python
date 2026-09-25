import json
from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/hello")
db=client["Json"]
collection=db["my_collections"]
print("Connection starts")
with open("product.json","r") as file:
     data=json.load(file)

collection.insert_one(data)    

for i in collection.find():
     print(i)

print("connection ends")


