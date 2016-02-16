from flask import Blueprint, render_template
from ..database import db_session
from ..models import Submission

submission = Blueprint('submission', __name__, url_prefix='/submission')


@submission.route('/')
def index():
    return render_template('layout.html')


@submission.route('/details')
def details():
    return render_template('layout.html')


@submission.route('/delete')
def delete():
    return render_template('layout.html')


@submission.route('/edit')
def edit():
    return render_template('layout.html')


@submission.route('/create')
def create():
    return render_template('layout.html')
