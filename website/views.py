from flask import Blueprint, render_template

# This file is a blueprint of our application, here we define the routes

# usually we name this the same name as the file (views.py)
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")