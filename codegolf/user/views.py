from flask import Blueprint, render_template

user = Blueprint('user', __name__, url_prefix='/user')


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


@user.route('/register')
def register():
    return render_template('layout.html')
