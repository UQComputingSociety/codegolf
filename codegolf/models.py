from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from codegolf import db


class User(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT, primary_key=True)
    email = db.Column(db.TEXT, primary_key=True)
    uqName = db.Column(db.TEXT, primary_key=True)