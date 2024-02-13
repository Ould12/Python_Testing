import pytest
from flask import Flask
from server import app
import sys
from pathlib import Path
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_purchasePlaces_valid_reservation(client):
    response = client.post('/purchasePlaces', data={'competition': 'Fall Classic', 'club': 'Simply Lift', 'places': '13'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Reservation reussie!' in response.data
    
# Test purchasePlaces route for edge cases
def test_purchasePlaces_edge_cases(client):
    # Test case where number of places equals 12
    response = client.post('/purchasePlaces', data={'competition': 'Fall Classic', 'club': 'Simply Lift', 'places': '12'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Reservation reussie!' in response.data

    # Test case where club has just enough points
    club = [c for c in club if c['name'] == 'Simply Lift'][0]
    club['points'] = 13
    response = client.post('/purchasePlaces', data={'competition': 'Fall Classic', 'club': 'Simply Lift', 'places': '13'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Reservation reussie!' in response.data

    # Test case where club has more than enough points
    club['points'] = 20
    response = client.post('/purchasePlaces', data={'competition': 'Fall Classic', 'club': 'Simply Lift', 'places': '13'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Reservation reussie!' in response.data

# Add more tests for other routes, edge cases, and validations

