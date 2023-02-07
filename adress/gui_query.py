from tkinter import ttk 
import tkinter as tk
from tkinter import *
from tkinter import messagebox

from tkinter import filedialog
import os
from PIL import Image, ImageTk
from adress.query_search_by import QuerySearchBy
from adress.add_only_one_second_adress import Accept_Adress
import sqlite3

#load the image
Profile = {1: ""}

class MainWinQuery(Accept_Adress, QuerySearchBy):

    def __init__(self):
        """Initialize database connection and define settings like color, geometry"""
        self.connection = sqlite3.connect("database/adress_cat.db")
        self.win = Tk()
        self.win.title=("Adress-Management")
        self.win.geometry('800x600')
        self.co0 = "#ffffff"
        self.co1 = "#000000"
        self.co2 = "#20214f"
        self.win.configure(background=self.co0) #set the background color
        self.win.resizable(width=False, height=False) #don't let the window resizing
        

    def SearchByPhone(self, event):
        """Search for record by phonenumber"""
        for x in self.tree.get_children():
            self.tree.delete(x)
        phone = self.entrySearchByPhone.get()
        if phone == '':
            messagebox.showwarning("Warning", "Bitte Tel.-Nr. eingeben") #raise messagebox if user ask without phonenumber
        self.querybyphone(phone,)  
        if not self.contact and not phone == '':
            messagebox.showinfo("Info", "Telefonnummer nicht vorhanden!") #raise messagebox if the specific record is not in db
        for row in self.contact:
            self.tree.insert('', END, values=row)

    def query_contact(self):
        """Get all records in treeview"""
        for x in self.tree.get_children():
            self.tree.delete(x)
        self.askin_all()
        if not self.contact:
            messagebox.showwarning("Warning", "Keine Datensätze vorhanden") #raise messagebox if db is empty
        for row in self.contact:
            self.tree.insert('', END, values=row)


    def SearchByName(self, event):
        """Search for Record by name"""
        for x in self.tree.get_children():
            self.tree.delete(x)
        name = self.entrySearchByName.get()
        lname = self.entrySearchByLName.get()
        if name == '' or lname == '':
            messagebox.showwarning("Warning", "Bitte Vor- u. Nachname eingeben!") #raise messagebox if user only insert one name
        self.querybyname(name, lname)
        if not self.contact and not name == '' and not lname == '':
            messagebox.showinfo("Info", "Eintrag nicht vorhanden!") #raise messagebox if specific record isn't in db
        else:
            for row in self.contact:
                self.tree.insert('', END, values=row)

    def Delete_Win(self):
        """Switch to delete window"""
        self.win.withdraw()#destroy actual window
        self.win.destroy()
        from delete_contact_gui import MainWinDelete
        win = MainWinDelete()
        win.Window()
        win.win.mainloop()

    def Add_Win(self):
        """Switch to Add Window"""
        self.win.withdraw()#destroy actual Window
        self.win.destroy()
        from add_contact_gui import MainWin
        win = MainWin()
        win.Window_Main()
        win.win.mainloop()

    def Update_Win(self):
        """Switch to Update Window"""
        self.win.withdraw()#destroy actual Window
        self.win.destroy()
        from gui_update_record import MainWinUpdate
        wind = MainWinUpdate()
        wind.MainWinUpdate()
        wind.wind.mainloop()

    def combobox(self):
        """Create a Combo Box for Kategorie items"""
        self.root = tk.Tk()
        self.root.configure(background=self.co2)
        self.root.resizable(width=False, height=False)  # don't allow resizeable window
        self.combo = ttk.Combobox(self.root, values=["Familie", "Freunde", "Schule", "Arbeit"])
        self.combo.pack()
        self.combo.current(0)  # setting default value
        ok_button = tk.Button(self.root, bg=self.co2, fg=self.co0, text="OK", command=self.searching)
        ok_button.pack()
        self.root.mainloop()

    def searching(self):
        """Save Kategory item in Database and Close the Combobox"""
        self.selected = self.combo.get()
        for x in self.tree.get_children():
            self.tree.delete(x)
        self.querycat(self.selected)
        if not self.contact:
            messagebox.showwarning("Warning", "Keine Datensätze vorhanden") #raise messagebox if db is empty
        for row in self.contact:
            self.tree.insert('', END, values=row)
        self.root.destroy()

    def home_(self):
        self.win.withdraw() #close actual window
        self.win.destroy()
        from main_gui import Win
        win = Win()
        win.Window()
        win.win.mainloop()

    def Window(self):
        """Create the Window for the Query Option Window"""
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
        self.entrySearchByName.place(x=400, y=60, width=160, height=30)


        self.lbSearchByLName = Label(self.win, text="Suche nach Name:", font=("Calibri 16 bold"), bg=self.co0, fg=self.co1)
        self.lbSearchByLName.place(x=200, y=60, width=200)
        self.entrySearchByLName = Entry(self.win)
        self.entrySearchByLName.insert(0, "Nachname")
        self.entrySearchByLName.bind("<Return>", self.SearchByName)
        self.entrySearchByLName.place(x=580, y=60, width=160, height=30)

        self.lbSearchByPhone = Label(self.win, text="Suche nach Tel.:", font=("Calibri 16 bold"), bg=self.co0, fg=self.co1)
        self.lbSearchByPhone.place(x=190, y=90, width=200)
        self.entrySearchByPhone = Entry(self.win)
        self.entrySearchByPhone.insert(0, "Tel.-Nr.")
        self.entrySearchByPhone.bind("<Return>", self.SearchByPhone)
        self.entrySearchByPhone.place(x=400, y=90, width=160, height=30)

        # Add Contact Button
        self.bAdd = Button(self.win, text="Alle Kontakte abfragen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.query_contact)
        self.bAdd.place(x=480, y=370, width=255, height=40)

        # Update
        self.bAdd = Button(self.win, text="Kontakt aktualisieren", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Update_Win)
        self.bAdd.place(x=20, y=128, width=190, height=40)

        # Add
        self.bAdd = Button(self.win, text="Kontakt hinzufügen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Add_Win)
        self.bAdd.place(x=20, y=228, width=190, height=40)

        # delete
        self.bdelete = Button(self.win, text="Kontakt löschen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.Delete_Win)
        self.bdelete.place(x=20, y=328, width=190, height=40)

        #search by category
        self.bCategory = Button(self.win, text="Nach Kategorie suchen", font=("Bahnschrift 14 bold"), bg=self.co2, fg=self.co0, command=self.combobox)
        self.bCategory.place(x=480, y=420, width=255, height=40)

        # Home Button
        self.bHome = Button(self.win, text="🏠", font=("Bahnschrift 40 bold"), bg=self.co0, command=self.home_)
        self.bHome.place(x=722, y=60, width=60, height=60)

        self.tree = ttk.Treeview(self.win, columns=(1, 2, 3, 4, 5, 6, 7, 8, ), height=5, show="headings")
        self.tree.place(x=220, y=140, width=520, height=220)
        self.tree.bind("<<TreeviewSelect>>", self.treeActionSelect)

        # Add headings
        self.tree.heading(1, text="ID")
        self.tree.heading(2, text="Vorname")
        self.tree.heading(3, text="Nachname")
        self.tree.heading(4, text="Adresse")
        self.tree.heading(5, text="Nebenadresse")
        self.tree.heading(6, text="Tel.-Nr.")
        self.tree.heading(7, text="Zweite Tel.-Nr.")
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


        #self.load = Image.open("img/profile.png")
        #self.photo = ImageTk.PhotoImage(self.load, master=self.win)
        #self.label_image = Label(self.win, image=self.photo)  
        #self.label_image.place(x=40, y=380)



    def treeActionSelect(self, event):
        """Select Items of Treeview"""
        #self.label_image.destroy()
        self.idSelect = self.tree.item(self.tree.selection())['values'][0]
        self.first_name = self.tree.item(self.tree.selection())['values'][1]
        self.last_name = self.tree.item(self.tree.selection())['values'][2]
        self.adresse = self.tree.item(self.tree.selection())['values'][3]
        self.adresse2 = self.tree.item(self.tree.selection())['values'][4]
        self.tel = self.tree.item(self.tree.selection())['values'][5]
        self.tel2 = self.tree.item(self.tree.selection())['values'][6]
        self.imgProfile="img/img_/profile_" + str(self.idSelect) + "." + "jpg"
        self.load = Image.open(self.imgProfile)
        self.load.thumbnail((90, 120))
        self.photo = ImageTk.PhotoImage(self.load, master=self.win)
        Profile[1] = self.photo
        self.lblImage = Label(self.win, bg= "black",image=self.photo)
        self.lblImage.place(x=40, y=410)
        self.lname = Label(self.win, width=40, anchor="w", text="Name: " + str(self.first_name) + " " +str(self.last_name), bg=self.co0)
        self.lname.place(x=148, y=430)

        self.splitting = self.adresse.split(',')
        self.ladr = Label(self.win, width=40, anchor="w", text="Adresse: " + str(self.splitting[0]) + str(self.splitting[3]) + str(self.splitting[1]) + str(self.splitting[2]), bg=self.co0)
        self.ladr.place(x=148, y=460)

        self.lphone = Label(self.win, width=40, anchor="w", text="Tel.-Nr.: " + str(self.tel), bg=self.co0)
        self.lphone.place(x=148, y=498)

        self.get_id_for_check(self.first_name, self.last_name, self.tel)
        self.get_count_tel()
        self.get_count_adr()
        if self.tc_id == 2:
            self.lphone1 = Label(self.win, width=40, anchor="w", text="2. Tel.-Nr.: " + str(self.tel2), bg=self.co0)
            self.lphone1.place(x=148, y=514)
        if self.tc_id != 2:
            self.lphone1 = Label(self.win, width = 40, bg=self.co0)
            self.lphone1.place(x=148, y=514)
        if self.c_id == 2:
            self.part = self.adresse2.split(',')
            self.ladr1 = Label(self.win, width=40, anchor="w", text="Neben-Adresse: " + str(self.part[0]) + str(self.part[3]) + str(self.part[1]) + str(self.part[2]), bg=self.co0)
            self.ladr1.place(x=148, y=478)

        if self.c_id != 2:
            self.ladr1 = Label(self.win, width = 40, bg=self.co0)
            self.ladr1.place(x=148, y=478)

def main():
    win = MainWinQuery()
    win.Window()
    win.win.mainloop()


if __name__ == "__main__":
    main()
