from dataclasses import dataclass

@dataclass
class Room:
    """
    Représente une salle de réunion chez MeetingPro.
    """
    id: str
    room_type: str  # 'standard', 'conference', 'informatique'
    capacity: int

    def to_dict(self) -> dict:
        """
        Convertit l'objet Room en dictionnaire pour sauvegarde JSON.
        """
        return {
            "id": self.id,
            "room_type": self.room_type,
            "capacity": self.capacity
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Crée un objet Room à partir d'un dictionnaire (lecture JSON).
        """
        return Room(
            id=data["id"],
            room_type=data["room_type"],
            capacity=data["capacity"]
        )
