import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os
from datetime import datetime

# Ajouter src au chemin pour les imports relatifs
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.controller.client_controller import add_client
from src.controller.room_controller import add_room, get_all_rooms
from src.controller.reservation_controller import (
    add_reservation,
    get_reservations_for_client,
    get_available_rooms
)


class AddClientForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ajouter un client")
        self.geometry("300x250")
        self.parent = parent
        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(self, text="Prénom:").pack(pady=5)
        self.first_name_entry = ttk.Entry(self)
        self.first_name_entry.pack()

        ttk.Label(self, text="Nom:").pack(pady=5)
        self.last_name_entry = ttk.Entry(self)
        self.last_name_entry.pack()

        ttk.Label(self, text="Email:").pack(pady=5)
        self.email_entry = ttk.Entry(self)
        self.email_entry.pack()

        ttk.Button(self, text="Ajouter", command=self._add_client).pack(pady=10)

    def _add_client(self):
        first = self.first_name_entry.get().strip()
        last = self.last_name_entry.get().strip()
        email = self.email_entry.get().strip()

        if not (first and last and email):
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires.")
            return

        client = add_client(first, last, email)
        messagebox.showinfo("Succès", f"Client ajouté avec l'ID : {client.id}")
        self.destroy()

class AddRoomForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ajouter une salle")
        self.geometry("300x300")
        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(self, text="ID de la salle:").pack(pady=5)
        self.id_entry = ttk.Entry(self)
        self.id_entry.pack()

        ttk.Label(self, text="Type de salle:").pack(pady=5)
        self.type_combo = ttk.Combobox(self, values=["standard", "conference", "informatique"])
        self.type_combo.pack()

        ttk.Label(self, text="Capacité:").pack(pady=5)
        self.capacity_spinbox = ttk.Spinbox(self, from_=1, to=20)
        self.capacity_spinbox.pack()

        ttk.Button(self, text="Ajouter", command=self._add_room).pack(pady=10)

    def _add_room(self):
        room_id = self.id_entry.get().strip()
        room_type = self.type_combo.get().strip()
        try:
            capacity = int(self.capacity_spinbox.get())
        except ValueError:
            messagebox.showerror("Erreur", "Capacité invalide.")
            return

        if not (room_id and room_type):
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires.")
            return

        try:
            room = add_room(room_id, room_type, capacity)
            messagebox.showinfo("Succès", f"Salle '{room.id}' ajoutée.")
            self.destroy()
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

class ViewRoomsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Salles réservables")
        self.geometry("400x300")
        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(self, text="Liste des salles disponibles", font=("Arial", 12)).pack(pady=10)
        self.tree = ttk.Treeview(self, columns=("ID", "Type", "Capacité"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Capacité", text="Capacité")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for room in get_all_rooms():
            self.tree.insert("", tk.END, values=(room.id, room.room_type, room.capacity))

class ViewClientReservations(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Réservations d'un client")
        self.geometry("500x350")
        self._create_widgets()

    def _create_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(pady=10, fill=tk.X)

        ttk.Label(frame, text="ID du client:").pack(side=tk.LEFT, padx=5)
        self.client_entry = ttk.Entry(frame)
        self.client_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        ttk.Button(frame, text="Rechercher", command=self._search).pack(side=tk.LEFT, padx=5)

        self.tree = ttk.Treeview(self, columns=("Salle", "Début", "Fin"), show="headings")
        self.tree.heading("Salle", text="Salle")
        self.tree.heading("Début", text="Début")
        self.tree.heading("Fin", text="Fin")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def _search(self):
        client_id = self.client_entry.get().strip()
        if not client_id:
            messagebox.showerror("Erreur", "Veuillez entrer un ID client.")
            return

        reservations = get_reservations_for_client(client_id)
        for item in self.tree.get_children():
            self.tree.delete(item)

        if not reservations:
            messagebox.showinfo("Info", "Aucune réservation trouvée pour ce client.")
            return

        for res in reservations:
            self.tree.insert("", tk.END, values=(res.room_id, res.start_datetime, res.end_datetime))

class ViewClientReservations(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Réservations d'un client")
        self.geometry("500x350")
        self._create_widgets()

    def _create_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(pady=10, fill=tk.X)

        ttk.Label(frame, text="ID du client:").pack(side=tk.LEFT, padx=5)
        self.client_entry = ttk.Entry(frame)
        self.client_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        ttk.Button(frame, text="Rechercher", command=self._search).pack(side=tk.LEFT, padx=5)

        self.tree = ttk.Treeview(self, columns=("Salle", "Début", "Fin"), show="headings")
        self.tree.heading("Salle", text="Salle")
        self.tree.heading("Début", text="Début")
        self.tree.heading("Fin", text="Fin")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def _search(self):
        client_id = self.client_entry.get().strip()
        if not client_id:
            messagebox.showerror("Erreur", "Veuillez entrer un ID client.")
            return

        reservations = get_reservations_for_client(client_id)
        for item in self.tree.get_children():
            self.tree.delete(item)

        if not reservations:
            messagebox.showinfo("Info", "Aucune réservation trouvée pour ce client.")
            return

        for res in reservations:
            self.tree.insert("", tk.END, values=(res.room_id, res.start_datetime, res.end_datetime))

class AvailableRoomsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Salles disponibles sur un créneau")
        self.geometry("500x350")
        self._create_widgets()

    def _create_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(pady=10, fill=tk.X)

        ttk.Label(frame, text="Début (YYYY-MM-DD HH:MM):").pack()
        self.start_entry = ttk.Entry(frame)
        self.start_entry.pack()

        ttk.Label(frame, text="Fin (YYYY-MM-DD HH:MM):").pack()
        self.end_entry = ttk.Entry(frame)
        self.end_entry.pack()

        ttk.Button(frame, text="Rechercher", command=self._search).pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("ID", "Type", "Capacité"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Capacité", text="Capacité")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def _search(self):
        try:
            start = datetime.strptime(self.start_entry.get().strip(), "%Y-%m-%d %H:%M")
            end = datetime.strptime(self.end_entry.get().strip(), "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Erreur", "Format de date/heure invalide.")
            return

        if end <= start:
            messagebox.showerror("Erreur", "La date de fin doit être postérieure à celle de début.")
            return

        available = get_available_rooms(get_all_rooms(), start, end)

        for item in self.tree.get_children():
            self.tree.delete(item)

        if not available:
            messagebox.showinfo("Aucune salle", "Aucune salle disponible sur ce créneau.")
        else:
            for room in available:
                self.tree.insert("", tk.END, values=(room.id, room.room_type, room.capacity))

class MakeReservationForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Réserver une salle")
        self.geometry("500x400")
        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(self, text="ID du client:").pack(pady=5)
        self.client_entry = ttk.Entry(self)
        self.client_entry.pack()

        ttk.Label(self, text="Début (YYYY-MM-DD HH:MM):").pack(pady=5)
        self.start_entry = ttk.Entry(self)
        self.start_entry.pack()

        ttk.Label(self, text="Fin (YYYY-MM-DD HH:MM):").pack(pady=5)
        self.end_entry = ttk.Entry(self)
        self.end_entry.pack()

        ttk.Button(self, text="Chercher les salles disponibles", command=self._search_rooms).pack(pady=10)

        self.rooms_combo = ttk.Combobox(self, state="readonly")
        self.rooms_combo.pack(pady=10)

        ttk.Button(self, text="Réserver", command=self._reserve).pack(pady=10)

    def _search_rooms(self):
        try:
            self.start = datetime.strptime(self.start_entry.get().strip(), "%Y-%m-%d %H:%M")
            self.end = datetime.strptime(self.end_entry.get().strip(), "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Erreur", "Format de date/heure invalide.")
            return

        if self.end <= self.start:
            messagebox.showerror("Erreur", "La date de fin doit être postérieure à celle de début.")
            return

        available = get_available_rooms(get_all_rooms(), self.start, self.end)

        if not available:
            messagebox.showinfo("Aucune salle", "Aucune salle disponible sur ce créneau.")
            self.rooms_combo['values'] = []
        else:
            self.rooms_combo['values'] = [room.id for room in available]
            self.rooms_combo.current(0)

    def _reserve(self):
        client_id = self.client_entry.get().strip()
        room_id = self.rooms_combo.get().strip()

        if not (client_id and room_id):
            messagebox.showerror("Erreur", "Veuillez renseigner tous les champs et sélectionner une salle.")
            return

        try:
            add_reservation(client_id, room_id, self.start, self.end)
            messagebox.showinfo("Succès", "Réservation effectuée avec succès.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", str(e))
