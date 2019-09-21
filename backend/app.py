import flask

from arithmetic_api import basic_ops

app = flask.Flask(__name__)

def arithmetic_helper(data):
    if 'operand1' not in list(data.keys()):
        print('Throw Error') # TODO: Throw Error
    if 'operand2' not in list(data.keys()):
        print('Throw Error') # TODO: Throw Error

@app.route('/add', methods=['GET', 'POST'])
def arithmetic_add():
    data = flask.request.json
    arithmetic_helper(data)
    return flask.jsonify({'result': basic_ops.add(data)})

@app.route('/sub', methods=['GET', 'POST'])
def arithmetic_sub():
    data = flask.request.json
    arithmetic_helper(data)
    return flask.jsonify({'result': basic_ops.sub(data)})

@app.route('/mul')
def arithmetic_mul():
	return flask.render_template_string('HEllO from mul')

@app.route('/div')
def arithmetic_div():
	return flask.render_template_string('HEllO from div')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
