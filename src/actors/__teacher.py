from .client import BaseClient

class Teacher(BaseClient):
    """
    actors.__teacher.Teacher: This class is a derived class from the ABC - actors.client.BaseClass.
    It represents a teacher interacting with the web interface.
    """

    DB_URL = "/Teachers"

    def __init__(self, username, id, name):
        """
        actors.__teacher.Teacher: This class is a derived class from the ABC - actors.client.BaseClass.
        It represents a teacher interacting with the web interface.

        @params
        username: Username of the Teacher.
        id: Id of the Teacher.
        name: Name of the Teacher
        """
        super().__init__(username, id, name)
        self.__grades = []

    def set_name(self, name):
        """
        Teacher.set_name: Takes name to be placed for the current teacher object.

        @params
        name: Name of the Teacher
        """
        super().set_name(name)

    def add_grade(self, grade):
        """
        Teacher.add_grade: Takes and add grade (aka class) for the current teacher in his/her list of grades.

        @params
        grade: Grade that the Teacher teaches
        """
        self.__grades.append(grades)

    def get_name(self):
        """
        Teacher.get_name: Returns the name for the current teacher object

        @returns
        name: Name of the teacher
        """
        return super().get_name()

    def get_username(self):
        """
        Teacher.get_username: Returns the username for the current teacher object

        @returns
        username: Username of the teacher
        """
        return super().get_username()

    def get_id(self):
        """
        Teacher.get_id: Returns the id for the current teacher object

        @returns
        id: ID of the teacher
        """
        return super().get_id()

    def get_grades(self):
        """
        Teacher.get_grades: Returns the grades or classes for the current teacher object

        @returns
        grades: list of grades that current teacher teaches
        """
        return self.__grades
