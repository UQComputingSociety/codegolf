"""
Views for the Challenge model.
"""
from flask import Blueprint, render_template
from flask_login import login_required
from codegolf.models import Challenge

challenge = Blueprint('challenge', __name__, url_prefix='/challenge')


@challenge.route('/')
def index():
    return render_template('layout.html')


@challenge.route('/details')
def details():
    return render_template('layout.html')


@challenge.route('/delete')
@login_required
def delete():
    return render_template('layout.html')


@challenge.route('/edit')
@login_required
def edit():
    return render_template('layout.html')


@challenge.route('/create')
@login_required
def create():
    return render_template('layout.html')
