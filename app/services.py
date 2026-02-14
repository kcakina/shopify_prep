from app.models import Exchange, Person
from app.db import DB
from typing import Optional

def create_new_exchange(db: DB) -> Optional[Exchange]:
    try:
        return db.create_new_exchange()
    except:
        print("Too bad")

def add_person_to_exchange(db: DB, exchange_id: str) -> bool:
    try:
        person = Person()
        db.add_person_to_db(person.id)
        db.add_person_to_exchange(person.id, exchange_id)
        return True
    except Exception:
        return False

def create_exclusions(db: DB,exchange_id: str, p1_id: str, p2_id: str)-> bool:
    try:
        db.person_exists(p1_id)
        db.person_exists(p2_id)

        exchange = db.get_exchange(exchange_id)

        if p1_id not in exchange.people or p2_id not in exchange.people:
            return False
        else:
            db.create_exclusion(exchange_id, p1_id, p2_id)

    except Exception:
        return False




