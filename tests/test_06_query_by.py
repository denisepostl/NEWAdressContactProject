import sqlite3
import pytest
import logging


try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)

@pytest.fixture(scope="module")
def setup_memory_db():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # create tables
    cursor.execute("""CREATE TABLE Contact (ID INTEGER PRIMARY KEY, First_Name TEXT, LastName TEXT)""")
    cursor.execute("""CREATE TABLE Adress (ID INTEGER PRIMARY KEY, Contact_ID INTEGER, Street TEXT, PostCode TEXT, City TEXT, HouseNumber TEXT, Main_Adress INTEGER)""")
    cursor.execute("""CREATE TABLE PhoneNumber (ID INTEGER PRIMARY KEY, Contact_ID INTEGER, PhoneNumber TEXT, Main_Tel INTEGER)""")
    cursor.execute("""CREATE TABLE Kategorie (ID INTEGER PRIMARY KEY, Contact_ID INTEGER, Kategorie TEXT)""")
    connection.commit()

    # insert data into tables
    cursor.execute("""INSERT INTO Contact (ID, First_Name, LastName) VALUES (1, 'John', 'Doe')""")
    cursor.execute("""INSERT INTO Adress (ID, Contact_ID, Street, PostCode, City, HouseNumber, Main_Adress) VALUES (1, 1, 'Street 1', '12345', 'City 1', '1', 1)""")
    cursor.execute("""INSERT INTO PhoneNumber (ID, Contact_ID, PhoneNumber, Main_Tel) VALUES (1, 1, '123456789', 1)""")
    cursor.execute("""INSERT INTO Kategorie (ID, Contact_ID, Kategorie) VALUES (1, 1, 'Family')""")
    connection.commit()

    yield connection

    connection.close()

def test_querybyphone(setup_memory_db):
    query = adress.QuerySearchBy()
    query.connection = setup_memory_db

    # test with valid phone number
    query.querybyphone("123456789")
    result = query.contact
    assert len(result) == 1
    assert result[0][1] == 'John'
    assert result[0][2] == 'Doe'
    assert result[0][3] == 'Street 1, 12345, City 1, 1'
    assert result[0][4] is None
    assert result[0][5] == '123456789'
    assert result[0][6] is None
    assert result[0][7] == 'Family'

    # test with invalid phone number
    query.querybyphone("987654321")
    result = query.contact
    assert len(result) == 0

def test_querybycat(setup_memory_db):
    query = adress.QuerySearchBy()
    query.connection = setup_memory_db

    # test with valid category
    query.querycat("Family")
    result = query.contact
    assert len(result) == 1
    assert result[0][1] == 'John'
    assert result[0][2] == 'Doe'
    assert result[0][3] == 'Street 1, 12345, City 1, 1'
    assert result[0][4] is None
    assert result[0][5] == '123456789'
    assert result[0][6] is None
    assert result[0][7] == 'Family'

    # test with invalid category
    query.querycat("Familie")
    result = query.contact
    assert len(result) == 0

def test_querybyid(setup_memory_db):
    query = adress.QuerySearchBy()
    query.connection = setup_memory_db

    # test with valid id
    query.querybyid(1)
    result = query.contact
    assert len(result) == 1
    assert result[0][1] == 'John'
    assert result[0][2] == 'Doe'
    assert result[0][3] == 'Street 1, 12345, City 1, 1'
    assert result[0][4] is None
    assert result[0][5] == '123456789'
    assert result[0][6] is None
    assert result[0][7] == 'Family'

    # test with invalid id
    query.querybyid(2)
    result = query.contact
    assert len(result) == 0

def test_querybyname(setup_memory_db):
    query = adress.QuerySearchBy()
    query.connection = setup_memory_db

    # test with valid name
    query.querybyname("John", "Doe")
    result = query.contact
    assert len(result) == 1
    assert result[0][1] == 'John'
    assert result[0][2] == 'Doe'
    assert result[0][3] == 'Street 1, 12345, City 1, 1'
    assert result[0][4] is None
    assert result[0][5] == '123456789'
    assert result[0][6] is None
    assert result[0][7] == 'Family'

    # test with invalid name
    query.querybyname("Jane", "Doe")
    result = query.contact
    assert len(result) == 0

def test_askin_all(setup_memory_db):
    query = adress.QuerySearchBy()
    query.connection = setup_memory_db

    query.askin_all()
    result = query.contact
    assert len(result) == 1
    assert result[0][1] == 'John'
    assert result[0][2] == 'Doe'
    assert result[0][3] == 'Street 1, 12345, City 1, 1'
    assert result[0][4] is None
    assert result[0][5] == '123456789'
    assert result[0][6] is None
    assert result[0][7] == 'Family'
