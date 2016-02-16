from flask import Blueprint, render_template

challenge = Blueprint('challenge', __name__, url_prefix='/challenge')


@challenge.route('/')
def index():
    return render_template('layout.html')


@challenge.route('/details')
def details():
    return render_template('layout.html')


@challenge.route('/delete')
def delete():
    return render_template('layout.html')


@challenge.route('/edit')
def edit():
    return render_template('layout.html')


@challenge.route('/create')
def create():
    return render_template('layout.html')
