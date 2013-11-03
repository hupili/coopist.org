import pymongo
from pymongo import MongoClient

#client = MongoClient()
mongo_client = MongoClient('127.0.0.1', 27017)
#status_list = mongo_client.twitter.status_list
#status_list.create_index([('time', pymongo.DESCENDING)])

if __name__ == '__main__':
    print status_list.find().count()

