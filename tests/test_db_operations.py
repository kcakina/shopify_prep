import pytest
from app.db import DB
from app.models import Exchange
from app.models import Person
from app.services import create_new_exchange, add_person_to_exchange, create_exclusions, assign_exchange_partners


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


def _setup_exchange_with_two_people(db):
    exchange = db.create_new_exchange()
    p1 = Person()
    p2 = Person()
    db.add_person_to_db(p1.id)
    db.add_person_to_db(p2.id)
    db.add_person_to_exchange(p1.id, exchange.id)
    db.add_person_to_exchange(p2.id, exchange.id)
    return exchange, p1, p2


def test_create_exclusions_success():
    db = DB()
    exchange, p1, p2 = _setup_exchange_with_two_people(db)
    create_exclusions(db, exchange.id, p1.id, p2.id)
    assert (p1.id, p2.id) in exchange.exclusions


def test_create_exclusions_fails_person_not_in_exchange():
    db = DB()
    exchange = db.create_new_exchange()
    p1 = Person()
    p2 = Person()
    db.add_person_to_db(p1.id)
    db.add_person_to_db(p2.id)
    db.add_person_to_exchange(p1.id, exchange.id)
    # p2 not added to exchange
    result = create_exclusions(db, exchange.id, p1.id, p2.id)
    assert result is False


def test_create_exclusions_fails_person_not_in_db():
    db = DB()
    exchange = db.create_new_exchange()
    result = create_exclusions(db, exchange.id, "fake-person-1", "fake-person-2")
    assert result is False


def _setup_exchange_with_people(db, count):
    exchange = db.create_new_exchange()
    people = []
    for _ in range(count):
        p = Person()
        db.add_person_to_db(p.id)
        db.add_person_to_exchange(p.id, exchange.id)
        people.append(p)
    return exchange, people


def test_assign_exchange_partners_everyone_gets_a_partner():
    db = DB()
    exchange, people = _setup_exchange_with_people(db, 4)
    assignments = assign_exchange_partners(db, exchange.id)
    assert len(assignments) == 4
    for p in people:
        assert p.id in assignments


def test_assign_exchange_partners_no_self_assignment():
    db = DB()
    exchange, people = _setup_exchange_with_people(db, 5)
    assignments = assign_exchange_partners(db, exchange.id)
    for giver, receiver in assignments.items():
        assert giver != receiver


def test_assign_exchange_partners_respects_exclusions():
    db = DB()
    exchange, people = _setup_exchange_with_people(db, 4)
    p1, p2 = people[0], people[1]
    db.create_exclusion(exchange.id, p1.id, p2.id)
    assignments = assign_exchange_partners(db, exchange.id)
    assert assignments[p1.id] != p2.id


def test_assign_exchange_partners_stores_on_exchange():
    db = DB()
    exchange, people = _setup_exchange_with_people(db, 3)
    assignments = assign_exchange_partners(db, exchange.id)
    assert exchange.assignments == assignments