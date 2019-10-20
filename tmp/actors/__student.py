from .client import BaseClient

class Student(BaseClient):
	"""
	actors.__student.Student: This class is a derived class from the ABC - actors.client.BaseClass.
	It represents a student interacting with the web interface.
	"""

	DB_URL = "/Students"

	def __init__(self, username, id, name, grade):
		"""
		actors.__student.Student: This class is a derived class from the ABC - actors.client.BaseClass.
		It represents a student interacting with the web interface.

		@params
		username: Username of the Student.
		id: Id of the student.
		name: Name of the Student
		grade: Grade/class in which the Student belong.
		"""
		super().__init__(username, id, name)
		self.__grade = grade
		self.__marks = []

	def set_name(self, name):
		"""
		Student.set_name: Takes name to be placed for the current student object.

		@params
		name: Name of the Student
		"""
		super().set_name(name)

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
		"""
		Student.get_name: Returns the name for the current student object

		@returns
		name: Name of the student
		"""
		return super().get_name()

	def get_username(self):
		"""
		Student.get_username: Returns the username for the current student object

		@returns
		username: Username of the student
		"""
		return super().get_username()

	def get_id(self):
		"""
		Student.get_id: Returns the id for the current student object

		@returns
		id: ID of the student
		"""
		return super().get_id()

	def get_grade(self):
		"""
		Student.get_grade: Returns the grade or class for the current student object

		@returns
		grade: Grade of the student
		"""
		return self.__grade

	def get_marks(self):
		"""
		Student.get_marks: Returns a list of all the marks obtained by current student. Returns an empty list in case of no marks data.

		@returns
		marks: List of marks of the student
		"""
		return self.__marks
