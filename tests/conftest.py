import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import init_app
from flask_pymongo import PyMongo

TEST_URI = 'mongodb+srv://cooluser:password12345@cluster0.sbchk.mongodb.net/recipe-db-test?retryWrites=true&w=majority'

@pytest.fixture
def app():

    app = create_app({
        "MONGOURI": TEST_URI,
    })

    with app.app_context():
        init_app(app)
        db = PyMongo(app, uri=app.config["URI"])

    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()