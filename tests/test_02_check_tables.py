import sqlite3
import pytest
import logging


def test_if_tables_exists():
    """Test if the Tables exist in adress.db"""

    conn = sqlite3.connect('database/adress.db')
    c = conn.cursor()
    c.execute("""
        SELECT ID, First_Name, LastName
        FROM Contact;
    """, )

    c.execute("""
        SELECT ID, Street, PostCode, City, HouseNumber, Contact_ID
        FROM Adress;
    """, )

    c.execute("""
        SELECT ID, PhoneNumber, Contact_ID
        FROM PhoneNumber;
    """, )
    ret = bool(c.fetchone())
    conn.close()
    return ret


def test_if_tables_exists_category():
    """Test if the Tables exist in adress_cat.db"""

    conn = sqlite3.connect('database/adress_cat.db')
    c = conn.cursor()
    c.execute("""
        SELECT ID, First_Name, LastName
        FROM Contact;
    """, )

    c.execute("""
        SELECT ID, Street, PostCode, City, HouseNumber, Main_Adress, Contact_ID
        FROM Adress;
    """, )

    c.execute("""
        SELECT ID, PhoneNumber, Main_Tel, Contact_ID
        FROM PhoneNumber;
    """, )

    c.execute("""
        SELECT ID, Kategorie, Contact_ID
        FROM Kategorie;
    """, )
    ret = bool(c.fetchone())
    conn.close()
    return ret
