import os
import sys
import tempfile
import pytest

# Ajouter src au chemin d'import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.model.room import Room
from src.utils.db import load_db
from src.controller.room_controller import add_room


def test_room_creation():
    room = Room("R101", "conference", 8)
    assert room.id == "R101"
    assert room.room_type == "conference"
    assert room.capacity == 8


def test_room_serialization():
    original = Room("R202", "standard", 4)
    data = original.to_dict()
    reconstructed = Room.from_dict(data)
    assert original == reconstructed


def test_add_room_persistence(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "rooms.json")

        monkeypatch.setattr("src.controller.room_controller", "ROOM_DB_PATH", path)

        room = add_room("R303", "informatique", 3)
        rooms = load_db(path)
        assert room.id in rooms
        assert rooms[room.id]["capacity"] == 3
