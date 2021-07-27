# Entry point for the application.
from . import app    # For application discovery by the 'flask' command.
from .src import views  # For import side-effects of setting up routes.
