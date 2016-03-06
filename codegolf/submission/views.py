"""
Views for the Submission model.
"""
from flask import Blueprint, render_template
from flask_login import login_required
from codegolf.models import Submission

submission = Blueprint('submission', __name__, url_prefix='/submission')


# Lists all submissions for your account
@submission.route('/')
def index():
    return render_template('layout.html')


# allows you to view and individual submission /details?sub_id=2030230938
@submission.route('/details')
def details():
    return render_template('layout.html')


# allows you to delete a submission if your the owner /delete?sub_id=skdhfkjdshfkjd
@submission.route('/delete')
@login_required
def delete():
    return render_template('layout.html')


# allows you to edit a submission if your the owner /edit?sub_id=934798347
@submission.route('/edit')
@login_required
def edit():
    return render_template('layout.html')


# allows you to create a submission for a challenge /create?challenge_id=9020934809843
@submission.route('/create')
@login_required
def create():
    return render_template('layout.html')
