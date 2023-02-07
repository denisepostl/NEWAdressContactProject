import re
from tkinter import messagebox

class Check_Entry():
    def check(FName, LName, PLZ, Ort, Str, HNR, Phone):
        if FName == '' or LName == '' or PLZ == '' or Ort == '' or Str == '' or HNR == '' or Phone == '':
            messagebox.showwarning("Warning", "Feld darf nicht leer sein")  # raise messagebox if entry is empty

        elif not re.search(r'^\d{4}$', PLZ):
            messagebox.showerror("Error", "Bitte geben Sie eine gültige PLZ ein.")  # raise messagebox if user uses wrong PostCode

        elif not FName.strip().isalpha():
            messagebox.showwarning("Warning", "Datentyp bei Vorname beachten!")  # raise messagebox if user uses wrong Datatype

        elif not LName.strip().isalpha(): 
            messagebox.showwarning("Warning", "Datentyp bei Nachname beachten!")

        elif not Ort.strip().isalpha():
            messagebox.showwarning("Warning", "Datentyp bei Ort beachten!")

        elif not Str.isalpha():
            messagebox.showwarning("Warning", "Datentyp bei Straße beachten!")

        elif not HNR.strip().isnumeric(): 
            messagebox.showwarning("Warning", "Datentyp bei Haus-Nr. beachten!")
        
        elif not Phone.strip().isnumeric():
            messagebox.showwarning("Warning", "Datentyp bei Tel.-Nr. beachten!")