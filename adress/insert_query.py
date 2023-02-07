import sqlite3
from adress.calculate_id import CalculateID

class Add(CalculateID):

    def __init__(self):
        self.connection = sqlite3.connect("database/adress.db")

    def add_Name(self, ID, first_name, last_name):
        cur = self.connection.cursor()
        query = """
            INSERT INTO Contact(ID, First_Name, LastName)
            VALUES(%d, "%s", "%s"); """ %(ID, first_name, last_name)
        
        cur.execute(query)
        self.connection.commit()


    def add_Address(self, street, post_code, city, house_number, Contact_ID):
        cur = self.connection.cursor()
        self.calculate_adress_id()

        query = """
            INSERT INTO Adress(ID, Street, PostCode, City, Housenumber, Contact_ID)
            VALUES(%d, "%s", "%s", "%s", "%s", %d); """ %(self.New_ID, street, post_code, city, house_number, Contact_ID)
        
        cur.execute(query)
        self.connection.commit()


    def add_PhoneNumber(self, phone_number, Contact_ID):
        cur = self.connection.cursor()
        self.calculate_phone_id()
        query = """
            INSERT INTO PhoneNumber(ID, PhoneNumber, Contact_ID)
            VALUES(%d, "%s", %d); """ %(self.New_ID, phone_number, Contact_ID)
        
        cur.execute(query)
        self.connection.commit()
