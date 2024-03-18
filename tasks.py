from celery import Celery
from parse_company import parse
import pymongo

app = Celery('tasks', broker='amqp://nurbo:nurbo@localhost:5672/myvhost')


def insert_into_mongo(data):
    MONGO_URI = "mongodb://localhost:27017/"
    DB_NAME = "test_task"
    COLLECTION_NAME = "companies"
    client = pymongo.MongoClient(MONGO_URI)

    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    collection.insert_one(data)

@app.task(queue='companies_queue')
def retrieve_company_info(company):
    data = parse(company)
    insert_into_mongo(data)

def add_to_queue(company_list):
    for company_id in company_list:
        # app.send_task('celery.accumulate', args=[company_id], queue='companies_queue')
        retrieve_company_info.apply_async((company_id,),
                                        queue='companies_queue')
