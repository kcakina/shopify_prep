from collections import defaultdict
from app.models import Person, Exchange
from typing import Optional
class DB:
    def __init__(self):
        self.exchanges = {}
        self.exclusions = {}
        self.participants = {}

    def create_new_exchange(self) -> Optional[Exchange]:
        new_exchange = Exchange()
        try:
            if new_exchange.id in self.exchanges:
                raise Exception(f'Cant reuse id {new_exchange.id}')
            else:
                self.exchanges[new_exchange.id] = new_exchange
                return new_exchange
        except Exception:
            print("Unable to create new exchange")




