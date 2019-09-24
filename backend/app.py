import flask

from arithmetic_api import basic_ops

app = flask.Flask(__name__)

def arithmetic_helper(data):
    if 'operand1' not in list(data.keys()):
        print('Throw Error') # TODO: Throw Error
    if 'operand2' not in list(data.keys()):
        print('Throw Error') # TODO: Throw Error

@app.route('/eval', methods=['GET', 'POST'])
def basic_arithmetic_ops():
	data = flask.request.json 
	implementor = basic_ops.OperatorImplementor.create()
	result = implementor.do_op(data)
	return flask.jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
