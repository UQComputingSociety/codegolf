"""
Views for the Challenge model.
"""
from flask import Blueprint, render_template
from codegolf.models import challenge as m_challenge

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
