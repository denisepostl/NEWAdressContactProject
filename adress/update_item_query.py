import sqlite3

class Update_Select():

    def __init__(self):
        self.connection = sqlite3.connect("database/adress.db")
        

    def names(self):
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
        
        
        self.f_name = str(contacts[0][0])
        self.l_name = str(contacts[0][1])
        self.street = str(contacts[0][2])
        self.post_code = str(contacts[0][3])
        self.city = str(contacts[0][4])
        self.house_nr = str(contacts[0][5])
        self.phone_nr = str(contacts[0][6])