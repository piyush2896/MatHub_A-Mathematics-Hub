import flask

app = flask.Flask(__name__)

@app.route('/add')
def arithmetic_add():
    return flask.render_template_string('HEllO from add')

@app.route('/sub')
def arithmetic_sub():
    return flask.render_template_string('HEllO from sub')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
