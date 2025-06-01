import sys
import os
from datetime import datetime

# Ajouter le dossier parent de 'src' au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.model.reservation import Reservation
from src.utils.db import load_db, save_db

RESERVATION_DB_PATH = "reservations.json"

def add_reservation(client_id: str, room_id: str, start: datetime, end: datetime) -> Reservation:
    """
    Ajoute une réservation à la base de données.
    """
    reservations = load_db(RESERVATION_DB_PATH)
    new_reservation = Reservation(client_id=client_id, room_id=room_id, start_datetime=start, end_datetime=end)
    reservation_id = f"{client_id}_{room_id}_{start.isoformat()}"
    reservations[reservation_id] = new_reservation.to_dict()
    save_db(RESERVATION_DB_PATH, reservations)
    return new_reservation

def get_all_reservations() -> list:
    """
    Récupère toutes les réservations.
    """
    reservations = load_db(RESERVATION_DB_PATH)
    return [Reservation.from_dict(data) for data in reservations.values()]

def get_reservations_for_client(client_id: str) -> list:
    """
    Retourne toutes les réservations effectuées par un client donné.
    """
    return [r for r in get_all_reservations() if r.client_id == client_id]

def is_room_available(room_id: str, start: datetime, end: datetime) -> bool:
    """
    Vérifie si une salle est disponible pendant un créneau donné.
    """
    for res in get_all_reservations():
        if res.room_id == room_id:
            if not (end <= res.start_datetime or start >= res.end_datetime):
                return False
    return True

def get_available_rooms(rooms: list, start: datetime, end: datetime) -> list:
    """
    Retourne la liste des salles disponibles pour un créneau donné.
    """
    return [room for room in rooms if is_room_available(room.id, start, end)]
