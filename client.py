import uuid
from dataclasses import dataclass

@dataclass
class Client:
    """
    Représente un client de MeetingPro.
    """
    first_name: str
    last_name: str
    email: str
    id: str = None

    def __post_init__(self):
        if self.id is None:
            self.id = str(uuid.uuid4())

    def to_dict(self) -> dict:
        """
        Convertit l'objet Client en dictionnaire pour sauvegarde JSON.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "id": self.id
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Crée un objet Client à partir d'un dictionnaire (lecture JSON).
        """
        return Client(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            id=data["id"]
        )
