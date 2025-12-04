"""
Routes API pour le dashboard.
"""
from flask import Blueprint, jsonify

from backend.services.data_service import load_data
from backend.services.analytics_service import calculate_all_stats, get_filter_options
from backend.utils.filters import apply_filters

# Création du Blueprint pour les routes API
api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/filters')
def get_filters():
    """Retourne les options disponibles pour les filtres."""
    try:
        df = load_data()
        return jsonify(get_filter_options(df))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_bp.route('/stats')
def get_stats():
    """Endpoint principal pour les statistiques avec support des filtres."""
    try:
        df = load_data()
        filtered_df = apply_filters(df)
        stats = calculate_all_stats(filtered_df)
        return jsonify(stats)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

