"""
All the actors, which are in contact with the web-interface, comes under this package.

Every actor must inherit from the Abstract Base Class -> actors.client.BaseClient
"""

from .__student import Student
from .__teacher import Teacher
from .__parent import Parent
from .__admin import Admin

STUDENT_ID_PREFIX = 'S'
TEACHER_ID_PREFIX = 'T'
PARENT_ID_PREFIX = 'P'
ADMIN_ID_PREFIX = 'A'

START_ID = 100
