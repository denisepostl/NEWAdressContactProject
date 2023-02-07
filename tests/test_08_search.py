import sqlite3
import pytest
import logging


try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)


@pytest.fixture
def setup_memory_db():
    """Create the in-memory database for testing."""
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE Contact (
            ID INTEGER PRIMARY KEY,
            First_Name TEXT,
            LastName TEXT
        );
    """)
    cursor.execute("""
        CREATE TABLE Adress (
            Contact_ID INTEGER,
            PostCode TEXT,
            City TEXT,
            Street TEXT,
            HouseNumber TEXT,
            FOREIGN KEY (Contact_ID) REFERENCES Contact (ID)
        );
    """)
    cursor.execute("""
        CREATE TABLE PhoneNumber (
            Contact_ID INTEGER,
            PhoneNumber TEXT,
            FOREIGN KEY (Contact_ID) REFERENCES Contact (ID)
        );
    """)
    cursor.execute("""
        CREATE TABLE Kategorie (
            Contact_ID INTEGER,
            Kategorie TEXT,
            FOREIGN KEY (Contact_ID) REFERENCES Contact (ID)
        );
    """)
    cursor.execute("""
        INSERT INTO Contact (ID, First_Name, LastName)
        VALUES (1, 'John', 'Doe'), (2, 'Jane', 'Doe');
    """)
    cursor.execute("""
        INSERT INTO Adress (Contact_ID, PostCode, City, Street, HouseNumber)
        VALUES (1, '12345', 'City A', 'Street A', '1'), (2, '54321', 'City B', 'Street B', '2');
    """)
    cursor.execute("""
        INSERT INTO PhoneNumber (Contact_ID, PhoneNumber)
        VALUES (1, '0664201202'), (2, '0620121212');
    """)
    cursor.execute("""
        INSERT INTO Kategorie (Contact_ID, Kategorie)
        VALUES (1, 'Familie'), (2, 'Freunde');
    """)
    connection.commit()
    return connection


def test_askin_query(setup_memory_db):
    """Test if right records returned if user search for contact by First- and Last Name"""
    query = adress.QuerySearchBy()
    query.connection = setup_memory_db
    query.askin_query("John", "Doe")
    result = query.contact
    assert result == [(1, 'John', 'Doe', '12345', 'City A', 'Street A', '1', '0664201202', 'Familie')]


def test_askin_phone_query(setup_memory_db):
    """Test if right records returned if user search for contact by PhoneNumber"""
    query = adress.QuerySearchBy()
    query.connection = setup_memory_db
    query.askin_phone_query("0620121212")
    result = query.contact
    assert result == [(2, 'Jane', 'Doe', '54321', 'City B', 'Street B', '2', '0620121212', 'Freunde')]


def test_askin_all(setup_memory_db):
    """Test if right records returned if user search for all contacts"""
    query = adress.QuerySearchBy()
    query.connection = setup_memory_db
    query.askin_all_query()
    result = query.contact
    assert result == [
        (1, 'John', 'Doe', '12345', 'City A', 'Street A', '1', '0664201202', 'Familie'),
        (2, 'Jane', 'Doe', '54321', 'City B', 'Street B', '2', '0620121212', 'Freunde')
    ]

def test_askin_by_id(setup_memory_db):
    """Test if right records returned if user search for all contacts"""
    query = adress.QuerySearchBy()
    query.connection = setup_memory_db
    query.askin_by_id(1)
    result = query.contact
    assert result == [(1, 'John', 'Doe', '12345', 'City A', 'Street A', '1', '0664201202', 'Familie')]

def test_askin_by_category(setup_memory_db):
    query = adress.QuerySearchBy()
    query.connection = setup_memory_db
    query.askin_category_query('Familie')
    result = query.contact
    assert result == [(1, 'John', 'Doe', '12345', 'City A', 'Street A', '1', '0664201202', 'Familie')]
