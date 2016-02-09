import flask

app = flask.Flask(__name__)


@app.route('/')
def home_page():
    return flask.render_template('layout.html')

if __name__ == "__main__":
    app.run()
