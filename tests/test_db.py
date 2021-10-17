import pytest
from flaskr import db

def test_get_recipe():
    response = db.db_get_recipes()
    print(response)
    assert "curry" in response
    assert "gnocchi" in response

def test_get_user():
    user = {"name": "test", "password": "test", "email": "test"}
    response = db.add_user(user)
    print(response)
    