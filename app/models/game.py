class Game:
    def __init__(self, title, genre, year_released, platform, ESRB_rating, admin):
        self.title = title
        self.genre = genre
        self.year_released = year_released
        self.platform = platform
        self.ESRB_rating = ESRB_rating
        self.admin = admin

    def to_dict(self):
        return {
            "title": self.title,
            "genre": self.genre,
            "year_released": self.year_released,
            "platform": self.platform,
            "ESRB_rating": self.ESRB_rating,
            "admin": self.admin
        }