import sqlite3
from tkinter import messagebox

class Checking():
    """Checking Class."""

    def __init__(self):
        """Initialize connection do database"""
        self.connection = sqlite3.connect("database/adress_cat.db")

    def check_for_same_tel(self, same_phone):
        """Method for searching for same phone"""
        cur = self.connection.cursor()
        query = """
                SELECT
	                a.PhoneNumber
                from PhoneNumber a 
                where a.PhoneNumber like %s
        """% (same_phone)
        cur.execute(query)
        self.same_phone_ = cur.fetchall()
        return self.same_phone_
       

    def check_for_same_name(self, first_name, last_name):
        """Method for searching for same name"""
        cur = self.connection.cursor()
        query = """
                SELECT
	                First_Name,
	                LastName
                from Contact 
                where First_Name like "%s" and LastName like "%s"
        """%(first_name, last_name,)
        cur.execute(query)
        self.name = cur.fetchall()
        self.connection.commit()
        return self.name
    
    def get_second_tel(self, firstname, lastname, tel):
        """Method for searching for second tel"""
        cur = self.connection.cursor()
        query = """
                SELECT
	                a.PhoneNumber
                from PhoneNumber a
                join Contact b
                    on b.ID = a.Contact_ID
                where a.Main_Tel = 0 and b.First_Name="%s" and b.LastName="%s" and a.PhoneNumber = "%s" 
        """%(firstname, lastname, tel)
        cur.execute(query)
        self.telmain = cur.fetchall()
        self.connection.commit()
        return self.telmain
    
    def get_second_adr(self, firstname, lastname, tel):
        """Method for searching for second adress"""
        cur = self.connection.cursor()
        query = """
                SELECT
	                a.Street,
	                a.PostCode,
	                a.HouseNumber,
	                a.City
                from Adress a
                join Contact b
                    on b.ID = a.Contact_ID
                join PhoneNumber d
                    on d.Contact_ID = b.ID
                where a.Main_Adress = 0 and b.First_Name="%s" and b.LastName="%s" and d.PhoneNumber = "%s"
        """%(firstname, lastname, tel)
        cur.execute(query)
        self.adrmain = cur.fetchall()
        self.connection.commit()
        return self.adrmain
