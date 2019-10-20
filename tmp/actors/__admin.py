import numpy as np

from .client import BaseClient
from .__parent import Parent
from .__student import Student
from .__teacher import Teacher

class Admin(BaseClient):
    """
    actors.__admin.Admin: This class is a derived class from the ABC - actors.client.BaseClass.
    It represents an admin interacting with the web interface.
    """

    DB_URL = "/Admin" # TODO: Discuss

    def __init__(self, username, id, name, db_handler):
        """
        actors.__admin.Admin: This class is a derived class from the ABC - actors.client.BaseClass.
        It represents an admin interacting with the web interface.

        @params
        username: Username of the Admin.
        id: Id of the Admin.
        name: Name of the Admin
        """
        super().__init__(username, id, name)
        self.db_handler = db_handler

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

    def create_user(self, client):
        base_client_error = "Client to be created should be of type actors.client.BaseClient"
        assert isinstance(client, BaseClient), base_client_error

        if isinstance(client, Student):
            self.db_handler.add_data(Student.DB_URL, client.convert_to_dict())

        if isinstance(client, Teacher):
            self.db_handler.add_data(Teacher.DB_URL, client.convert_to_dict())

        if isinstance(client, Parent):
            self.db_handler.add_data(Parent.DB_URL, client.convert_to_dict())
