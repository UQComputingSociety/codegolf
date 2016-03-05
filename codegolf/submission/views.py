"""
Views for the Submission model.
"""
from flask import Blueprint, render_template
from flask_login import login_required
from codegolf.models import Submission

submission = Blueprint('submission', __name__, url_prefix='/submission')


@submission.route('/')
def index():
    return render_template('layout.html')


@submission.route('/details')
def details():
    return render_template('layout.html')


@submission.route('/delete')
@login_required
def delete():
    return render_template('layout.html')


@submission.route('/edit')
@login_required
def edit():
    return render_template('layout.html')


@submission.route('/create')
@login_required
def create():
    return render_template('layout.html')
