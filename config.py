"""
Configuration de l'application Dashboard Analytique.
"""
from pathlib import Path

# Chemins de base
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
TEMPLATE_DIR = BASE_DIR / "frontend" / "templates"
STATIC_DIR = BASE_DIR / "frontend" / "static"

# Configuration Flask
DEBUG = True
SECRET_KEY = "dev-secret-key-change-in-production"

# Configuration des données
REQUIRED_COLUMNS = [
    "session_id",
    "service",
    "langue",
    "duree_minutes",
    "interactions_patient",
    "interactions_praticien",
    "interactions_totales",
    "note_praticien",
    "qualite_score",
    "device",
]

