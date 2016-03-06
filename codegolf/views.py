"""
Main entry point views.
"""
import flask

from . import app
from .database import db_session
from .models import User


@app.route('/')
def index():
    return flask.render_template('home.html')


@app.route('/about')
def about():
    return flask.render_template('about.html')


@app.route('/contribute')
def contribute():
    return flask.render_template('contribute.html')


@app.route('/scores')
def scores():
    return flask.render_template('scores.html')


@app.route('/addBob')
def test_db_with_bob():
    u = User("Bobby", "bob@example.com")
    db_session.add(u)
    db_session.commit()
    return flask.render_template('layout.html')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
