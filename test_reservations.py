import os
import sys
import tempfile
from datetime import datetime, timedelta
import pytest

# Ajouter src au chemin d'import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.controller.reservation_controller import (
    add_reservation,
    get_all_reservations,
    is_room_available
)
from src.utils.db import load_db


def test_add_and_load_reservation(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "reservations.json")
        monkeypatch.setattr("src.controller.reservation_controller", "RESERVATION_DB_PATH", path)

        start = datetime.now()
        end = start + timedelta(hours=1)
        reservation = add_reservation("client123", "roomA", start, end)

        reservations = load_db(path)
        assert len(reservations) == 1
        key = list(reservations.keys())[0]
        assert reservations[key]["client_id"] == "client123"
        assert reservations[key]["room_id"] == "roomA"


def test_is_room_available(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "reservations.json")
        monkeypatch.setattr("src.controller.reservation_controller", "RESERVATION_DB_PATH", path)

        start = datetime(2025, 1, 1, 9, 0)
        end = datetime(2025, 1, 1, 10, 0)
        add_reservation("clientX", "roomY", start, end)

        assert not is_room_available("roomY", datetime(2025, 1, 1, 9, 30), datetime(2025, 1, 1, 10, 30))
        assert is_room_available("roomY", datetime(2025, 1, 1, 10, 0), datetime(2025, 1, 1, 11, 0))
