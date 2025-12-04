"""
Service de gestion des données.
Charge et gère le cache des données CSV.
"""
from pathlib import Path
import pandas as pd
from config import DATA_DIR, REQUIRED_COLUMNS

# Cache pour les données chargées
_data_cache = None


def load_data() -> pd.DataFrame:
    """
    Charge le fichier CSV présent dans le dossier `data`.
    - Utilise le premier fichier *.csv trouvé dans `data`
    - Parse les dates pour faciliter l'analyse temporelle
    - Gestion d'erreurs améliorée
    - Mise en cache pour améliorer les performances
    """
    global _data_cache
    
    if _data_cache is not None:
        return _data_cache.copy()
    
    if not DATA_DIR.exists():
        raise FileNotFoundError(f"Le dossier data est introuvable : {DATA_DIR}")

    csv_files = list(DATA_DIR.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"Aucun fichier CSV trouvé dans {DATA_DIR}")

    csv_path = csv_files[0]
    try:
        df = pd.read_csv(csv_path)
        
        # Parser la colonne date si elle existe
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"], errors="coerce")
        
        # S'assurer que toutes les colonnes nécessaires existent
        missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        if missing:
            raise ValueError(f"Colonnes manquantes dans le CSV : {', '.join(missing)}")
        
        _data_cache = df.copy()
        return df
    except Exception as e:
        raise RuntimeError(f"Erreur lors du chargement du fichier CSV : {str(e)}")


def clear_cache():
    """Réinitialise le cache des données."""
    global _data_cache
    _data_cache = None

