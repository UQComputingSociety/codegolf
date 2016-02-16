import flask

from . import app
from .database import db_session
from .models import User


@app.route('/')
def index():
    return flask.render_template('layout.html')


@app.route('/addBob')
def test_db_with_bob():
    u = User("Bobby", "bob@example.com")
    db_session.add(u)
    db_session.commit()
    return flask.render_template('layout.html')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
