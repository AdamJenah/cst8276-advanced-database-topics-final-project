import pytest
from unittest.mock import MagicMock, patch
from app.models.database import get_database, create_database_if_not_exists
from pymongo import MongoClient

def test_get_database():
    # Mock MongoClient to avoid actual database connection
    with patch("app.models.database.MongoClient") as mongo_mock:
        # Raise an exception when the instance is called
        mongo_mock.side_effect = Exception("Mocked exception")
        with pytest.raises(Exception, match="Mocked exception"):
            get_database()


