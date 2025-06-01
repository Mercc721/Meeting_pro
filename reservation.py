from dataclasses import dataclass
from datetime import datetime

@dataclass
class Reservation:
    """
    Représente une réservation d'une salle par un client.
    """
    client_id: str
    room_id: str
    start_datetime: datetime
    end_datetime: datetime

    def to_dict(self) -> dict:
        """
        Convertit l'objet Reservation en dictionnaire pour sauvegarde JSON.
        """
        return {
            "client_id": self.client_id,
            "room_id": self.room_id,
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": self.end_datetime.isoformat()
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Crée un objet Reservation à partir d'un dictionnaire (lecture JSON).
        """
        return Reservation(
            client_id=data["client_id"],
            room_id=data["room_id"],
            start_datetime=datetime.fromisoformat(data["start_datetime"]),
            end_datetime=datetime.fromisoformat(data["end_datetime"])
        )
