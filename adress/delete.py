import sqlite3

class Delete():

    def __init__(self):
        """Initialize database connection."""
        self.connection = sqlite3.connect("database/adress.db")

    def get_del_id(self, first_name, last_name):
        """This method is used to return the id from record when the user wants to delete a record by first- and last name."""
        cur = self.connection.cursor()
        get_id = """
            SELECT
	            a.ID
            from Contact a
            where a.First_Name like "%s"
            and a.LastName like "%s";
        """ %(first_name, last_name)

        cur.execute(get_id)
        
        ID = cur.fetchall()
        tup = ID[0]
        self.ID = int(tup[0])
        self.connection.commit()

        return self.ID
        

    def delete_contact(self, first_name, last_name):
        """This method is used for deleting a record in contact table."""
        cur = self.connection.cursor()
        query = """
            DELETE FROM Contact
            where First_Name like "%s"
            and LastName like "%s"
        """ %(first_name, last_name)
        cur.execute(query)
        self.connection.commit()

    def delete_adress(self):
        """This method is used for deleting a record in adress table."""
        cur = self.connection.cursor()
        query = """
            DELETE FROM Adress
            where Contact_ID like "%d"
        """ %(self.ID)
        cur.execute(query)
        self.connection.commit()

    def delete_phonenumber(self):
        """This method is used for deleting a record in phonenumber table."""
        cur = self.connection.cursor()
        query = """
            DELETE FROM PhoneNumber
            where Contact_ID like "%d"
        """ %(self.ID)
        cur.execute(query)
        self.connection.commit()