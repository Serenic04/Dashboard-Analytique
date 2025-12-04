"""
Routes pour le dashboard.
"""
from flask import Blueprint, render_template

# Création du Blueprint pour les routes du dashboard
dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/')
def index():
    """Page principale du dashboard."""
    return render_template('dashboard.html')

