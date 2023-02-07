import sqlite3


class Insert():
    """Insert Class."""

    def __init__(self):
        """Initialize connection do database"""
        self.connection = sqlite3.connect("database/adress_cat.db")

    def insert_Name(self, first_name, last_name):
        """Method for inserting a name"""
        cur = self.connection.cursor()
        cur.execute("INSERT INTO Contact ('First_Name', 'LastName') values(?,?)", (first_name, last_name))
        self.contact_id = cur.lastrowid
        self.connection.commit()

    def insert_Address(self, post_code, street, city, house_number, main_adress):
        """Method for inserting an adress"""
        cur = self.connection.cursor()
        cur.execute("INSERT INTO Adress ('PostCode', 'Street', 'City', 'Housenumber', 'Main_Adress', 'Contact_ID') values(?,?,?,?,?,?)", (post_code, street, city, house_number, main_adress, self.contact_id))
        self.connection.commit()

    def Insert_Category(self, category):
        """Method for inserting a category"""
        cur = self.connection.cursor()
        cur.execute("INSERT INTO Kategorie ('Kategorie', 'Contact_ID') values(?,?)", (category, self.contact_id))
        self.connection.commit()

    def insert_PhoneNumber(self, phone_number, main_tel):
        """Method for inserting a Phone Number"""
        cur = self.connection.cursor()
        cur.execute("INSERT INTO PhoneNumber ('PhoneNumber', 'Main_Tel', 'Contact_ID') values(?,?,?)", (phone_number, main_tel, self.contact_id))
        self.connection.commit()
