"""
Service d'analyse des données.
Contient toute la logique de calcul des statistiques et indicateurs.
"""
import pandas as pd


def calculate_kpis(df: pd.DataFrame) -> dict:
    """Calcule les KPIs principaux."""
    return {
        "total_sessions": len(df),
        "avg_duration": round(float(df["duree_minutes"].mean()), 1),
        "avg_note": round(float(df["note_praticien"].mean()), 2),
        "avg_qualite": round(float(df["qualite_score"].mean()), 3),
        "avg_interactions": round(float(df["interactions_totales"].mean()), 1),
        "avg_interactions_patient": round(float(df["interactions_patient"].mean()), 1),
        "avg_interactions_praticien": round(float(df["interactions_praticien"].mean()), 1),
    }


def get_sessions_by_service(df: pd.DataFrame) -> list:
    """Retourne la répartition des sessions par service."""
    return (
        df.groupby("service", as_index=False)
        .agg({"session_id": "count", "duree_minutes": "mean"})
        .rename(columns={"session_id": "count", "duree_minutes": "avg_duration"})
        .sort_values("count", ascending=False)
        .to_dict(orient="records")
    )


def get_top_langues(df: pd.DataFrame, limit: int = 10) -> list:
    """Retourne le top des langues les plus utilisées."""
    return (
        df.groupby("langue", as_index=False)
        .agg({"session_id": "count"})
        .rename(columns={"session_id": "count"})
        .sort_values("count", ascending=False)
        .head(limit)
        .to_dict(orient="records")
    )


def get_time_series(df: pd.DataFrame) -> list:
    """Retourne l'évolution temporelle des sessions."""
    if "date" not in df.columns or df["date"].notna().sum() == 0:
        return []
    
    df_copy = df.copy()
    df_copy["month"] = df_copy["date"].dt.to_period("M").astype(str)
    return (
        df_copy.groupby("month", as_index=False)
        .agg({"session_id": "count"})
        .rename(columns={"session_id": "count"})
        .sort_values("month")
        .to_dict(orient="records")
    )


def get_notes_distribution(df: pd.DataFrame) -> list:
    """Retourne la distribution des notes par tranches."""
    if "note_praticien" not in df.columns:
        return []
    
    df_copy = df.copy()
    df_copy["note_range"] = pd.cut(
        df_copy["note_praticien"],
        bins=[0, 2, 3, 4, 4.5, 5, 6],
        labels=["0-2", "2-3", "3-4", "4-4.5", "4.5-5", "5+"],
        include_lowest=True,
    )
    return (
        df_copy.groupby("note_range", as_index=False)
        .agg({"session_id": "count"})
        .rename(columns={"session_id": "count"})
        .to_dict(orient="records")
    )


def get_duration_by_service(df: pd.DataFrame) -> list:
    """Retourne la durée moyenne par service."""
    return (
        df.groupby("service", as_index=False)
        .agg({"duree_minutes": "mean"})
        .rename(columns={"duree_minutes": "avg_duration"})
        .sort_values("avg_duration", ascending=False)
        .to_dict(orient="records")
    )


def get_qualite_indicators(df: pd.DataFrame) -> dict:
    """Retourne les indicateurs de qualité."""
    return {
        "avg_qualite_score": round(float(df["qualite_score"].mean()), 3),
        "min_qualite_score": round(float(df["qualite_score"].min()), 3),
        "max_qualite_score": round(float(df["qualite_score"].max()), 3),
        "avg_segments_non_reconnus": round(float(df["segments_non_reconnus"].mean()), 1) if "segments_non_reconnus" in df.columns else 0,
        "sessions_haute_qualite": int(len(df[df["qualite_score"] >= 0.9])),
        "sessions_basse_qualite": int(len(df[df["qualite_score"] < 0.8])),
    }


def get_interactions_breakdown(df: pd.DataFrame) -> dict:
    """Retourne le détail des interactions."""
    return {
        "avg_patient": round(float(df["interactions_patient"].mean()), 1),
        "avg_praticien": round(float(df["interactions_praticien"].mean()), 1),
        "avg_totales": round(float(df["interactions_totales"].mean()), 1),
    }


def get_filter_options(df: pd.DataFrame) -> dict:
    """Retourne les options disponibles pour les filtres."""
    result = {
        "services": sorted(df["service"].unique().tolist()),
        "langues": sorted(df["langue"].unique().tolist()),
        "devices": sorted(df["device"].unique().tolist()),
        "date_min": None,
        "date_max": None,
    }
    
    if "date" in df.columns and df["date"].notna().any():
        result["date_min"] = df["date"].min().strftime("%Y-%m-%d")
        result["date_max"] = df["date"].max().strftime("%Y-%m-%d")
    
    return result


def calculate_all_stats(df: pd.DataFrame) -> dict:
    """Calcule toutes les statistiques nécessaires pour le dashboard."""
    if len(df) == 0:
        return {
            "kpis": {
                "total_sessions": 0,
                "avg_duration": 0,
                "avg_note": 0,
                "avg_qualite": 0,
                "avg_interactions": 0,
                "avg_interactions_patient": 0,
                "avg_interactions_praticien": 0,
            },
            "sessions_by_service": [],
            "top_langues": [],
            "time_series": [],
            "notes_distribution": [],
            "duration_by_service": [],
            "qualite_indicators": {},
            "interactions_breakdown": {},
        }
    
    return {
        "kpis": calculate_kpis(df),
        "sessions_by_service": get_sessions_by_service(df),
        "top_langues": get_top_langues(df),
        "time_series": get_time_series(df),
        "notes_distribution": get_notes_distribution(df),
        "duration_by_service": get_duration_by_service(df),
        "qualite_indicators": get_qualite_indicators(df),
        "interactions_breakdown": get_interactions_breakdown(df),
    }

