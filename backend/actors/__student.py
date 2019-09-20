import numpy as np

from .client import BaseClient

class Student(BaseClient):
	def __init__(self, name, grade):
		self.__name = name
		self.__grade = grade
		self.__marks = []

	def set_name(self, name):
		self.__name = name

	def set_grade(self, grade):
		self.__grade = grade

	def add_marks(self, marks):
		self.__marks.append(marks)

	def get_name(self):
		return self.__name

	def get_grade(self):
		return self.__grade

	def get_marks(self):
		return self.__marks
