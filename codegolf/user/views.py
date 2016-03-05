"""
Views for the User model.
"""
from flask import Blueprint, render_template, url_for, redirect
from flask_oauthlib.client import OAuth
from flask_oauthlib.contrib.apps import github
from flask_login import login_required, current_user, login_user, logout_user
from codegolf import login_manager, app
from codegolf.database import db_session
from codegolf.models import User

user = Blueprint('user', __name__, url_prefix='/user')

oauth = OAuth(app)
git_auth = github.register_to(oauth)


@login_manager.user_loader
def user_loader(user_id):
    return db_session.query(User).filter(User.id == user_id).one()


@user.route('/')
def index():
    return render_template('layout.html')


@user.route('/details')
def details():
    return render_template('layout.html')


@user.route('/delete')
@login_required
def delete():
    return render_template('layout.html')


@user.route('/account')
@login_required
def account():
    return render_template('layout.html')


@user.route('/login')
def login():
    callback_url = url_for('user.authorize', _external=True)
    return git_auth.authorize(callback=callback_url)


@user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@user.route('/authorize')
def authorize():
    resp = git_auth.authorized_response()
    user_info = git_auth.get('user', token=(resp["access_token"],)).data
    u = db_session.query(User).filter(User.email == user_info['email']).first()
    if not u:
        u = User(user_info['login'], user_info['email'])
        db_session.add(u)
        db_session.commit()
    login_user(u, remember=True)
    return redirect(url_for('index'))
