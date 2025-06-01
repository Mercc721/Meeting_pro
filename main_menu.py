import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Ajouter src au chemin d'import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.view.forms import (
    AddClientForm,
    AddRoomForm,
    ViewRoomsWindow,
    ViewClientReservations,
    AvailableRoomsWindow,
    MakeReservationForm
)

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MeetingPro - Gestion des salles")
        self.geometry("500x400")
        self._create_widgets()

    def _create_widgets(self):
        label = ttk.Label(self, text="Menu Principal", font=("Arial", 16))
        label.pack(pady=20)

        buttons = [
            ("1. Ajouter un nouveau client", self._open_add_client_form),
            ("2. Ajouter une nouvelle salle", self._open_add_room_form),
            ("3. Afficher les salles réservables", self._open_show_rooms_form),
            ("4. Afficher les réservations pour un client", self._open_show_client_reservations),
            ("5. Vérifier la disponibilité d'une salle", self._open_check_availability),
            ("6. Afficher les salles disponibles", self._open_available_rooms),
            ("7. Réserver une salle", self._open_make_reservation)
        ]

        for text, command in buttons:
            b = ttk.Button(self, text=text, command=command)
            b.pack(pady=5, fill=tk.X, padx=50)

    def _open_add_client_form(self):
        AddClientForm(self)

    def _open_add_room_form(self):
        AddRoomForm(self)

    def _open_show_rooms_form(self):
        ViewRoomsWindow(self)

    def _open_show_client_reservations(self):
        ViewClientReservations(self)

    def _open_check_availability(self):
        CheckRoomAvailabilityForm(self)

        
    def _open_available_rooms(self):
        AvailableRoomsWindow(self)

    def _open_make_reservation(self):
        MakeReservationForm(self)


if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()
