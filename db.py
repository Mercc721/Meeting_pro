import json
import os
from typing import Any

def load_db(path: str) -> dict:
    """
    Charge les données depuis un fichier JSON.
    Retourne un dictionnaire vide si le fichier n'existe pas.
    """
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_db(path: str, data: Any) -> None:
    """
    Sauvegarde les données dans un fichier JSON.
    """
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def append_to_db(path: str, entry: dict, key: str) -> None:
    """
    Ajoute une nouvelle entrée à un fichier JSON contenant un dictionnaire.
    """
    db = load_db(path)
    db[key] = entry
    save_db(path, db)
