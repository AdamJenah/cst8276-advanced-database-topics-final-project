from pymongo import MongoClient


class Database:
    def __init__(self):
        self.records = []

    def get_database(self):
        client = MongoClient()
        return client['video_games']

    def create_database_if_not_exists(self):
        client = MongoClient("mongodb://localhost:27017/")
        if 'video_games' not in client.list_database_names():
            print("Creating 'video_games' database...")
            client['video_games']
