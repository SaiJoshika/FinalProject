import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_all_listings_successful(client):
    response = client.get('/listings')
    assert response.status_code == 200
    
def test_get_all_listings_failure(client):
    response = client.get('/listings')
    assert response.status_code == 200 
    assert 'error' not in response.json

def test_get_listing_by_id_success(client):
    listing_id = 323733
    response = client.get(f'/listings/{listing_id}')
    assert response.status_code == 200
    assert response.json is not None
    assert response.json['id'] == listing_id
   
def test_get_listing_by_id_not_found(client):
    listing_id = 999999 
    response = client.get(f'/listings/{listing_id}')
    assert response.status_code == 404
    assert response.json['error'] == 'Listing not found'

def test_filter_listings_success(client):
    response = client.get('/listings/filter?neighbourhood=78704&host_id=1798084&room_type=Entire home')
    assert response.status_code == 200
    assert response.json is not None
    assert isinstance(response.json, list)

def test_filter_listings_invalid_parameters_bad_request(client):
    response = client.get('/listings/filter?invalid_param=value')
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'Invalid query parameters'
