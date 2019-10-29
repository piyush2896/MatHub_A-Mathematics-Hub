import numpy as np

from .client import BaseClient
from .__parent import Parent
from .__student import Student
from .__teacher import Teacher
from db_handler import firebase_handler as fb_handle

class Admin(BaseClient):
    """
    actors.__admin.Admin: This class is a derived class from the ABC - actors.client.BaseClass.
    It represents an admin interacting with the web interface.
    """

    DB_URL = "/Admins" # TODO: Discuss

    STUDENT = 'student'
    TEACHER = 'teacher'
    PARENT = 'parent'
    ADMIN = 'admin'

    def __init__(self, username, id, name):
        """
        actors.__admin.Admin: This class is a derived class from the ABC - actors.client.BaseClass.
        It represents an admin interacting with the web interface.

        @params
        username: Username of the Admin.
        id: Id of the Admin.
        name: Name of the Admin
        """
        super().__init__(username, id, name)

    def set_name(self, name):
        """
        Admin.set_name: Takes name to be placed for the current admin object.

        @params
        name: Name of the admin
        """
        super().set_name(name)

    def get_name(self):
        """
        Admin.get_name: Returns the name for the current admin object

        @returns
        name: Name of the admin
        """
        return super().get_name()

    def get_username(self):
        """
        Admin.get_username: Returns the username for the current admin object

        @returns
        username: Username of the admin
        """
        return super().get_username()

    def get_id(self):
        """
        Admin.get_id: Returns the id for the current admin object

        @returns
        id: ID of the admin
        """
        return super().get_id()

    @staticmethod
    def create_user(fb_url, client_dict):
        db_handler = fb_handle.FirebaseEntryPoint.create()
        db_handler.add_data(fb_url, client_dict)

    @staticmethod
    def create_user_instance(data):
        if data['usertype'] == Admin.STUDENT:
            client = Student(
                data['username'], data['id'], data['name'], data['grade'])
            if 'marks' in data:
                for marks in data['marks']:
                    client.add_marks(marks)

        elif data['usertype'] == Admin.TEACHER:
            client = Teacher(data['username'], data['id'], data['name'])
            if 'grades' in data:
                for grade in data['grades']: client.add_grade(grade)

        elif data['usertype'] == Admin.PARENT:
            client = Parent(
                data['username'], data['id'], data['name'], data['stud_id'])

        else:
            client = Admin(
                data['username'], data['id'], data['name'])

        return client
