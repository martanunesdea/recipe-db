import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import init_db

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    db_path = 'mongodb+srv://cooluser:password12345@cluster0.sbchk.mongodb.net/recipe-db-test?retryWrites=true&w=majority'

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()