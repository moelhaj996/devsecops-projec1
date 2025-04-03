import json
import pytest
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'message' in data

def test_data_route(client):
    response = client.get('/api/data')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'data' in data

def test_echo_route_valid(client):
    response = client.post('/api/echo', 
                          json={'message': 'test message'},
                          content_type='application/json')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['echo'] == 'test message'

def test_echo_route_invalid(client):
    response = client.post('/api/echo', 
                          json={'wrong_key': 'test message'},
                          content_type='application/json')
    assert response.status_code == 400