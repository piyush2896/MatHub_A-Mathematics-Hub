from .client import BaseClient

class Parent(BaseClient):
    """
    actors.__parent.Parent: This class is a derived class from the ABC - actors.client.BaseClass.
    It represents a parent interacting with the web interface.
    """

    DB_URL = "/Parents"

    def __init__(self, username, id, name, stud_id):
        """
        actors.__parent.Parent: This class is a derived class from the ABC - actors.client.BaseClass.
        It represents a parent interacting with the web interface.

        @params
        username: Username of the Parent.
        id: Id of the Parent.
        name: Name of the Parent
        stud_id: Student ID
        """
        super().__init__(username, id, name)
        self.__stud_id = stud_id

    def set_name(self, name):
        """
        Parent.set_name: Takes name to be placed for the current parent object.

        @params
        name: Name of the parent
        """
        super().set_name(name)

    def get_name(self):
        """
        Parent.get_name: Returns the name for the current parent object

        @returns
        name: Name of the parent
        """
        return super().get_name()

    def get_username(self):
        """
        Parent.get_username: Returns the username for the current parent object

        @returns
        username: Username of the parent
        """
        return super().get_username()

    def get_id(self):
        """
        Parent.get_id: Returns the id for the current parent object

        @returns
        id: ID of the parent
        """
        return super().get_id()

    def get_stud_id(self):
        """
        Parent.get_id: Returns the id of the Student related to the current Parent object

        @returns
        stud_id: ID of the student.
        """
        return self.__stud_id
