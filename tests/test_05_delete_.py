import sqlite3
import pytest
import logging


try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)


@pytest.fixture
def setup_delete_contact():
    """Create in-memory database for testing"""
    connection = sqlite3.connect(":memory:")
    cur = connection.cursor()
    cur.execute("""
        CREATE TABLE Adress (
            Contact_ID INTEGER PRIMARY KEY,
            Street TEXT,
            City TEXT,
            Country TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE PhoneNumber (
            Contact_ID INTEGER PRIMARY KEY,
            Phone_Number TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE Kategorie (
            Contact_ID INTEGER PRIMARY KEY,
            Category TEXT
        )
    """)
    cur.execute("""
        INSERT INTO Adress (Contact_ID, Street, City, Country)
        VALUES (1, 'Street 1', 'City 1', 'Country 1'),
               (2, 'Street 2', 'City 2', 'Country 2')
    """)
    cur.execute("""
        INSERT INTO PhoneNumber (Contact_ID, Phone_Number)
        VALUES (1, '1234567890'),
               (2, '0987654321')
    """)
    cur.execute("""
        INSERT INTO Kategorie (Contact_ID, Category)
        VALUES (1, 'Category 1'),
               (2, 'Category 2')
    """)
    connection.commit()
    yield connection
    connection.close()


def test_delete_adress(setup_delete_contact):
    """Test if user can delete adress"""
    delete_contact = adress.Delete_Contact()
    delete_contact.connection = setup_delete_contact
    delete_contact.delete_adress(1)
    cur = delete_contact.connection.cursor()
    cur.execute("SELECT * FROM Adress")
    adresses = cur.fetchall()
    assert len(adresses) == 1
    assert adresses[0][0] == 2


def test_delete_phonenumber(setup_delete_contact):
    """Test if user can delete phonenumber"""
    delete_contact = adress.Delete_Contact()
    delete_contact.connection = setup_delete_contact
    delete_contact.delete_phonenumber(1)
    cur = delete_contact.connection.cursor()
    cur.execute("SELECT * FROM PhoneNumber")
    phone_numbers = cur.fetchall()
    assert len(phone_numbers) == 1
    assert phone_numbers[0][0] == 2


def test_delete_category(setup_delete_contact):
    """Test if user can delete category"""
    delete_contact = adress.Delete_Contact()
    delete_contact.connection = setup_delete_contact
    delete_contact.delete_category(1)
    cur = delete_contact.connection.cursor()
    cur.execute("SELECT * FROM Kategorie")
    categories = cur.fetchall()
    assert len(categories) == 1
    assert categories[0][0] == 2