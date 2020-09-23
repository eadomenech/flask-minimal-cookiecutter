import pytest
from application import create_app

@pytest.fixture
def app():
    yield create_app('config.TestConfig')

@pytest.fixture
def client(app):

    with app.test_client() as client:
        yield client
