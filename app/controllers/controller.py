from app.models.database import get_database
from app.models.game import Game


class GameController:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.games  # Assuming the collection is named 'games'

    def add_game(self, title, genre, year_released, platform, ESRB_rating, admin):
        new_game = Game(title, genre, year_released, platform, ESRB_rating, admin)
        return self.collection.insert_one(new_game.to_dict())

    def get_all_games(self):
        return list(self.collection.find({}))

    def get_game_by_title(self, title):
        return self.collection.find_one({"title": title})

    def update_game(self, title, update_data):
        return self.collection.update_one({"title": title}, {"$set": update_data})

    def delete_game(self, title):
        return self.collection.delete_one({"title": title})
