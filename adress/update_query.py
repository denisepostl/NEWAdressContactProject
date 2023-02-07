import sqlite3

class Update():

    def __init__(self):
        self.connection = sqlite3.connect("database/adress.db")


    def update_first_name(self, value, first_name, last_name):
        """This method is used to update first name record in contact table by first- and lastname."""
        cur = self.connection.cursor()
        query = """
            UPDATE Contact
            SET First_Name = "%s"
            WHERE First_Name = "%s"
            and LastName = "%s"; 
        """ %(value, first_name, last_name)

        cur.execute(query)
        self.connection.commit()

    def update_last_name(self, value, first_name, last_name):
        """This method is used to update last name record in contact table by first- and lastname."""
        cur = self.connection.cursor()
        query = """
            UPDATE Contact
            SET LastName = "%s"
            WHERE First_Name = "%s"
            and LastName = "%s"; 
        """ %(value, first_name, last_name)

        cur.execute(query)
        self.connection.commit()

    def get_add_id(self, first_name, last_name):
        """This method is used to get contact_id."""
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
        self.IDA = int(tup[0])
        self.connection.commit()

        return self.IDA
        
    def update_street(self, value):
        """This method is used to update street record in adress table."""
        cur = self.connection.cursor()
        
        update_by_ID = """
            UPDATE Adress
	        SET Street = "%s"
            where Contact_ID like "%s";
        """ %(value, self.IDA)

        cur.execute(update_by_ID)
        self.connection.commit()
        
    
    def update_housenumber(self, value):
        """This method is used to update housenumber record in adress table."""
        cur = self.connection.cursor()
        
        update_by_ID = """
            UPDATE Adress
	        SET HouseNumber = "%s"
            where Contact_ID like "%s";
        """ %(value, self.IDA)

        cur.execute(update_by_ID)
        self.connection.commit()
        
    
    def update_ort(self, value):
        """This method is used to update ort record in adress table."""
        cur = self.connection.cursor()
        
        update_by_ID = """
            UPDATE Adress
	        SET City = "%s"
            where Contact_ID like "%s";
        """ %(value, self.IDA)

        cur.execute(update_by_ID)
        self.connection.commit()
        
    
    def update_plz(self, value):
        """This method is used to update plz record in adress table."""
        cur = self.connection.cursor()
        
        update_by_ID = """
            UPDATE Adress
	        SET PostCode = "%s"
            where Contact_ID like "%s";
        """ %(value, self.IDA)

        cur.execute(update_by_ID)
        self.connection.commit()


    def get_id(self, first_name, last_name):
        """This method is used to get Contact_ID."""
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
        
    
    def update_tel(self, value):
        """This method is used to update phonenumber record in phonennumber table."""
        cur = self.connection.cursor()
        
        update_by_ID = """
            UPDATE PhoneNumber
	        SET PhoneNumber = "%s"
            where Contact_ID like "%s";
        """ %(value, self.ID)

        cur.execute(update_by_ID)
        self.connection.commit()
