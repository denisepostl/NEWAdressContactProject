import sqlite3

class Accept_Adress():

    def __init__(self):
        self.connection = sqlite3.connect("database/adress_cat.db")

    def get_id_for_check(self, first_name, last_name, tel):
        """This method is used to return the id from record when the user wants to update a record."""
        cur = self.connection.cursor()
        get_id = """
            SELECT
	            a.ID
            from Contact a
            join PhoneNumber c
                on c.Contact_ID = a.ID
            where a.First_Name like "%s"
            and a.LastName like "%s" and c.PhoneNumber like "%s";
        """ %(first_name, last_name, tel)

        cur.execute(get_id)
        
        ID = cur.fetchall()
        tup = ID[0]
        self.My_ID = int(tup[0])
        self.connection.commit()

        return self.My_ID

    def get_count_adr(self):
        """Method which check if user is able to add another adr or tel"""
        cur = self.connection.cursor()
        query = """
            SELECT
	            Count(Contact_ID)
            from Adress
            where Contact_ID="%d"
        """ % (self.My_ID)
        cur.execute(query)
        ID = cur.fetchall()
        tup = ID[0]
        self.c_id = int(tup[0])
        self.connection.commit()
        return self.c_id
    
    def get_count_tel(self):
        """Method which check if user is able to add another adr or tel"""
        cur = self.connection.cursor()
        query = """
            SELECT
	            Count(Contact_ID)
            from PhoneNumber
            where Contact_ID="%d"
        """ % (self.My_ID)
        cur.execute(query)
        ID = cur.fetchall()
        tup = ID[0]
        self.tc_id = int(tup[0])
        self.connection.commit()
        return self.tc_id