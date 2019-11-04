class OperatorImplementor:
	"""
	TODO: Give proper reference in documentation phase
	Src: https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
	"""
	__instance = None

	@staticmethod
	def create():
		if OperatorImplementor.__instance == None:
			OperatorImplementor()
		return OperatorImplementor.__instance

	def __init__(self):
		if OperatorImplementor.__instance != None:
			raise Exception('Cannot re-instantiate a singleton class.')
		
		self.__ops_to_func = {
			'+': add,
			'-': sub,
			'*': mul,
			'/': div,
			'^': power
		}
		self.__ops_available = set(self.__ops_to_func.keys())
		OperatorImplementor.__instance = self

	def do_op(self, data):
		if data['operator'] not in self.__ops_available:
			raise NotImplementedError('Operator not implemented')
		else:
			return self.__ops_to_func[data['operator']](data)

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
def power(data):
    """
    arithmetic_api.power: operand1 to power operand2

    @params
    data: a dictionary containing two key-value pairs, keys 'operand1' and 'operand2' for respective operand value.

    @returns
    operand1 to power operand2

    """
    return data['operand1'] ** data['operand2']