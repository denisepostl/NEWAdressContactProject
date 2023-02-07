import sqlite3
import logging
import pytest

try:
    import adress
except ModuleNotFoundError as e:
    logging.error("Module not found %s", e)


@pytest.fixture
def in_memory_db():
    """Create a in memory database for testing"""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    cursor.execute("CREATE TABLE Contact ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'First_Name' TEXT, 'LastName' TEXT)")
    cursor.execute("CREATE TABLE Adress ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'PostCode' TEXT, 'Street' TEXT, 'City' TEXT, 'Housenumber' TEXT, 'Main_Adress' INTEGER, 'Contact_ID' INTEGER)")
    cursor.execute("CREATE TABLE Kategorie ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'Kategorie' TEXT, 'Contact_ID' INTEGER)")
    cursor.execute("CREATE TABLE PhoneNumber ('ID' INTEGER PRIMARY KEY AUTOINCREMENT, 'PhoneNumber' TEXT, 'Main_Tel' INTEGER, 'Contact_ID' INTEGER)")
 
    yield conn
    
    conn.close()



def test_insert_name(in_memory_db):
    """Test if user can insert First and LastName in Table Contact"""
    insert = adress.Insert()
    insert.connection=in_memory_db #connection to the in-memory db
    insert.insert_Name("John", "Doe")
    cursor = in_memory_db.cursor()
    cursor.execute("SELECT First_Name, LastName FROM Contact")
    result = cursor.fetchone()
    assert result[0] == 'John'
    assert result[1] == 'Doe' 

def test_insert_address(in_memory_db):
    """Test if user can insert Adress in Table Adress"""
    insert = adress.Insert()
    insert.connection=in_memory_db
    insert.insert_Name("John", "Doe")
    insert.insert_Address("12345", "Main St", "San Francisco", "42", 1)
    cursor = in_memory_db.cursor()
    cursor.execute("SELECT a.PostCode, a.Street, a.City, a.HouseNumber from adress a join contact c on a. ID = c.ID")
    result = cursor.fetchone()
    assert result[0] == '12345'
    assert result[1] == 'Main St'
    assert result[2] == 'San Francisco'
    assert result[3] == '42'


def test_insert_category(in_memory_db):
    """Test if user can insert Category in Table Kategorie"""
    insert = adress.Insert()
    insert.connection=in_memory_db
    insert.insert_Name("John", "Doe")
    insert.Insert_Category("Freund")
    cursor = in_memory_db.cursor()
    cursor.execute("SELECT a.Kategorie from Kategorie a join contact c on a. ID = c.ID")
    result = cursor.fetchone()
    assert result[0] == 'Freund'


def test_insert_phone_number(in_memory_db):
    """Test if user can insert PhoneNumber in Table PhoneNumber"""
    insert = adress.Insert()
    insert.connection=in_memory_db
    insert.insert_Name("John", "Doe")
    insert.insert_PhoneNumber("0644202010", 1)
    cursor = in_memory_db.cursor()
    cursor.execute("SELECT a.PhoneNumber from PhoneNumber a join contact c on a. ID = c.ID")
    result = cursor.fetchone()
    assert result[0] == '0644202010'

def insert_Name(self, first_name, last_name):
        """Method for inserting a name"""
        cur = self.connection.cursor()
        cur.execute("INSERT INTO Contact ('First_Name', 'LastName') values(?,?)", (first_name, last_name))
        self.contact_id = cur.lastrowid
        self.connection.commit()
