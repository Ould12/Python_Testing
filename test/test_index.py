import pytest
from datetime import datetime
from server import app, load_clubs, load_competitions

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    # Chargement des clubs et des compétitions depuis le JSON
    competitions = load_competitions(datetime.strptime("2024-02-12 09:00:00", "%Y-%m-%d %H:%M:%S"))
    clubs = load_clubs()
    
    # Envoyer une demande GET à la route index
    response = client.get('/')

    # Vérification que le code de statut de la réponse est 200 (OK)
    assert response.status_code == 200

    # Vérification que la réponse contient les noms des compétitions et des clubs
    for competition in competitions:
        assert bytes(competition['name'], 'utf-8') in response.data
        assert bytes(str(competition['numberOfPlaces']), 'utf-8') in response.data  # Vérifie le nombre de places

    for club in clubs:
        assert bytes(club['name'], 'utf-8') in response.data
        assert bytes(club['email'], 'utf-8') in response.data  # Vérifie l'email du club
        assert bytes(str(club['points']), 'utf-8') in response.data  # Vérifie les points du club
