import sqlite3


class CalculateID:
    """Calculate the ID for the command line program."""

    def __init__(self):
        self.connection = sqlite3.connect("database/adress.db")

    def calculate_phone_id(self):
        """This method calculates the phone_id that the user can add contacts comfortable."""
        cur = self.connection.cursor()
        id = """
            SELECT
                Max(ID)
            from PhoneNumber
        """
        cur.execute(id)
        ID = cur.fetchall()
        tup = ID[0]
        self.New_ID = int(tup[0]) + int(1)
        self.connection.commit()

    def calculate_contact_id(self):
        """This method calculates the contact_id that the user can add contacts comfortable."""
        cur = self.connection.cursor()
        id = """
            SELECT
                Max(ID)
            from Contact
        """
        cur.execute(id)
        ID = cur.fetchall()
        tup = ID[0]
        self.My_ID = int(tup[0]) + int(1)
        self.connection.commit()

    def calculate_adress_id(self):
        """This method calculates the adress_id that the user can add contacts comfortable."""
        cur = self.connection.cursor()
        id = """
            SELECT
                Max(ID)
            from Adress
        """
        cur.execute(id)
        ID = cur.fetchall()
        tup = ID[0]
        self.New_ID = int(tup[0]) + int(1)
        self.connection.commit()
