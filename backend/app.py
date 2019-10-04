import flask

from arithmetic_api import basic_ops

app = flask.Flask(__name__)

def arithmetic_helper(data):
    if 'operand1' not in list(data.keys()):
        raise KeyError('operand 1 key missing in data')
    if 'operand2' not in list(data.keys()):
        raise KeyError('operand 2 key missing in data')
    if 'operator' not in list(data.keys()):
        raise KeyError('operator key missing in data')

@app.route('/eval', methods=['GET', 'POST'])
def basic_arithmetic_ops():
    data = flask.request.json
    try:
        arithmetic_helper(data)
    except KeyError as e:
        return flask.jsonify({'result': '{}'.format(e)})
    except:
        return flask.jsonify({'result': 'Error'}) 
    implementor = basic_ops.OperatorImplementor.create()
    result = implementor.do_op(data)
    return flask.jsonify({'result': result})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)