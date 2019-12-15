import pytest
from app import create_app

@pytest.fixture
def client():
    yield create_app()




def test_one(client):
    assert client