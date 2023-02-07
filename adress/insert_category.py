import sqlite3

class Insert():

    def __init__(self):
        self.connection = sqlite3.connect("database/adress_cat.db")


    def insert_Name(self, first_name, last_name):
        cur = self.connection.cursor()
        cur.execute("INSERT INTO Contact ('First_Name', 'LastName') values(?,?)", (first_name, last_name))
        self.contact_id = cur.lastrowid
        self.connection.commit()


    def insert_Address(self, post_code, street, city, house_number):
        cur = self.connection.cursor()
        cur.execute("INSERT INTO Adress ('PostCode', 'Street', 'City', 'Housenumber', 'Contact_ID') values(?,?,?,?,?)", (post_code, street, city, house_number, self.contact_id))
        self.connection.commit()

    def insert_PhoneNumber(self, phone_number):
        cur = self.connection.cursor()
        cur.execute("INSERT INTO PhoneNumber ('PhoneNumber', 'Contact_ID') values(?,?)", (phone_number, self.contact_id))
        self.connection.commit()

    def Insert_Category(self, category):
        cur = self.connection.cursor()
        cur.execute("INSERT INTO Kategorie ('Kategorie', 'Contact_ID') values(?,?)", (category, self.contact_id))
        self.connection.commit()