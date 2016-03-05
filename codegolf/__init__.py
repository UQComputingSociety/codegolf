import os
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///codegolf.db'
app.config['GITHUB_CONSUMER_KEY'] = os.environ['CODEGOLF_GITHUB_CONSUMER_KEY']
app.config['GITHUB_CONSUMER_SECRET'] = os.environ['CODEGOLF_GITHUB_CONSUMER_SECRET']
app.config['SECRET_KEY'] = os.environ['CODEGOLF_SECRET_KEY']

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "user.login"
login_manager.login_message = "Log In Please"

from .models import *

from .user import user as user_bp
from .challenge import challenge as challenge_bp
from .submission import submission as submission_bp

BLUEPRINTS = (user_bp, challenge_bp, submission_bp)

for blueprint in BLUEPRINTS:
    app.register_blueprint(blueprint)

from . import views