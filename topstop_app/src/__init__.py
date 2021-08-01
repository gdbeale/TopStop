from flask import Flask
from ..config import Config, ProdConfig, DevConfig

# Globally accessible libraries here


def create_app(config_class=None):
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_class)

    # Initialize Plugins here

    with app.app_context():
        # Include application routes
        from . import controller
        return app
