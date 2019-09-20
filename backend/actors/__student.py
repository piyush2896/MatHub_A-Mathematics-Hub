import numpy as np

from .client import BaseClient

class Student(BaseClient):
	"""
	actors.__student.Student: This class is a derived class from the ABC - actors.client.BaseClass.
	It represents a student interacting with the web interface.
	"""
	def __init__(self, name, grade):
		"""
		actors.__student.Student: This class is a derived class from the ABC - actors.client.BaseClass.
		It represents a student interacting with the web interface.

		@params
		name: Name of the Student
		grade: Grade/class in which the Student belong.

		@returns
		Student: Returns an instance of object of class Student
		"""
		self.__name = name
		self.__grade = grade
		self.__marks = []

	def set_name(self, name):
		"""
		Student.set_name: Takes name to be placed for the current student object.

		@params
		name: Name of the Student
		"""
		self.__name = name

	def set_grade(self, grade):
		"""
		Student.set_grade: Takes grade (aka current class of the student) to be placed 
		for the current student object.

		@params
		grade: Grade of the Student
		"""
		self.__grade = grade

	def add_marks(self, marks):
		"""
		Student.add_marks: Takes and add marks for the current student in his/her marks list.

		@params
		marks: Marks of student in a test.
		"""
		self.__marks.append(marks)

	def get_name(self):
		return self.__name

	def get_grade(self):
		return self.__grade

	def get_marks(self):
		return self.__marks
