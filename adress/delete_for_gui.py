import sqlite3


class Delete_Contact():
    """Delete Records by Contact_ID"""

    def __init__(self):
        """Initialize connection do database"""
        self.connection = sqlite3.connect("database/adress_cat.db")

    def delete_adress(self, id):
        """Method for deleting an adress"""
        cur = self.connection.cursor()
        cur.execute("Delete from Adress where Contact_ID = %s" % (id))
        self.contact_id = cur.lastrowid
        self.connection.commit()

    def delete_phonenumber(self, id):
        """Method for deleting a phonenumber"""
        cur = self.connection.cursor()
        cur.execute("Delete from PhoneNumber where Contact_ID = %s" % (id))
        self.contact_id = cur.lastrowid
        self.connection.commit()

    def delete_category(self, id):
        """Method for deleting a category"""
        cur = self.connection.cursor()
        cur.execute("Delete from Kategorie where Contact_ID = %s" % (id))
        self.contact_id = cur.lastrowid
        self.connection.commit()
