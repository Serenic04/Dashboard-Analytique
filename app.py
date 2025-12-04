"""
Application principale - Dashboard Analytique.
Architecture modulaire et propre.
"""
from flask import Flask
from config import DEBUG, TEMPLATE_DIR, STATIC_DIR
from backend.routes.dashboard import dashboard_bp
from backend.routes.api import api_bp


def create_app():
    """Factory function pour créer l'application Flask avec une architecture propre."""
    app = Flask(
        __name__,
        template_folder=str(TEMPLATE_DIR),
        static_folder=str(STATIC_DIR),
    )
    
    app.config['DEBUG'] = DEBUG
    
    # Enregistrement des blueprints pour une architecture modulaire
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(api_bp)
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=DEBUG)
