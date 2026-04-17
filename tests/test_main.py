import pytest
from app.main import app # Import your Flask app instance

@pytest.fixture
def client():
    # Set up a test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello from my Python App!' in response.data

def test_api_version(client):
    response = client.get('/api/version')
    assert response.status_code == 200
    assert response.get_json() == {'version': '1.0.0'}
