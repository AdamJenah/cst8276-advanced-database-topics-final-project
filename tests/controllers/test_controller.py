import pytest
from unittest.mock import MagicMock
from app.controllers.controller import GameController

@pytest.fixture
def game_controller():
    return GameController()

def test_add_game(game_controller):
    # Mock the database and collection
    game_controller.db = MagicMock()
    game_controller.collection = game_controller.db.games

    # Mock the insert_one method
    game_controller.collection.insert_one = MagicMock(return_value="mock_insert_result")

    # Test the add_game method
    result = game_controller.add_game("Test Game", "Action", 2022, "PC", "Mature", "admin")

    # Assertions
    assert result == "mock_insert_result"
    game_controller.collection.insert_one.assert_called_once()

def test_get_all_games(game_controller):
    # Mock the collection
    game_controller.collection = MagicMock()
    game_controller.collection.find.return_value = ["game1", "game2", "game3"]

    # Test the get_all_games method
    result = game_controller.get_all_games()

    # Assertions
    assert result == ["game1", "game2", "game3"]
    game_controller.collection.find.assert_called_once_with({})

# Similar tests for get_game_by_title, update_game, and delete_game methods
