import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/boards')
def boards():
    return flask.render_template('boards.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)