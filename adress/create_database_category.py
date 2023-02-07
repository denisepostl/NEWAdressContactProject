import sqlite3


class Create_Contact():
    """Create Tables for database."""

    def __init__(self):
        """Initialize the database connection."""
        self.connection = sqlite3.connect("database/adress_category.db")

    def create_Contact(self):
        """This method is used to create Table Contact"""
        cur = self.connection.cursor()
        query = """
            CREATE TABLE Contact(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            First_Name VARCHAR,
            LastName VARCHAR,
            Kategorie_ID INTEGER,
            FOREIGN KEY(Kategorie_ID) REFERENCES Kategorie(ID));
        """
        cur.execute(query)
        self.connection.commit()

    def create_Phonenumber(self):
        """This method is used to create Table Phonennumber"""
        cur = self.connection.cursor()
        query = """
            CREATE TABLE PhoneNumber(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            PhoneNumber VARCHAR UNIQUE,
            Contact_ID INT,
            FOREIGN KEY(Contact_ID) REFERENCES Contact(ID));
        """
        cur.execute(query)
        self.connection.commit()

    def create_Adress(self):
        """This method is used to create Table Adress"""
        cur = self.connection.cursor()
        query = """
            CREATE TABLE Adress(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Street VARCHAR,
            PostCode VARCHAR,
            City VARCHAR,
            HouseNumber NVARCHAR,
            Contact_ID INT,
            FOREIGN KEY(Contact_ID) REFERENCES Contact(ID));
        """
        cur.execute(query)
        self.connection.commit()

    def create_Category(self):
        """This method is used to create Table Category"""
        cur = self.connection.cursor()
        query = """
            CREATE TABLE Kategorie(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Kategorie VARCHAR);
        """
        cur.execute(query)
        self.connection.commit()


def main():
    db = Create_Contact()
    db.create_Phonenumber()
    db.create_Contact()
    db.create_Adress()
    db.create_Category()


if __name__ == "__main__":
    main()
