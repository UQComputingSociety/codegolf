"""
Starts up a development run of the codegolf server.
"""
from codegolf import app

app.run(debug=True, host="localhost")
