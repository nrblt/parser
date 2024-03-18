from pymongo import MongoClient
import json

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "test_task"
COLLECTION_NAME = "companies"

def get_mongo_client():
    return MongoClient(MONGO_URI)

def find_all_companies(client, query):
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    return collection.find(query, {"_id":0})

client = get_mongo_client()
query = {}
        
companies = list(find_all_companies(client,query))
json_data = json.dumps(companies, indent=4)

file_path = "data.json"
with open(file_path, 'w') as json_file:
    json_file.write(json_data)
