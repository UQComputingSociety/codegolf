from flask import Flask

from .user import user as user_bp
from .challenge import challenge as challenge_bp
from .submission import submission as submission_bp

from .models import *

BLUEPRINTS = (user_bp, challenge_bp, submission_bp)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///codegolf.db'

for blueprint in BLUEPRINTS:
    app.register_blueprint(blueprint)

from . import views
