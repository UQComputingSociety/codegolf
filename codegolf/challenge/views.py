"""
Views for the Challenge model.
"""
from flask import Blueprint, render_template
from flask_login import login_required
from codegolf.models import Challenge

challenge = Blueprint('challenge', __name__, url_prefix='/challenge')


@challenge.route('/')
def index():
    """
    Displays a list of all challenges alongside the start/end date and who had the shortest program with what length
    and language.
    """
    return render_template('layout.html')


@challenge.route('/details')
def details():
    """
    Displays the details for a particular challenge, and a textbox/input where you can submit a solution to the
    challenge. If the end date has passed, people can still submit solutions they can still submit, they just won't be
    eligible for points. As well, if the end date has passed, you will see a list of solutions with the option to filter
    by language at the top. You can click on a solution to go to the relevant submission details page.
    """
    return render_template('layout.html')


@challenge.route('/delete')
@login_required
def delete():
    """
    Admin only page for deleting a challenge.
    """
    return render_template('layout.html')


@challenge.route('/edit')
@login_required
def edit():
    """
    Admin only page to edit a challenge (such as change the description). If a non-admin views this page, it should be a
    form to request a challenge to be edited or to ask for clarification.
    """
    return render_template('layout.html')


@challenge.route('/create')
@login_required
def create():
    """
    Admin only page to create a challenge. If a non-admin views this page, there is a form to suggest new challenges.
    """
    return render_template('layout.html')
