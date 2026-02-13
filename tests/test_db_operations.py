import pytest
from app.db import DB
from app.models import Exchange
from app.services import create_new_exchange, add_person_to_exchange


def test_create_new_exchange_returns_exchange():
    db = DB()
    result = create_new_exchange(db)
    assert isinstance(result, Exchange)


def test_create_new_exchange_stores_in_db():
    db = DB()
    result = create_new_exchange(db)
    assert result.id in db.exchanges
    assert db.exchanges[result.id] is result


def test_add_person_to_exchange_success():
    db = DB()
    exchange = create_new_exchange(db)
    result = add_person_to_exchange(db, exchange.id)
    assert result is True
    assert len(exchange.people) == 1


def test_add_person_to_exchange_fails_with_invalid_exchange():
    db = DB()
    result = add_person_to_exchange(db, "nonexistent-id")
    assert result is False


def test_db_add_person_to_exchange_raises_on_invalid_exchange():
    db = DB()
    with pytest.raises(Exception, match="exchange_id: fake-id not found"):
        db.add_person_to_exchange("some-person", "fake-id")


def test_db_add_person_to_db_raises_on_duplicate():
    db = DB()
    db.add_person_to_db("person-1")
    with pytest.raises(Exception, match="invalid person id"):
        db.add_person_to_db("person-1")