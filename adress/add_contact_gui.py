"""Class for the Add Functionality to insert a Contact in database."""

from tkinter import ttk 
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

from tkinter import filedialog
from tkinter import messagebox
import re
from PIL import Image, ImageTk
import sqlite3
from adress.add_for_gui import Insert
from adress.add_check import Checking

Profile = {1: ""}


class MainWin(Insert, Checking):
    """Class for Adding a Contact in database."""

    def __init__(self):
        """Initializing important attributes"""
        # connect with database
        self.connection = sqlite3.connect("database/adress_cat.db")
        # create Window and define details like title, geometry and colors
        self.win = Tk()
        self.win.title = ("Adress-Management")
        self.win.geometry('800x600')
        self.co0 = "#ffffff"
        self.co1 = "#000000"
        self.co2 = "#20214f"
        self.win.configure(background=self.co0)
        self.win.resizable(width=False, height=False)  # don't allow resizeable window

    def add_contact(self):
        """This method allows to add records in connected database."""
        cur = self.connection.cursor()  # define connection to database
        self.FName = self.entryFName.get()  # define Entrys
        self.LName = self.entryName.get()
        self.Ort = self.entryOrt.get()
        self.PLZ = self.entryPLZ.get()
        self.HNR = self.entryHNR.get()
        self.Str = self.entryStr.get()
        self.Phone = self.entryPhone.get()

        if self.FName == '' or self.LName == '' or self.PLZ == '' or self.Ort == '' or self.Str == '' or self.HNR == '' or self.Phone == '':
            messagebox.showwarning("Warning", "Feld darf nicht leer sein")  # raise messagebox if entry is empty

        elif not re.search(r'^\d{4}$', self.PLZ):
            messagebox.showerror("Error", "Bitte geben Sie eine gültige PLZ ein.")  # raise messagebox if user uses wrong PostCode

        elif not self.FName.strip().isalpha():
            messagebox.showwarning("Warning", "Datentyp bei Vorname beachten!")  # raise messagebox if user uses wrong Datatype

        elif not self.LName.strip().isalpha(): 
            messagebox.showwarning("Warning", "Datentyp bei Nachname beachten!")

        elif not self.Ort.strip().isalpha():
            messagebox.showwarning("Warning", "Datentyp bei Ort beachten!")

        elif not self.Str.isalpha():
            messagebox.showwarning("Warning", "Datentyp bei Straße beachten!")

        elif not self.HNR.strip().isnumeric(): 
            messagebox.showwarning("Warning", "Datentyp bei Haus-Nr. beachten!")
        
        elif not self.Phone.strip().isnumeric():
            messagebox.showwarning("Warning", "Datentyp bei Tel.-Nr. beachten!")

        elif self.check_for_same_tel(self.Phone):
            messagebox.showerror("Error", "Telefonnummer ist bereits vorhanden")

        else:
            if self.check_for_same_name(self.FName, self.LName):
                messagebox.showinfo("Info", "Kontakt mit selben Namen vorhanden! Kontakt wurde erfolgreich hinzugefügt!")
            self.insert_Name(self.FName, self.LName)  # methods which allow to save data
            self.insert_Address(self.PLZ, self.Str, self.Ort, self.HNR, bool(1))
            self.insert_PhoneNumber(self.Phone, bool(1))
            self.Insert_Category(self.selected)
            self.connection.commit()
            select = cur.execute("SELECT * FROM Contact order by id desc")
            select = list(select)
            id = select[0][0]
            filename = self.entryPhoto.get()
            im = Image.open(filename)
            rgb_im = im.convert('RGB')
            rgb_im.save(("img/img_/profile_" + str(id) + "." + "jpg"))  # save the selected image

    def combo_(self):
        """Create a Combo Box for Kategorie items"""
        self.root = tk.Tk()
        self.root.configure(background=self.co2)
        self.root.resizable(width=False, height=False)  # don't allow resizeable window
        self.combo = ttk.Combobox(self.root, values=["Familie", "Freunde", "Schule", "Arbeit"])
        self.combo.pack()
        self.combo.current(0)  # setting default value
        ok_button = tk.Button(self.root, bg=self.co2, fg=self.co0, text="OK", command=self.save_close)
        ok_button.pack()
        self.root.mainloop()

    def save_close(self):
        """Save Kategory item in Database and Close the Combobox"""
        self.selected = self.combo.get()
        self.connection.commit()
        self.root.destroy()

    def BrowsePhoto(self):
        """Allows to search for a photo"""
        self.entryPhoto.delete(0, END)
        filename = filedialog.askopenfilename(initialdir="/", title="Select File")
        return self.entryPhoto.insert(END, filename)

    def Delete_Win(self):
        """Switch to Delete Win"""
        self.win.withdraw()  # close actual window
        self.win.destroy()
        from delete_contact_gui import MainWinDelete
        win = MainWinDelete()
        win.Window()
        win.win.mainloop()

    def Query_Win(self):
        """Switch to Query Win"""
        self.win.withdraw()  # close actual window
        self.win.destroy()
        from gui_query import MainWinQuery
        win = MainWinQuery()
        win.Window()
        win.win.mainloop()

    def Update_Win(self):
        """Switch to Update Win"""
        self.win.withdraw()  # close actual window
        self.win.destroy()
        from gui_update_record import MainWinUpdate
        wind = MainWinUpdate()
        wind.MainWinUpdate()
        wind.wind.mainloop()

    def home_(self):
        self.win.withdraw() #close actual window
        self.win.destroy()
        from main_gui import Win
        win = Win()
        win.Window()
        win.win.mainloop()

    def Window_Main(self):
        """Create the Main Window of the Add Window"""
        top = Frame(self.win, width=800, height=50, bg=self.co2)
        top.grid(row=0, column=0, padx=0, pady=1)

        bottom = Frame(self.win, width=800, height=150, bg=self.co2)
        bottom.place(x=0, y=480)

        header = Label(top, text="Adress-Management ✆", height=1, font=("Bahnschrift 22 bold"), bg= self.co2, fg=self.co0)
        header.place(x=280, y=2)

        # First Name
        self.lblFName = Label(self.win, text="Vorname: ", font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblFName.place(x=240, y=70, width=125)
        self.entryFName = Entry(self.win)
        self.entryFName.place(x=263, y=100, width=200, height=30)

        # Last Name
        self.lblName = Label(self.win, text="Nachname: ", font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblName.place(x=480, y=70, width=125)
        self.entryName = Entry(self.win)
        self.entryName.place(x=496, y=100, width=200, height=30)

        # PLZ
        self.lblPLZ = Label(self.win, text="PLZ: ", font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblPLZ.place(x=220, y=140, width=125)
        self.entryPLZ = Entry(self.win)
        self.entryPLZ.place(x=263, y=170, width=200, height=30)

        # Street
        self.lblStr = Label(self.win, text="Straße: ", font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblStr.place(x=464, y=140, width=125)
        self.entryStr = Entry(self.win)
        self.entryStr.place(x=496, y=170, width=200, height=30)

        # City
        self.lblOrt = Label(self.win, text="Ort: ", font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblOrt.place(x=220, y=210, width=125)
        self.entryOrt = Entry(self.win)
        self.entryOrt.place(x=263, y=240, width=200, height=30)

        # Housenumber
        self.lblHNR = Label(self.win, text="Haus-Nr.: ", font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblHNR.place(x=472, y=210, width=125)
        self.entryHNR = Entry(self.win)
        self.entryHNR.place(x=496, y=240, width=200, height=30)

        # Phone
        self.lblPhone = Label(self.win, text="Tel.: ", font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblPhone.place(x=222, y=280, width=125, height=30)
        self.entryPhone = Entry(self.win)
        self.entryPhone.place(x=263, y=310, width=200, height=30)

        # Photo
        self.lblPhoto = Label(self.win, text="Photo: ",  font=("Calibri 14 bold"), bg=self.co0, fg=self.co1)
        self.lblPhoto.place(x=462, y=280, width=125, height=30)
        self.bPhoto = Button(self.win, text="Browse", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.BrowsePhoto)
        self.bPhoto.place(x=620, y=350, height=30)
        self.entryPhoto = Entry(self.win)
        self.entryPhoto.place(x=496, y=310, width=200, height=30)

        # Add Contact Button
        self.bAdd = Button(self.win, text="Kontakt hinzufügen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.add_contact)
        self.bAdd.place(x=480, y=410, width=255, height=40)

        # Update Button
        self.bUpdate = Button(self.win, text="Kontakt aktualisieren", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Update_Win)
        self.bUpdate.place(x=20, y=100, width=180, height=40)

        # Query Button
        self.bQuery = Button(self.win, text="Kontakt abfragen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Query_Win)
        self.bQuery.place(x=20, y=200, width=180, height=40)

        # Delete Button
        self.bDelete = Button(self.win, text="Kontakt löschen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Delete_Win)
        self.bDelete.place(x=20, y=300, width=180, height=40)

        # Category Button
        self.bCategory = Button(self.win, text="Kategorie hinzufügen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.combo_)
        self.bCategory.place(x=280, y=410, width=180, height=40)

        # Home Button
        self.bHome = Button(self.win, text="🏠", font=("Bahnschrift 40 bold"), bg=self.co0, command=self.home_)
        self.bHome.place(x=722, y=60, width=60, height=60)

def main():
    win = MainWin()
    win.Window_Main()
    win.win.mainloop()


if __name__ == "__main__":
    main()
