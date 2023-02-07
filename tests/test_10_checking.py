import sqlite3
import pytest
import logging


try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)

@pytest.fixture
def setup_database():
    """Setting up the setup database"""
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE PhoneNumber (PhoneNumber INTEGER)")
    cursor.execute("CREATE TABLE Contact (First_Name TEXT, LastName TEXT)")
    cursor.execute("INSERT INTO PhoneNumber (PhoneNumber) VALUES (1234567890)")
    cursor.execute("INSERT INTO Contact (First_Name, LastName) VALUES ('John', 'Doe')")
    connection.commit()
    yield connection
    connection.close()

def test_check_for_same_tel(setup_database):
    """This method checks if same tel is in db"""
    checking = adress.Checking()
    checking.connection = setup_database
    result = checking.check_for_same_tel(1234567890)
    assert result == [(1234567890,)]

def test_check_for_same_name(setup_database):
    """This method checks if same name is in db"""
    checking = adress.Checking()
    checking.connection = setup_database
    result = checking.check_for_same_name('John', 'Doe')
    assert result == [('John', 'Doe')]
