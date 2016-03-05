"""
Views for the User model.
"""
from flask import Blueprint, render_template, url_for, redirect
from flask_oauthlib.client import OAuth
from flask_oauthlib.contrib.apps import github
from flask_login import login_required, current_user
from codegolf import login_manager, app
from codegolf.database import db_session
from codegolf.models import User

user = Blueprint('user', __name__, url_prefix='/user')

oauth = OAuth(app)
git_auth = github.register_to(oauth)


@user.route('/')
def index():
    return render_template('layout.html')


@user.route('/details')
def details():
    return render_template('layout.html')


@user.route('/delete')
def delete():
    return render_template('layout.html')


@user.route('/account')
def account():
    return render_template('layout.html')


@user.route('/login')
def login():
    callback_url = url_for('user.authorize', _external=True)
    print(callback_url)
    return git_auth.authorize(callback=callback_url)


@user.route('/authorize')
def authorize():
    resp = git_auth.authorized_response()
    print(resp)
    return redirect(url_for('index'))


@login_manager.user_loader
def user_loader(user_id):
    return db_session.query(User).filter(User.id == user_id).one()
