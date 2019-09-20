def add(data):
	"""
	arithmetic_api.add: Adds two operands

	@params
	data: a dictionary containing two key-value pairs, keys 'operand1' and 'operand2' for respective operand value.

	@returns
	addition of operand1 and operand2
	"""
	return data['operand1'] + data['operand2']

def sub(data):
	"""
	arithmetic_api.sub: Subtracts two operands

	@params
	data: a dictionary containing two key-value pairs, keys 'operand1' and 'operand2' for respective operand value.

	@returns
	subtraction of operand1 and operand2
	"""
	return data['operand1'] - data['operand2']

def mul(data):
	"""
	arithmetic_api.mul: Multiplies two operands

	@params
	data: a dictionary containing two key-value pairs, keys 'operand1' and 'operand2' for respective operand value.

	@returns
	multiplication of operand1 and operand2
	"""
	return data['operand1'] * data['operand2']

def div(data):
	"""
	arithmetic_api.div: Divides two operands

	@params
	data: a dictionary containing two key-value pairs, keys 'operand1' and 'operand2' for respective operand value.

	@returns
	division of operand1 and operand2
	"""
	return data['operand1'] / data['operand2']
