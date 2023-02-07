import sqlite3

class QuerySearchBy():
    """Class for Searching Records by Name | Phonenumber or askin all"""

    def __init__(self):
        self.connection = sqlite3.connect("database/adress_cat.db")

    def askin_query(self, first_name, last_name):
        """Asking for a contact by first and last name"""
        cur = self.connection.cursor()
        query = """
            SELECT
                a.ID,
	            a.First_Name,
	            a.LastName,
                b.PostCode,
                b.City,
	            b.Street,
	            b.HouseNumber,
	            c.PhoneNumber,
                d.Kategorie
            from Contact a
            join Adress b
	            on a.ID = b.Contact_ID
            join PhoneNumber c
	            on a.ID = c.Contact_ID
            join Kategorie d
                on a.ID = d.Contact_ID
            where First_Name like "%s" and LastName like "%s" """ % (first_name, last_name,)

        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()

    def askin_phone_query(self, phone):
        """Search for a contact by Phone Number."""
        cur = self.connection.cursor()
        query = """
            SELECT
                a.ID,
	            a.First_Name,
	            a.LastName,
                b.PostCode,
                b.City,
	            b.Street,
	            b.HouseNumber,
	            c.PhoneNumber,
                d.Kategorie
            from Contact a
            join Adress b
	            on a.ID = b.Contact_ID
            join PhoneNumber c
	            on a.ID = c.Contact_ID
            join Kategorie d
                on a.ID = d.Contact_ID
            where PhoneNumber like "%s" """ % (phone,)

        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()

    def askin_category_query(self, category):
        """Search for a contact by Kategorie."""
        cur = self.connection.cursor()
        query = """
            SELECT
                a.ID,
	            a.First_Name,
	            a.LastName,
                b.PostCode,
                b.City,
	            b.Street,
	            b.HouseNumber,
	            c.PhoneNumber,
                d.Kategorie
            from Contact a
            join Adress b
	            on a.ID = b.Contact_ID
            join PhoneNumber c
	            on a.ID = c.Contact_ID
            join Kategorie d
                on a.ID = d.Contact_ID
            where Kategorie like "%s" """ % (category,)

        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()

    def askin_all_query(self):
        """Search for all contacts."""
        cur = self.connection.cursor()
        query = """
            SELECT
                a.ID,
	            a.First_Name,
	            a.LastName,
                b.PostCode,
                b.City,
	            b.Street,
	            b.HouseNumber,
	            c.PhoneNumber,
                d.Kategorie
            from Contact a
            join Adress b
	            on a.ID = b.Contact_ID
            join PhoneNumber c
	            on a.ID = c.Contact_ID
            join Kategorie d
                on a.ID = d.Contact_ID """

        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()

    def askin_by_id(self, id):
        """Asking for a contact by id"""
        cur = self.connection.cursor()
        query = """
            SELECT
                a.ID,
	            a.First_Name,
	            a.LastName,
                b.PostCode,
                b.City,
	            b.Street,
	            b.HouseNumber,
	            c.PhoneNumber,
                d.Kategorie
            from Contact a
            join Adress b
	            on a.ID = b.Contact_ID
            join PhoneNumber c
	            on a.ID = c.Contact_ID
            join Kategorie d
                on a.ID = d.Contact_ID
            where a.ID = %d
            """ % (id)

        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()

    def querybyphone(self, tel):
        cur = self.connection.cursor()
        query = """
            WITH Adress_Phone AS (
            SELECT 
                Contact.ID, Contact.First_Name, Contact.LastName, 
                COUNT(Adress.ID) AS Adress_Count, 
                COUNT(PhoneNumber.ID) AS PhoneNumber_Count
            FROM Contact
            LEFT JOIN Adress ON Contact.ID = Adress.Contact_ID
            LEFT JOIN PhoneNumber ON Contact.ID = PhoneNumber.Contact_ID
            GROUP BY Contact.ID
            )
            SELECT 
            Contact.ID,
            Contact.First_Name, Contact.LastName, 
            Adress1.Street || ', ' || Adress1.PostCode || ', ' || Adress1.City || ', ' || Adress1.HouseNumber AS Adress1,
            Adress2.Street || ', ' || Adress2.PostCode || ', ' || Adress2.City || ', ' || Adress2.HouseNumber AS Adress2,
            PhoneNumber1.PhoneNumber AS Tel1,
            PhoneNumber2.PhoneNumber AS Tel2,
            Kategorie.Kategorie
            FROM Adress_Phone
			JOIN PhoneNumber ON Contact.ID = PhoneNumber.Contact_ID
            JOIN Kategorie ON Contact.ID = Kategorie.Contact_ID
            JOIN Contact ON Adress_Phone.ID = Contact.ID
            LEFT JOIN Adress Adress1 ON Adress_Phone.ID = Adress1.Contact_ID AND Adress1.Main_Adress = 1
            LEFT JOIN Adress Adress2 ON Adress_Phone.ID = Adress2.Contact_ID AND Adress2.Main_Adress = 0
            LEFT JOIN PhoneNumber PhoneNumber1 ON Adress_Phone.ID = PhoneNumber1.Contact_ID AND PhoneNumber1.Main_Tel = 1
            LEFT JOIN PhoneNumber PhoneNumber2 ON Adress_Phone.ID = PhoneNumber2.Contact_ID AND PhoneNumber2.Main_Tel = 0
            WHERE (Adress_Phone.Adress_Count > 0 OR Adress_Phone.PhoneNumber_Count > 0)
            AND PhoneNumber.PhoneNumber like "%s"
        """%(tel)
        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()

    def querycat(self, kat):
        cur = self.connection.cursor()
        query = """
            WITH Adress_Phone AS (
            SELECT 
                Contact.ID, Contact.First_Name, Contact.LastName, 
                COUNT(Adress.ID) AS Adress_Count, 
                COUNT(PhoneNumber.ID) AS PhoneNumber_Count
            FROM Contact
            LEFT JOIN Adress ON Contact.ID = Adress.Contact_ID
            LEFT JOIN PhoneNumber ON Contact.ID = PhoneNumber.Contact_ID
            GROUP BY Contact.ID
            )
            SELECT 
            Contact.ID,
            Contact.First_Name, Contact.LastName, 
            Adress1.Street || ', ' || Adress1.PostCode || ', ' || Adress1.City || ', ' || Adress1.HouseNumber AS Adress1,
            Adress2.Street || ', ' || Adress2.PostCode || ', ' || Adress2.City || ', ' || Adress2.HouseNumber AS Adress2,
            PhoneNumber1.PhoneNumber AS Tel1,
            PhoneNumber2.PhoneNumber AS Tel2,
            Kategorie.Kategorie
            FROM Adress_Phone
            JOIN Kategorie ON Contact.ID = Kategorie.Contact_ID
            JOIN Contact ON Adress_Phone.ID = Contact.ID
            LEFT JOIN Adress Adress1 ON Adress_Phone.ID = Adress1.Contact_ID AND Adress1.Main_Adress = 1
            LEFT JOIN Adress Adress2 ON Adress_Phone.ID = Adress2.Contact_ID AND Adress2.Main_Adress = 0
            LEFT JOIN PhoneNumber PhoneNumber1 ON Adress_Phone.ID = PhoneNumber1.Contact_ID AND PhoneNumber1.Main_Tel = 1
            LEFT JOIN PhoneNumber PhoneNumber2 ON Adress_Phone.ID = PhoneNumber2.Contact_ID AND PhoneNumber2.Main_Tel = 0
            WHERE (Adress_Phone.Adress_Count > 0 OR Adress_Phone.PhoneNumber_Count > 0)
            AND Kategorie.Kategorie like "%s"
        """%(kat)
        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()

    def querybyid(self, id):
        cur = self.connection.cursor()
        query = """
            WITH Adress_Phone AS (
            SELECT 
                Contact.ID, Contact.First_Name, Contact.LastName, 
                COUNT(Adress.ID) AS Adress_Count, 
                COUNT(PhoneNumber.ID) AS PhoneNumber_Count
            FROM Contact
            LEFT JOIN Adress ON Contact.ID = Adress.Contact_ID
            LEFT JOIN PhoneNumber ON Contact.ID = PhoneNumber.Contact_ID
            GROUP BY Contact.ID
            )
            SELECT 
            Contact.ID,
            Contact.First_Name, Contact.LastName, 
            Adress1.Street || ', ' || Adress1.PostCode || ', ' || Adress1.City || ', ' || Adress1.HouseNumber AS Adress1,
            Adress2.Street || ', ' || Adress2.PostCode || ', ' || Adress2.City || ', ' || Adress2.HouseNumber AS Adress2,
            PhoneNumber1.PhoneNumber AS Tel1,
            PhoneNumber2.PhoneNumber AS Tel2,
            Kategorie.Kategorie
            FROM Adress_Phone
            JOIN Kategorie ON Contact.ID = Kategorie.Contact_ID
            JOIN Contact ON Adress_Phone.ID = Contact.ID
            LEFT JOIN Adress Adress1 ON Adress_Phone.ID = Adress1.Contact_ID AND Adress1.Main_Adress = 1
            LEFT JOIN Adress Adress2 ON Adress_Phone.ID = Adress2.Contact_ID AND Adress2.Main_Adress = 0
            LEFT JOIN PhoneNumber PhoneNumber1 ON Adress_Phone.ID = PhoneNumber1.Contact_ID AND PhoneNumber1.Main_Tel = 1
            LEFT JOIN PhoneNumber PhoneNumber2 ON Adress_Phone.ID = PhoneNumber2.Contact_ID AND PhoneNumber2.Main_Tel = 0
            WHERE (Adress_Phone.Adress_Count > 0 OR Adress_Phone.PhoneNumber_Count > 0)
            AND Contact.ID like "%d"
        """%(id)
        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()

    def querybyname(self, firstname, lastname):
        cur = self.connection.cursor()
        query = """
            WITH Adress_Phone AS (
            SELECT 
                Contact.ID, Contact.First_Name, Contact.LastName, 
                COUNT(Adress.ID) AS Adress_Count, 
                COUNT(PhoneNumber.ID) AS PhoneNumber_Count
            FROM Contact
            LEFT JOIN Adress ON Contact.ID = Adress.Contact_ID
            LEFT JOIN PhoneNumber ON Contact.ID = PhoneNumber.Contact_ID
            GROUP BY Contact.ID
            )
            SELECT 
            Contact.ID,
            Contact.First_Name, Contact.LastName, 
            Adress1.Street || ', ' || Adress1.PostCode || ', ' || Adress1.City || ', ' || Adress1.HouseNumber AS Adress1,
            Adress2.Street || ', ' || Adress2.PostCode || ', ' || Adress2.City || ', ' || Adress2.HouseNumber AS Adress2,
            PhoneNumber1.PhoneNumber AS Tel1,
            PhoneNumber2.PhoneNumber AS Tel2,
            Kategorie.Kategorie
            FROM Adress_Phone
            JOIN Kategorie ON Contact.ID = Kategorie.Contact_ID
            JOIN Contact ON Adress_Phone.ID = Contact.ID
            LEFT JOIN Adress Adress1 ON Adress_Phone.ID = Adress1.Contact_ID AND Adress1.Main_Adress = 1
            LEFT JOIN Adress Adress2 ON Adress_Phone.ID = Adress2.Contact_ID AND Adress2.Main_Adress = 0
            LEFT JOIN PhoneNumber PhoneNumber1 ON Adress_Phone.ID = PhoneNumber1.Contact_ID AND PhoneNumber1.Main_Tel = 1
            LEFT JOIN PhoneNumber PhoneNumber2 ON Adress_Phone.ID = PhoneNumber2.Contact_ID AND PhoneNumber2.Main_Tel = 0
            WHERE (Adress_Phone.Adress_Count > 0 OR Adress_Phone.PhoneNumber_Count > 0)
            AND Contact.First_Name = "%s" AND Contact.LastName = "%s"
        """%(firstname, lastname)
        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()


    def askin_all(self):
        cur = self.connection.cursor()
        query = """
            WITH Adress_Phone AS (
            SELECT 
                Contact.ID, Contact.First_Name, Contact.LastName, 
                COUNT(Adress.ID) AS Adress_Count, 
                COUNT(PhoneNumber.ID) AS PhoneNumber_Count
            FROM Contact
            LEFT JOIN Adress ON Contact.ID = Adress.Contact_ID
            LEFT JOIN PhoneNumber ON Contact.ID = PhoneNumber.Contact_ID
            GROUP BY Contact.ID
            )
            SELECT 
            Contact.ID,
            Contact.First_Name, Contact.LastName, 
            Adress1.Street || ', ' || Adress1.PostCode || ', ' || Adress1.City || ', ' || Adress1.HouseNumber AS Adress1,
            Adress2.Street || ', ' || Adress2.PostCode || ', ' || Adress2.City || ', ' || Adress2.HouseNumber AS Adress2,
            PhoneNumber1.PhoneNumber AS Tel1,
            PhoneNumber2.PhoneNumber AS Tel2,
            Kategorie.Kategorie
            FROM Adress_Phone
            JOIN Kategorie ON Contact.ID = Kategorie.Contact_ID
            JOIN Contact ON Adress_Phone.ID = Contact.ID
            LEFT JOIN Adress Adress1 ON Adress_Phone.ID = Adress1.Contact_ID AND Adress1.Main_Adress = 1
            LEFT JOIN Adress Adress2 ON Adress_Phone.ID = Adress2.Contact_ID AND Adress2.Main_Adress = 0
            LEFT JOIN PhoneNumber PhoneNumber1 ON Adress_Phone.ID = PhoneNumber1.Contact_ID AND PhoneNumber1.Main_Tel = 1
            LEFT JOIN PhoneNumber PhoneNumber2 ON Adress_Phone.ID = PhoneNumber2.Contact_ID AND PhoneNumber2.Main_Tel = 0
            WHERE Adress_Phone.Adress_Count > 0 OR Adress_Phone.PhoneNumber_Count > 0
        """ 
        cur.execute(query)
        self.contact = cur.fetchall()
        self.connection.commit()

