import sqlite3

class Ask():
    """Search for Records."""

    def __init__(self):
        self.connection = sqlite3.connect("database/adress.db")

    def askin(self, first_name, last_name):
        """Search for Records by First and Last Name"""
        cur = self.connection.cursor()
        query = """
            SELECT
	            a.First_Name,
	            a.LastName,
	            b.Street,
	            b.PostCode,
	            b.City,
	            b.HouseNumber,
	            c.PhoneNumber
            from Contact a
            join Adress b
	            on a.ID = b.Contact_ID
            join PhoneNumber c
	            on a.ID = c.Contact_ID
            where First_Name like "%s"
            and LastName like "%s"; """ % (first_name, last_name)

        cur.execute(query)
        self.contacts = cur.fetchall()
        self.connection.commit()
        print(self.contacts)

    def askin_all(self):
        """Search for all Records"""
        print("Vorname | Nachname |    Straße    |    PLZ    |    Ort    |   Haus-Nr.   |  Tel.:  |")
        cur = self.connection.cursor()
        query = """
            SELECT
	            a.First_Name,
	            a.LastName,
	            b.Street,
	            b.PostCode,
	            b.City,
	            b.HouseNumber,
	            c.PhoneNumber
            from Contact a
            join Adress b
	            on a.ID = b.Contact_ID
            join PhoneNumber c
	            on a.ID = c.Contact_ID """
     
        cur.execute(query)
        contacts = cur.fetchall()
        self.connection.commit()
     
        for contact in contacts:
            print(contact)
        
        return "--------------------------------------------------------"
