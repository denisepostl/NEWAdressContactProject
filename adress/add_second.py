import sqlite3


class AddSecondRecord():
    """Add Second Address | Phonenumber to Contact."""

    def __init__(self):
        self.connection = sqlite3.connect("database/adress_cat.db")

    def get_name_id(self, first_name, last_name, tel):
        """Method which return the ID of the contact"""
        cur = self.connection.cursor()
        query = """
            SELECT
	            c.ID
            from Contact c
            join PhoneNumber a
                on c.ID=a.Contact_ID
            join Adress b
                on b.Contact_ID = c.ID
            where First_Name like "%s" and LastName like "%s" and a.PhoneNumber like "%s"
        """ % (first_name, last_name, tel)
        cur.execute(query)
        ID = cur.fetchall()
        tup = ID[0]
        self.name_id = int(tup[0])
        self.connection.commit()
        return self.name_id

    def add_adress_(self, post_code, street, city, house_number, adr):
        """Add a second adress to the Contact."""
        cur = self.connection.cursor()
        cur.execute("INSERT INTO Adress ('PostCode', 'Street', 'City', 'Housenumber', 'Main_Adress', 'Contact_ID') values(?,?,?,?,?,?)", (post_code, street, city, house_number, adr, self.name_id))
        self.connection.commit()

    def add_phone(self, phone_number, tel):
        """Add a second phonenumber to the Contact."""
        cur = self.connection.cursor()
        cur.execute("INSERT INTO PhoneNumber ('PhoneNumber', 'Main_Tel', 'Contact_ID') values(?,?,?)", (phone_number, tel, self.name_id))
        self.connection.commit()
