from flask import Flask
from ..config import Config

# Globally accessible libraries here


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('topstop_app.config.Config')

    # Initialize Plugins here

    with app.app_context():
        # Include application routes
        from . import controller
        return app
