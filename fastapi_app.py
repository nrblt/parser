from fastapi import FastAPI, Query, Response
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import json
from bson import json_util

app = FastAPI()

# MongoDB connection details
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "test_task"
COLLECTION_NAME = "companies"

def get_mongo_client():
    return MongoClient(MONGO_URI)

def find_all_companies(client, query):
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    return collection.find(query, {"_id":0})

@app.get("/companies", tags=["companies"])
def get_all_companies(response: Response, name: str = None, organizational_and_legal_form: str = None):
    try:
        client = get_mongo_client()
        query = {}
        if name:
            query["name"] = {"$regex": name, "$options": "i"}
        if organizational_and_legal_form:
            query["organizational_and_legal_form"] = {"$regex": organizational_and_legal_form, "$options": "i"}
        companies = list(find_all_companies(client,query))
        return companies
    except Exception as e:
        response.status_code = 500
        return {"error": str(e)}
    finally:
        client.close()
