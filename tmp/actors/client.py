from abc import ABC, abstractmethod

from db_handler import firebase_handler as fb_handle

class ClientNotFoundError(LookupError):
	"""Raise when username is missing from firebase database"""

	def __init__(self, *args, **kwargs):
		LookupError.__init__(self, "Client not found error.", *args,**kwargs)

class BaseClient(ABC):
	"""
	actors.client.BaseClient: it is an Abstract Base Class which represents an entity that interacts with the web-interface.

	raises NotImplementedError on initialization. 
	"""
	def __init__(self, username, id, name):
		"""
		actors.client.BaseClient: it is an Abstract Base Class which represents an entity that interacts with the web-interface.

		@params
		username: Username of the user
		id: Id of the user
		name: Name of the user
		"""
		self.__username = username
		self.__id = id
		self.__name = name
		super().__init__()

	def get_username(self):
		return self.__username

	def get_id(self):
		return self.__id

	def get_name(self):
		return self.__name

	def set_name(self, name):
		return self.__name = name

	def get_password(self):
		data = fb_handle.retrieve_data(self.__username)
		if data == None:
			raise ClientNotFoundError('Client {} not found!'.format(self.__username))
		return fb_handle.retrieve_password_from_fb_data(data)
