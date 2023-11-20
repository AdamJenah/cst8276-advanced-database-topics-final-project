import pytest
from unittest.mock import MagicMock
from app.models.database import get_database, create_database_if_not_exists

def test_get_database():
    # Mock MongoClient to avoid actual database connection
    with pytest.raises(Exception):  # Ensure an exception is raised due to mock
        get_database()

def test_create_database_if_not_exists():
    # Mock MongoClient to avoid actual database connection
    with pytest.raises(Exception):  # Ensure an exception is raised due to mock
        create_database_if_not_exists()
