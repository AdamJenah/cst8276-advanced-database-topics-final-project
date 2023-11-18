import pymongo
import json


class Connection:
    def __init__(self):
        pass

    client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client["catalogue"]
    collection = db["video_games"]

    # Add try-catch for searching for the database
    # Add try-catch for searching for collection(s)
    f = open('dumby_data.json')
    data = json.load(f)  # pass in param

    x = collection.insert_many(data)  # for inserting the data into the collection
