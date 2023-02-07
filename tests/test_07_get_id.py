import sqlite3
import pytest
import logging


try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)


@pytest.fixture
def setup_database():
    """Create in-memory database for testing."""
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # create tables
    cursor.execute("CREATE TABLE Contact (ID INTEGER PRIMARY KEY, First_Name TEXT, LastName TEXT)")
    cursor.execute("CREATE TABLE Adress (ID INTEGER PRIMARY KEY, PostCode TEXT, City TEXT, Street TEXT, HouseNumber TEXT, Contact_ID INTEGER)")
    cursor.execute("CREATE TABLE PhoneNumber (ID INTEGER PRIMARY KEY, PhoneNumber TEXT, Contact_ID INTEGER)")
    cursor.execute("CREATE TABLE Kategorie (ID INTEGER PRIMARY KEY, Kategorie TEXT, Contact_ID INTEGER)")

    # insert test data
    cursor.execute("INSERT INTO Contact (ID, First_Name, LastName) VALUES (1, 'John', 'Doe')")
    cursor.execute("INSERT INTO Adress (ID, PostCode, City, Street, HouseNumber, Contact_ID) VALUES (1, '12345', 'Test City', 'Test Street', '1', 1)")
    cursor.execute("INSERT INTO PhoneNumber (ID, PhoneNumber, Contact_ID) VALUES (1, '1234567890', 1)")
    cursor.execute("INSERT INTO Kategorie (ID, Kategorie, Contact_ID) VALUES (1, 'Freunde', 1)")
    connection.commit()
    yield connection
    connection.close()


def test_get_name_id(setup_database):
    """Test if right contact id returned."""
    get_id_obj = adress.AddSecondRecord()
    get_id_obj.connection = setup_database
    result = get_id_obj.get_name_id("John", "Doe", "1234567890")
    assert result == 1
