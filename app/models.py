import uuid
from typing import List

class Person:
    def __init__(self):
        self.id = str(uuid.uuid4())

class Exchange:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.exclusions = set() # set of tuples
        self.assignments = None
        self.people = set()




