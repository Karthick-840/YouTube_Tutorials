# Import necessary modules
from flask import Flask, render_template
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL')
    )
    # Initialize extensions and blueprints
    return app

# Create the Flask app
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return 'Welcome to YouTube Tutorials!'

# Playlist creation route
@app.route('/create_playlist')
def create_playlist():
    return 'Create a playlist page'

# Schedule learning route
@app.route('/schedule_learning')
def schedule_learning():
    return 'Schedule your learning page'


