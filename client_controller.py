import sys
import os

# Ajouter le dossier parent de 'src' au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.model.client import Client
from src.utils.db import load_db, save_db

CLIENT_DB_PATH = "clients.json"

def add_client(first_name: str, last_name: str, email: str) -> Client:
    """
    Crée un nouveau client et l'ajoute à la base de données.
    """
    clients = load_db(CLIENT_DB_PATH)
    new_client = Client(first_name=first_name, last_name=last_name, email=email)
    clients[new_client.id] = new_client.to_dict()
    save_db(CLIENT_DB_PATH, clients)
    return new_client

def get_all_clients() -> list:
    """
    Retourne tous les clients de la base de données.
    """
    clients = load_db(CLIENT_DB_PATH)
    return [Client.from_dict(data) for data in clients.values()]
