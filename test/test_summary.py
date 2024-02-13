import sys
from pathlib import Path

# Obtenez le chemin absolu du répertoire racine de votre projet
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
import pytest
from server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_show_summary_valid_client(client):
    # Simuler une requête POST valide avec l'email correct
    response = client.post('/showSummary', data={'email': 'john@simplylift.com'})

    # Vérifier que le code de statut de la réponse est 302 (redirection)
    assert response.status_code == 302

    # Ajouter d'autres assertions en fonction du comportement attendu de votre application


def test_show_summary_invalid_client(client):
    # Simuler une requête avec une adresse e-mail invalide
    response = client.post('/showSummary', data={'email': 'nonexistent@example.com'})

    # Vérifier que le code de statut de la réponse est 302 (redirection)
    assert response.status_code == 302

   


