import flask

from codegolf import app


@app.route('/')
def index():
    return flask.render_template('layout.html')
