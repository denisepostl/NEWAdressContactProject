import sqlite3
import pytest

import logging


try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)

@pytest.fixture(scope="module")
def setup_db():
    """Setting up the test database"""
    connection = sqlite3.connect(":memory:")
    cur = connection.cursor()
    
    # Create tables for testing
    cur.execute("""
        CREATE TABLE Contact (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            First_Name TEXT NOT NULL,
            Last_Name TEXT NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE PhoneNumber (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            PhoneNumber TEXT NOT NULL,
            Contact_ID INTEGER NOT NULL,
            FOREIGN KEY (Contact_ID) REFERENCES Contact(ID)
        )
    """)
    cur.execute("""
        CREATE TABLE Adress (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Adress TEXT NOT NULL,
            Contact_ID INTEGER NOT NULL,
            FOREIGN KEY (Contact_ID) REFERENCES Contact(ID)
        )
    """)
    
    # Insert test data into the database
    cur.execute("INSERT INTO Contact (First_Name, Last_Name) VALUES ('John', 'Doe')")
    cur.execute("INSERT INTO PhoneNumber (PhoneNumber, Contact_ID) VALUES ('1234567890', 1)")
    cur.execute("INSERT INTO Adress (Adress, Contact_ID) VALUES ('123 Main St', 1)")
    
    connection.commit()
    yield connection
    connection.close()

def test_get_count_adr(setup_db):
    """Test for testing the count_adress Method"""
    obj = adress.Accept_Adress()
    obj.connection = setup_db
    obj.My_ID = 1
    
    result = obj.get_count_adr()
    assert result == 1

def test_get_count_tel(setup_db):
    """Test for testing the count_tel Method"""
    obj = adress.Accept_Adress()
    obj.connection = setup_db
    obj.My_ID = 1
    
    result = obj.get_count_tel()
    assert result == 1
