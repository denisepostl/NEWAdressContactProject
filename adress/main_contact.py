import sqlite3
from adress.calculate_id import CalculateID
from adress.insert_query import Add
from adress.query import Ask
from adress.update_query import Update
from adress.delete import Delete

class Contact(Add, Ask, Delete, CalculateID, Update):
    """This is a little command line program which allows you to inserting, update, query and delete records."""  

    def __init__(self):
        self.connection = sqlite3.connect("database/adress.db")

    def add_Contact(self):
        while True:
            print("Bitte wählen Sie die gewünschte Option")
            print("---------------------------------------------------------------------------")
            menü = input("(1) Kontakt hinzufügen \n(2) Kontakt abfragen \n(3) Kontaktdaten ändern \n(4) Kontakt löschen\n(5) Beenden\n\n")
            #------------------------------ ADD CONTACT ------------------------------#
            if menü == "1":
                value = input("Möchten Sie einen neuen Kontakt hinzufügen? [J/N]: " )
                if value == "J":
                #------------------------------ ADD Name ------------------------------#
                    self.calculate_contact_id()
                
                    first_name = str(input("Vorname: "))
                    last_name = str(input("Nachname: "))
                
                    self.add_Name(self.My_ID, first_name, last_name)

                #------------------------------ ADD ADDRESS ------------------------------#
                
                    street = str(input("Straße: "))
                    post_code = int(input("Postleitzahl: "))
                    city = str(input("Stadt: "))
                    house_number = int(input("Hausnummer: "))

                    self.add_Address(street, post_code, city, house_number, self.My_ID)

                #------------------------------ ADD PHONE NUMBER ------------------------------#
                    phone_number = str(input("Telefonnummer: "))

                    self.add_PhoneNumber(phone_number, self.My_ID)
                
                    print("Ihr Kontakt wurde erfolgreich hinzugefügt!")
                
                else:
                    inp = input(("Wollen Sie das Programm beenden? [J/N]: "))
                    if inp == "J":
                        break
                    print("Das Programm wird nun beendet!")

            #------------------------------ ASK CONTACT ------------------------------#
            elif menü == "2":
                print("---------------------------------------------------------------------------")
                wahl = input("(1) Einen Kontakt abfragen\n(2) Alle Kontakte abfragen\n\n")

                if wahl == "1":
                    value = input("Möchten Sie einen Kontakt abfragen? [J/N]: ")

                    if value == "J":
                        first_name = str(input("Vorname: "))
                        last_name = str(input("Nachname: "))
                        print("____________________________________________________________________________\n")
                        print(self.askin(first_name, last_name)) 
                        print("____________________________________________________________________________\n")

                elif wahl == "2":
                    value = input("Möchten Sie alle Kontakte abfragen? [J/N]: ")
                
                    if value == "J":
                        print("____________________________________________________________________________\n")
                        print(self.askin_all()) 
                        print("____________________________________________________________________________\n")

                else:
                    inp = input(("Wollen Sie das Programm beenden? [J/N]: "))
                    if inp == "J":
                        break
                    print("Das Programm wird nun beendet!")

            #------------------------------ EDIT CONTACT ------------------------------#
            elif menü == "3":
                first_name = input("Bitte geben Sie den Vornamen ihres Kontakts ein: ")
                last_name = input("Bitte geben Sie den Nachnamen ihres Kontakts ein: ")
                print(self.askin(first_name, last_name))
                inp = input("Ist das Ihr richtiger Kontakt? [J/N]: ")
                
                if inp == "J":
                
                    print("Bitte wählen Sie aus welche Daten Sie aktualisieren möchten? (STOP beendet)")
                    wahl = input("(1) Vorname\n(2) Nachname\n(3) Straße\n(4) PLZ \n(5) Ort\n(6) Haus-Nr.\n(7) Tel.:\n\n")
               
                    if wahl == "1":
                        value = str(input("Vorname: "))
                        self.update_first_name(value, first_name, last_name)
                        
                    elif wahl == "2":
                        value = str(input("Nachname: "))
                        self.update_last_name(value, first_name, last_name)
                    elif wahl == "3":
                        value = str(input("Straße: "))
                        self.get_add_id(first_name, last_name)
                        self.update_street(value)
                    elif wahl == "4":
                        value = str(input("PLZ: "))
                        self.get_add_id(first_name, last_name)
                        self.update_plz(value)
                    elif wahl == "5":
                        value = str(input("Ort: "))
                        self.get_add_id(first_name, last_name)
                        self.update_ort(value)
                    elif wahl == "6":
                        value = str(input("Haus-Nr.: "))
                        self.get_add_id(first_name, last_name)
                        self.update_housenumber(value)
                    elif wahl == "7":
                        value = str(input("Tel.: "))
                        self.get_id(first_name, last_name)
                        self.update_tel(value)
                    elif wahl == "STOP":
                        break
            #------------------------------ DELETE CONTACT ------------------------------#
            elif menü == "4":
                first_name = input("Bitte geben Sie den Vornamen ihres Kontakts ein: ")
                last_name = input("Bitte geben Sie den Nachnamen ihres Kontakts ein: ")
                print(self.askin(first_name, last_name))
                inp = input("Ist das Ihr richtiger Kontakt? [J/N]: ")
                if inp == "J":
                    self.get_del_id(first_name, last_name)
                    self.delete_adress()
                    self.delete_phonenumber()
                    self.delete_contact(first_name, last_name)
                    print("Ihr Kontakt wurde erfolgreich gelöscht")

            #------------------------------ QUIT PROGRAM ------------------------------#
            elif menü == "5":
                inp = input(("Wollen Sie das Programm beenden? [J/N]: "))
                if inp == "J":
                    break
                print("Das Programm wird nun beendet!")

        return "Ihre Kontakte wurden erfolgreich hinzugefügt!\n\n" 


if __name__ == "__main__":
    c = Contact()
    print(c.add_Contact())
