# Import necessary modules
from flask import Flask, render_template

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

