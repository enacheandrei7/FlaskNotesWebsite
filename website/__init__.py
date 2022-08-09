# When we put __init__.py in a folder, it becomes a python package and we can import elements from it

from flask import Flask

# Creating the main app


def create_app():
    # Default initialization
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdasdas'

    # Import the blueprints
    from .views import views
    from .auth import auth

    # Register the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
