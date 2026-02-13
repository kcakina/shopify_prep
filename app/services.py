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


