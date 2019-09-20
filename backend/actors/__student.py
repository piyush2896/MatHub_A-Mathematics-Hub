import numpy as np

from .client import BaseClient

class Student(BaseClient):
	def __init__(self, name, grade):
		self.__name = name
		self.__grade = grade
		self.__marks = []
