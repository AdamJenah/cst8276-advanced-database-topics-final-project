from pymongo import MongoClient


def get_database():
    # Placeholder for database connection
    client = MongoClient("mongodb://localhost:27017/")
    return client['video_games']
