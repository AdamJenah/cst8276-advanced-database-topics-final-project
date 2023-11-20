import pytest
from unittest.mock import MagicMock, patch
from app.views.game_view_controller import display_menu, add_game, main

def test_display_menu():
    with patch("builtins.input", return_value="1"):
        result = display_menu()
    assert result == "1"

# Similar tests for add_game, view_all_games, search_game, update_game, and delete_game functions

def test_add_game():
    controller_mock = MagicMock()
    input_values = ["Test Game", "Action", "2022", "PC", "Mature", "1", "admin", "password"]
    with patch("builtins.input", side_effect=input_values):
        add_game(controller_mock)
    controller_mock.add_game.assert_called_once_with("Test Game", ["Action"], 2022, ["PC"], "Mature", {"admin_id": 1, "username": "admin", "password": "password"})




