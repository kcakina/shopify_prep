from collections import defaultdict
from app.models import Person
class DB:
    def __init__(self):
        self.exchanges = {}
        self.exclusions = {}
        self.participants = {}