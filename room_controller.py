import sys
import os

# Ajouter le dossier parent de 'src' au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.model.room import Room
from src.utils.db import load_db, save_db

ROOM_DB_PATH = "rooms.json"

def add_room(room_id: str, room_type: str, capacity: int) -> Room:
    """
    Crée une nouvelle salle et l'ajoute à la base de données.
    L'identifiant de salle doit être unique.
    """
    rooms = load_db(ROOM_DB_PATH)
    if room_id in rooms:
        raise ValueError(f"La salle avec l'identifiant '{room_id}' existe déjà.")

    new_room = Room(id=room_id, room_type=room_type, capacity=capacity)
    rooms[room_id] = new_room.to_dict()
    save_db(ROOM_DB_PATH, rooms)
    return new_room

def get_all_rooms() -> list:
    """
    Retourne toutes les salles de la base de données.
    """
    rooms = load_db(ROOM_DB_PATH)
    return [Room.from_dict(data) for data in rooms.values()]
