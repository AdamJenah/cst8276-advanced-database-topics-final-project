from pymongo import MongoClient


def get_database():
    # Placeholder for database connection
    client = MongoClient("mongodb://localhost:27017/")
    return client['video_games']


def create_database_if_not_exists():
    client = MongoClient("mongodb://localhost:27017/")
    if 'video_games' not in client.list_database_names():
        print("Creating 'video_games' database...")
        client['video_games']  # This line accesses the database, effectively creating it
