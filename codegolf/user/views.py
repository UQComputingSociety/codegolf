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
@user.route('/account')
@login_required
def account():
    """
    View list of submissions for a given user and their total points
    """
    return render_template('user/account.html')


@user.route('/delete')
@login_required
def delete():
    """
    Admin only page to delete a user (for example troll account). Option to also delete all the users submissions or to
    keep them but prevent them from submitting further solutions.
    """
    return render_template('layout.html')


@user.route('/login')
def login():
    """
    Redirects to github oauth which redirects to /authorize
    """
    if app.testing:
        callback_url = url_for('user.authorize', _external=True)
    else:
        callback_url = 'https://codegolf.uqcs.org.au/user/authorize'
    return git_auth.authorize(callback=callback_url)


@user.route("/logout")
@login_required
def logout():
    """
    Logs out a user
    :return:
    """
    logout_user()
    return redirect(url_for('index'))


@user.route('/authorize')
def authorize():
    """
    Use information from github oauth log in to either create a new user or log in as an existing user.
    """
    resp = git_auth.authorized_response()
    user_info = git_auth.get('user', token=(resp["access_token"],)).data
    u = db_session.query(User).filter(User.email == user_info['email']).first()
    if not u:
        u = User(user_info['login'], user_info['email'])
        db_session.add(u)
        db_session.commit()
    login_user(u, remember=True)
    return redirect(url_for('index'))
