import pytest
from flask import g, session
from app.db import get_db


def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a', 'email': 'test'}
    )
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM users WHERE username = 'a'",
        ).fetchone() is not None


"""
@pytest.mark.parametrize(('username', 'password', 'email', 'message'), (
    ('', '', '', b'Username is required.'),
    ('a', '', '', b'Password is required.'),
    ('test', 'test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, email, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password, 'email': email}
    )
    assert message in response.data
"""

def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"

    with client:
        client.get('/')
        id = session.get('user_id')
        assert id != 0
        #assert g.user is not None

"""
@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Something went wrong'),
    ('test', 'a', b'Something went wrong'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data
"""

def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session
