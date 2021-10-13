import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import init_app
TEST_URI = 'mongodb+srv://cooluser:password12345@cluster0.sbchk.mongodb.net/recipe-db-test?retryWrites=true&w=majority'

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        "MONGOURI": TEST_URI,
    })

    with app.app_context():
        init_app(app)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()