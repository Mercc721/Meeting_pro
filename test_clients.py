import os
import sys
import tempfile
import pytest

# Ajouter src au chemin d'import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.model.client import Client
from src.utils.db import load_db, save_db
from src.controller.client_controller import add_client


def test_client_creation():
    client = Client("Jean", "Dupont", "jean@exemple.com")
    assert client.first_name == "Jean"
    assert client.last_name == "Dupont"
    assert client.email == "jean@exemple.com"
    assert isinstance(client.id, str)


def test_client_serialization():
    original = Client("Marie", "Curie", "marie@exemple.com")
    data = original.to_dict()
    reconstructed = Client.from_dict(data)
    assert original == reconstructed


def test_add_client_persistence(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "clients.json")

        # Rediriger la constante de chemin vers le temporaire
        monkeypatch.setattr("src.controller.client_controller", "CLIENT_DB_PATH", path)

        client = add_client("Albert", "Einstein", "albert@exemple.com")
        clients = load_db(path)
        assert client.id in clients
        assert clients[client.id]["email"] == "albert@exemple.com"

