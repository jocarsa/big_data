#pip install pymongo
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")  
db = client["empresa"]  
collection = db["clientes"]  
documents = collection.find()
for document in documents:
    print(document)
client.close()
