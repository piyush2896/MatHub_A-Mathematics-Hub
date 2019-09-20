from abc import ABC, abstractmethod

class BaseClient(ABC):
	"""
	actors.client.BaseClient: it is an Abstract Base Class which represents an entity that interacts with the web-interface.

	raises NotImplementedError on initialization. 
	"""
	def __init__(self):
		"""
		actors.client.BaseClient: it is an Abstract Base Class which represents an entity that interacts with the web-interface.

		raises NotImplementedError on initialization. 
		"""
		raise NotImplementedError('Cannot initialize Abstract Class')
