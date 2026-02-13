from app.models import Exchange
from app.db import DB
from typing import Optional

def create_new_exchange(db: DB) -> Optional[Exchange]:
    try:
        return db.create_new_exchange()
    except:
        print("Too bad")


