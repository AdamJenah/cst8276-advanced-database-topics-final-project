import pytest
from app.models.game import Game

def test_game_to_dict():
    # Create a Game instance for testing
    game = Game("Test Game", "Action", 2022, "PC", "Mature", "admin")

    # Test the to_dict method
    result = game.to_dict()

    # Assertions
    assert result == {
        "title": "Test Game",
        "genre": "Action",
        "year_released": 2022,
        "platform": "PC",
        "ESRB_rating": "Mature",
        "admin": "admin"
    }
