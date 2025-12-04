"""
Utilitaires pour l'application de filtres aux données.
"""
from flask import request
import pandas as pd


def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applique les filtres de la requête HTTP au DataFrame.
    
    Args:
        df: DataFrame pandas à filtrer
        
    Returns:
        DataFrame filtré
    """
    filtered_df = df.copy()
    
    # Filtre par service
    if request.args.get("service") and request.args.get("service") != "all":
        filtered_df = filtered_df[filtered_df["service"] == request.args.get("service")]
    
    # Filtre par langue
    if request.args.get("langue") and request.args.get("langue") != "all":
        filtered_df = filtered_df[filtered_df["langue"] == request.args.get("langue")]
    
    # Filtre par device
    if request.args.get("device") and request.args.get("device") != "all":
        filtered_df = filtered_df[filtered_df["device"] == request.args.get("device")]
    
    # Filtre par date (début)
    if request.args.get("date_debut"):
        try:
            date_debut = pd.to_datetime(request.args.get("date_debut"))
            filtered_df = filtered_df[filtered_df["date"] >= date_debut]
        except:
            pass
    
    # Filtre par date (fin)
    if request.args.get("date_fin"):
        try:
            date_fin = pd.to_datetime(request.args.get("date_fin"))
            filtered_df = filtered_df[filtered_df["date"] <= date_fin]
        except:
            pass
    
    return filtered_df

