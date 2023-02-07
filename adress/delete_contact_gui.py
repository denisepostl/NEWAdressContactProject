from tkinter import ttk 
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
from PIL import Image, ImageTk
from adress.query_search_by import QuerySearchBy
import sqlite3
from adress.gui_query import MainWinQuery
from adress.delete_for_gui import Delete_Contact
from adress.update_for_gui import Updating

# load the image
Profile = {1: ""}


class MainWinDelete(QuerySearchBy, Delete_Contact, Updating):
    """Create the window for Delete Option"""

    def __init__(self):
        """Initialize the database Connection and define Settings for the Window like color, geometry or Title"""
        self.connection = sqlite3.connect("database/adress_cat.db")
        self.win = Tk()
        self.win.title=("Adress-Management")
        self.win.geometry('800x600')
        self.co0 = "#ffffff"
        self.co1 = "#000000"
        self.co2 = "#20214f"
        self.win.configure(background=self.co0)
        self.win.resizable(width=False, height=False)
 
    def delete_contact(self):
        """Delete the Contact by selecting of Contact-Record"""
        if not self.tree.selection():
            messagebox.showerror("Kontakt auswählen", "Kontakt auswählen")
        self.idSelect = self.tree.item(self.tree.selection())['values'][0]

        self.deleting = tk.Tk()  # new window
        self.deleting.configure(background=self.co0)
        self.lbl = Label(self.deleting, text="Kontakt löschen? ", font=("Calibri 14"), bg=self.co0, fg=self.co1)
        self.lbl.place(x=2, y=28, width=200, height=20)
        self.lbl1 = Label(self.deleting, text="✗", font=("Arial 20"), bg=self.co0, fg="red")
        self.lbl1.place(x=107, y=110, width=20, height=20)
        self.lb = Label(self.deleting, text="✓", font=("Arial 20"), bg=self.co0, fg="green")
        self.lb.place(x=60, y=110, width=20, height=20)
        self.lbl2 = Label(self.deleting, bg=self.co2)
        self.lbl2.place(x=0, y=0, width=400, height=20)
        self.lbl3 = Label(self.deleting, bg=self.co2)
        self.lbl3.place(x=0, y=160, width=400, height=40)
        button = Button(self.deleting, text="Ja", font=("Calibri 12"), command=self.delete_c, bg=self.co2, fg=self.co0)
        button.place(x=50, y=80, width= 40, height=22)
        button1 = Button(self.deleting, text="Nein", font=("Calibri 12"), command=self.breaking, bg=self.co2, fg=self.co0)
        button1.place(x=100, y=80, width= 40, height=22)
        self.deleting.mainloop()
    
    def breaking(self):
        self.deleting.destroy()

    def delete_c(self):
        self.get_id_ = self.get_name_id(self.name, self.lname)
        self.get_id(self.name, self.lname)
        con = self.connection
        cur = con.cursor()
        cur.execute("delete from Contact where ID = {}".format(self.idSelect))
        self.delete_adress(self.get_id_)
        self.delete_phonenumber(self.get_id_)
        self.delete_category(self.get_id_)
        con.commit()
        self.imgProfile="img/img_/profile_" + str(self.idSelect) + "." + "jpg" # delete the image
        os.remove(self.imgProfile)
        self.deleting.destroy()
        self.viewing_records()
        
    def viewing_records(self):
        """Show the records"""
        for x in self.tree.get_children():
            self.tree.delete(x)
        self.querybyid(self.My_ID)
        for row in self.contact:
            self.tree.insert('', END, values=row)

    def get_name_id(self, first_name, last_name):
        """Get the ID from the Contact by first and last name"""
        cur = self.connection.cursor()
        query = """
            SELECT
	            c.ID
            from Contact c
            join PhoneNumber a
                on c.ID=a.ID
            join Adress b
                on b.ID = c.ID
            join Kategorie d
                on c.ID = d.ID
            where First_Name like "%s" and LastName like "%s"
        """ % (first_name, last_name)
        cur.execute(query)
        ID = cur.fetchall()
        tup = ID[0]
        self.name_id = int(tup[0])
        self.connection.commit()
        return self.name_id

    def query_contact(self):
        """Insert founded Records in treeview"""
        for x in self.tree.get_children():
            self.tree.delete(x)
        self.askin_all_query()
        for row in self.contact:
            self.tree.insert('', END, values=row)

    def SearchByName(self, event):
        """Search for records by name"""
        for x in self.tree.get_children():
            self.tree.delete(x)
        self.name = self.entrySearchByName.get()
        self.lname = self.entrySearchByLName.get()
        if self.name == '' or self.lname == '':
            messagebox.showwarning("Warning", "Bitte Vor- u. Nachname eingeben!")
        self.querybyname(self.name, self.lname)
        if not self.contact and not self.name == '' and not self.lname == '':
            messagebox.showinfo("Info", "Eintrag nicht vorhanden!")
        for row in self.contact:
            self.tree.insert('', END, values=row)

    def Add_Win(self):
        """Switch to Add Window"""
        self.win.withdraw()  # destroy actual window
        self.win.destroy()
        from add_contact_gui import MainWin
        win = MainWin()
        win.Window_Main()
        win.win.mainloop()

    def Query_Win(self):
        """Switch to Query Window"""
        self.win.withdraw()  # destroy actual window
        self.win.destroy()
        from gui_query import MainWinQuery
        win = MainWinQuery()
        win.Window()
        win.win.mainloop()

    def Update_Win(self):
        """Switch to Update Window"""
        self.win.withdraw()  # destroy actual window
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

    def Window(self):
        """Create the main window for the Delete Window Option"""
        top = Frame(self.win, width=800, height=50, bg=self.co2)
        top.grid(row=0, column=0, padx=0, pady=1)

        bottom = Frame(self.win, width=800, height=140, bg=self.co2)
        bottom.place(x=0, y=540)

        header = Label(top, text="Adress-Management ✆", height=1, font=("Bahnschrift 22 bold"), bg= self.co2, fg=self.co0)
        header.place(x=280, y=2)


        self.lbSearchByName = Label(self.win, text="Suche nach Name:", font=("Calibri 16 bold"), bg=self.co0, fg=self.co1)
        self.lbSearchByName.place(x=200, y=60, width=200)
        self.entrySearchByName = Entry(self.win)
        self.entrySearchByName.insert(0, "Vorname")
        self.entrySearchByName.bind("<Return>", self.SearchByName)
        self.entrySearchByName.place(x=400, y=60, width=160, height=30)  # search for a record by First Name

        self.lbSearchByLName = Label(self.win, text="Suche nach Name:", font=("Calibri 16 bold"), bg=self.co0, fg=self.co1)
        self.lbSearchByLName.place(x=200, y=60, width=200)
        self.entrySearchByLName = Entry(self.win)
        self.entrySearchByLName.insert(0, "Nachname")
        self.entrySearchByLName.bind("<Return>", self.SearchByName)
        self.entrySearchByLName.place(x=580, y=60, width=160, height=30)  # search for a record by Last Name
    
        # Delete Contact Button
        self.bDel = Button(self.win, text="Kontakt löschen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.delete_contact)
        self.bDel.place(x=480, y=370, width=255, height=40)

        # Update
        self.bUpdate = Button(self.win, text="Kontakt aktualisieren", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Update_Win)
        self.bUpdate.place(x=20, y=128, width=190, height=40)

        # Add
        self.bAdd = Button(self.win, text="Kontakt hinzufügen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Add_Win)
        self.bAdd.place(x=20, y=228, width=190, height=40)

        # query
        self.bquery = Button(self.win, text="Kontakt abfragen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Query_Win)
        self.bquery.place(x=20, y=328, width=190, height=40)

        self.tree = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5, 6, 7, 8,), height=5, show="headings")  # treeview
        self.tree.place(x=220, y=140, width=520, height=220)

        # Home Button
        self.bHome = Button(self.win, text="🏠", font=("Bahnschrift 40 bold"), bg=self.co0, command=self.home_)
        self.bHome.place(x=722, y=60, width=60, height=60)

   
        # Add headings
        self.tree.heading(1, text="ID")
        self.tree.heading(2, text="Vorname")
        self.tree.heading(3, text="Nachname")
        self.tree.heading(4, text="Adresse")
        self.tree.heading(5, text="Nebenadresse")
        self.tree.heading(6, text="Tel.-Nr.")
        self.tree.heading(7, text="Neben Tel.-Nr.")
        self.tree.heading(8, text="Kategorie")

        # define column width
        self.tree.column(1, width=2)
        self.tree.column(2, width=40)
        self.tree.column(3, width=48)
        self.tree.column(4, width=2)
        self.tree.column(5, width=20)
        self.tree.column(6, width=20)
        self.tree.column(7, width=20)
        self.tree.column(8, width=20)


def main():
    win = MainWinDelete()
    win.Window()
    win.win.mainloop()


if __name__ == "__main__":
    main()
