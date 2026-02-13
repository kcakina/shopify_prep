import uuid
from typing import List

class Person:
    def __init__(self):
        self.id = uuid.uuid4()

class Exchange:
    def __init__(self):
        self.id = uuid.uuid4()
        self.assignments = {}
        self.people = set()


class Exclusions:
    def __init__(self, personA, PersonB):
        self.exclusions = {}



