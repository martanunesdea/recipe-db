import pytest
from flaskr import db

def test_get_recipe():
    response = db.db_get_all()
    print(response)
    assert "curry" in response
    assert "gnocchi" in response

def test_get_user():
    response = db.register_user({"name": "test", "password": "test", "email": "test"})
    print(response)
    