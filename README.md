# MeetingPro - Gestion de Réservations de Salles

## Description

MeetingPro est une application Python avec interface graphique développée avec `tkinter`, permettant de gérer efficacement les clients, les salles et leurs réservations.
Elle offre une interface intuitive pour enregistrer des clients, ajouter des salles, vérifier les disponibilités, et réserver des créneaux.

## Architecture du Projet

```
projet_python/
│
├── src/
│   ├── controller/         # Logique applicative (client, salle, réservation)
│   ├── model/              # Structures de données (Client, Room, Reservation)
│   ├── utils/              # Fonctions utilitaires (accès JSON, vérifications)
│   └── view/               # Interfaces tkinter (menus et formulaires)
│
├── tests/                 # Tests unitaires avec pytest
│
├── data/                  # Fichiers de base de données JSON générés à l'exécution
│
└── README.md              # Documentation du projet
```

## Fonctionnalités principales

* Ajouter un **client** avec prénom, nom, email
* Ajouter une **salle** avec identifiant, type, capacité
* Visualiser toutes les salles
* Afficher les réservations d’un client
* Vérifier la disponibilité d’une salle
* Afficher les salles disponibles dans un créneau donné
* Réserver une salle (créneau minimum : 30 minutes)

## Interface utilisateur (Tkinter)

Le fichier principal est `main_menu.py`, situé dans `src/view/`. Il permet de naviguer entre les différentes fonctionnalités via un menu.

## Tests

Des tests unitaires ont été implémentés avec `pytest` :

* `tests/test_clients.py`
* `tests/test_rooms.py`
* `tests/test_reservations.py`

### Lancer les tests

Assurez-vous que `pytest` est installé :

```bash
pip install pytest
```

Puis exécutez :

```bash
pytest tests/
```

## Installation et Exécution

1. Cloner ou télécharger le projet
2. Naviguer dans le répertoire :

```bash
cd projet_python
```

3. Lancer l'application :

```bash
python src/view/main_menu.py
```

## Données

Les données sont enregistrées automatiquement dans des fichiers JSON :

* `clients.json`
* `rooms.json`
* `reservations.json`

Ils sont stockés dans le dossier `data/` (par défaut, ou dans le dossier racine).

## Dépendances

* Bibliothèques standards : `tkinter`, `uuid`, `json`, `datetime`, `os`, `sys`

## Auteurs

* **Emre BAYLAN** **Aymane EL JAOUDI** 

---

Ce projet suit une architecture MVC simplifiée avec tests unitaires et une interface graphique modulaire.
