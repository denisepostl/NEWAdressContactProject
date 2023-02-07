import sqlite3
import logging
import pytest

try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)


@pytest.fixture()
def create_db():
    """Create a database"""
    db = adress.Create()
    yield db
    # close the connection to the database
    db.connection.close()


def test_create_Phonenumber(create_db):
    """Test if Table PhoneNumber is created"""
    cur = create_db.connection.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='PhoneNumber';")
    result = cur.fetchone()
    assert result[0] == 'PhoneNumber', f"Expected table name PhoneNumber but got {result[0]}"


def test_create_Contact(create_db):
    """Test if Table Contact is created"""
    cur = create_db.connection.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Contact';")
    result = cur.fetchone()
    assert result[0] == 'Contact', f"Expected table name Contact but got {result[0]}"


def test_create_Adress(create_db):
    """Test if Table Adress is created"""
    cur = create_db.connection.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Adress';")
    result = cur.fetchone()
    assert result[0] == 'Adress', f"Expected table name Adress but got {result[0]}"


def test_create_Category(create_db):
    """Test if Table Category is created"""
    cur = create_db.connection.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Kategorie';")
    result = cur.fetchone()
    assert result[0] == 'Kategorie', f"Expected table name Kategorie but got {result[0]}"