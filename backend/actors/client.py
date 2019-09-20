from abc import ABC, abstractmethod

class BaseClient(ABC):
	def __init__(self):
		raise NotImplementedError('Cannot initialize Abstract Class')
