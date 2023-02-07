import sqlite3
import pytest
import logging


try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)



@pytest.fixture(scope="module")
def setup_db():
    """Setting up an in-memory database and insert test data"""
    connection = sqlite3.connect(":memory:")
    cur = connection.cursor()
    cur.execute("""
        CREATE TABLE Kategorie (
            Kategorie text
        )
    """)
    cur.execute("""
        INSERT INTO Kategorie (Kategorie)
        VALUES ("Schule"), ("Familie"), ("Arbeit"), ("Freunde"), ("Schule"), ("Arbeit")
    """)
    connection.commit()
    return connection

def test_get_school(setup_db):
    """Check the counted categories of category school"""
    counting = adress.Counting()
    counting.connection = setup_db
    counting.get_school()
    assert counting.school == 2

def test_get_family(setup_db):
    """Check the counted categories of category family"""
    counting = adress.Counting()
    counting.connection = setup_db
    counting.get_family()
    assert counting.family == 1

def test_get_work(setup_db):
    """Check the counted categories of category work"""
    counting = adress.Counting()
    counting.connection = setup_db
    counting.get_work()
    assert counting.work == 2

def test_get_friends(setup_db):
    """Check the counted categories of category friends"""
    counting = adress.Counting()
    counting.connection = setup_db
    counting.get_friends()
    assert counting.friend == 1