from collections import defaultdict

from exceptiongroup import catch

from app.models import Person, Exchange
from typing import Optional
class DB:
    def __init__(self):
        self.exchanges = {}
        self.exclusions = {}
        self.people = {}

    def create_new_exchange(self) -> Exchange:
        new_exchange = Exchange()
        if new_exchange.id in self.exchanges:
            raise Exception(f'Cant reuse id {new_exchange.id}')
        self.exchanges[new_exchange.id] = new_exchange
        return new_exchange

    def add_person_to_exchange(self, person_id: str, exchange_id):
        if exchange_id not in self.exchanges:
            raise Exception(f'exchange_id: {exchange_id} not found.')
        exchange = self.exchanges[exchange_id]
        exchange.people.add(person_id)

    def add_person_to_db(self, person_id: str):
        if person_id in self.people:
            raise Exception(f'invalid person id')
        self.people[person_id] = True




