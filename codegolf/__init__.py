from flask import Flask
import sqlalchemy as sa
import sqlalchemy.orm as sao
from .models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///codegolf.db'

from codegolf import views
