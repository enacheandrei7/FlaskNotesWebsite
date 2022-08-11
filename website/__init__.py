# When we put __init__.py in a folder, it becomes a python package and we can import elements from it

from genericpath import exists
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize the db
db = SQLAlchemy()
DB_NAME = "database.db"

# Creating the main app
def create_app():
    # Default initialization
    app = Flask(__name__)
    # The secret key is chosen by us, whatever we want
    app.config['SECRET_KEY'] = 'asdasdas'
    # The SQLAlchemy db is stored at sqlite:///DB_NAME
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Import the blueprints
    from .views import views
    from .auth import auth

    # Register the blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # here we check if there has been created a db before running the website
    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    # Here we specify where we should redirect the user if he's not logged in
    login_manager.login_view = 'auth.login'
    # Here we tell the login manager which app we're using
    login_manager.init_app(app)

    # Here we tell Flask how to load an user
    @login_manager.user_loader
    def load_user(id):
        # Here it checks if the primary key is equal to the value we've passed (id)
        return User.query.get(int(id))

    return app

# Here we check if the path to the database exists, if not we create it, if it exists we let it as it is
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
