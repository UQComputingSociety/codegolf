from flask import Flask
import sqlalchemy as sa
from .models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sa.sessionmaker(bind=engine)

# instantiate Session to do things.
# I might write some nice Flask extension here, but I don't want to use flask_sqlalchemy

from codegolf import views
