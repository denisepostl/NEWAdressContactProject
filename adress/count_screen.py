import sqlite3

class Counting():
    def __init__(self):
        """Initialize database connection."""
        self.connection = sqlite3.connect("database/adress_cat.db")

    def get_school(self):
        """This method is used to cound all Members of Kategorie 'Schule'."""
        cur = self.connection.cursor()
        get_id = """
            SELECT
	            Count(Kategorie)
            from Kategorie
            where Kategorie like "Schule";
        """ 
        cur.execute(get_id)
        
        ID = cur.fetchall()
        tup = ID[0]
        self.school = int(tup[0])
        self.connection.commit()

        return self.school

    def get_family(self):
        """This method is used to cound all Members of Kategorie 'Familie'."""
        cur = self.connection.cursor()
        get_id = """
            SELECT
	            Count(Kategorie)
            from Kategorie
            where Kategorie like "Familie";
        """ 
        cur.execute(get_id)
        
        ID = cur.fetchall()
        tup = ID[0]
        self.family = int(tup[0])
        self.connection.commit()

        return self.family
    
    def get_work(self):
        """This method is used to cound all Members of Kategorie 'Arbeit'."""
        cur = self.connection.cursor()
        get_id = """
            SELECT
	            Count(Kategorie)
            from Kategorie
            where Kategorie like "Arbeit";
        """ 
        cur.execute(get_id)
        
        ID = cur.fetchall()
        tup = ID[0]
        self.work = int(tup[0])
        self.connection.commit()

        return self.work

    def get_friends(self):
        """This method is used to cound all Members of Kategorie 'Freunde'."""
        cur = self.connection.cursor()
        get_id = """
            SELECT
	            Count(Kategorie)
            from Kategorie
            where Kategorie like "Freunde";
        """ 
        cur.execute(get_id)
        
        ID = cur.fetchall()
        tup = ID[0]
        self.friend = int(tup[0])
        self.connection.commit()

        return self.friend
