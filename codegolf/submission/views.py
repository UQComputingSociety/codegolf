"""
Views for the Submission model.
"""
from flask import Blueprint, render_template
from flask_login import login_required
from codegolf.models import Submission
from codegolf.user.views import admin_required

submission = Blueprint('submission', __name__, url_prefix='/submission')


@submission.route('/')
def index():
    """
    List all submissions for your account.
    """
    return render_template('layout.html')


@submission.route('/details')
def details():
    """
    View the details for a particular submission including source code, character count, and submitter. If the challenge
    has not completed yet, this only shows the character count and language with the actual code and the submitter
    unknown.
    """
    return render_template('layout.html')


@submission.route('/delete')
@admin_required
def delete():
    """
    Admin only page to delete a particular submission
    """
    return render_template('layout.html')


@submission.route('/edit')
@login_required
def edit():
    """
    Page that let's you update a particular submission if you are logged in as the same account that submitted the
    solution.
    """
    return render_template('layout.html')


# Removed in favour of creating submissions inside the details of the challenge
# @submission.route('/create')
# @login_required
# def create():
#     """
#
#     """
#     return render_template('layout.html')
