from flaskr import create_app


def test_config():
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/')
    assert not response.data == "Hello, World!"