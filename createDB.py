"""
Will create a database using the models defined in codegolf.models.
"""
from codegolf.database import init_db

print("Creating the database in this local directory called codegolf.db")
init_db()
