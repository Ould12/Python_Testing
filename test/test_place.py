import sys,json
from pathlib import Path
import pytest
from flask import Flask, render_template, request, flash, get_flashed_messages
from server import app, load_clubs, load_competitions


project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))


# Test routes
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test loadClubs function
def test_load_clubs():
    clubs = load_clubs()
    assert isinstance(clubs, list)
    assert all(isinstance(club, dict) for club in clubs)
    


# Test loadCompetitions function
def test_load_competitions():
    competitions = load_competitions()
    assert isinstance(competitions, list)
    assert all(isinstance(competition, dict) for competition in competitions)



def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    # Add more assertions to check the content of the response if necessary





def test_purchasePlaces(client):
    data = {
        'competition': 'Spring Festival',
        'club': 'Iron Temple',
        'places': '25'
    }
    competitions = [{"name": "Spring Festival", "numberOfPlaces": 100}]  # Replace with your test data
    clubs = [{"name": "Iron Temple", "points": 50}]  # Replace with your test data
    response = client.post('/purchasePlaces', data=data)
    competition_name = data['competition']
    club_name = data['club']
    competition = next((c for c in competitions if c['name'] == competition_name), None)
    club = next((c for c in clubs if c['name'] == club_name), None)
    with client.session_transaction() as session:
        flashed_messages = get_flashed_messages()
        print(flashed_messages)