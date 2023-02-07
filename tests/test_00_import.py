import os
import pytest
from types import FunctionType


try:
    import adress
except Exception as e:
    print(type(e))
    adress = None


def test_import_successful():
    """Test if import is possible."""
    assert type(adress) == type(os)



#------------------------------Ask-Class-------------------------------------#


def test_Ask_class_present():
    """Test if class is present."""
    assert adress is not None
    assert adress.Ask
    assert type(adress.Ask) is not None


def test_class_methods_present():
    """Test if the interface of Ask is complete."""
    assert adress is not None
    assert adress.Ask

    assert type(adress.Ask.askin) == FunctionType
    assert type(adress.Ask.askin_all) == FunctionType


#------------------------------Add-Class-------------------------------------#


def test_Add_class_present():
    """Test if class is present."""
    assert adress is not None
    assert adress.Add
    assert type(adress.Add) is not None

def test_class_methods_present():
    """Test if the interface of Add is complete."""
    assert adress is not None
    assert adress.Add

    assert type(adress.Add.add_Name) == FunctionType
    assert type(adress.Add.add_Address) == FunctionType
    assert type(adress.Add.add_PhoneNumber) == FunctionType

#------------------------------Contact-Class-------------------------------------#


def test_Contact_class_present():
    """Test if class is present."""
    assert adress is not None
    assert adress.Contact
    assert type(adress.Contact) is not None

def test_class_methods_present():
    """Test if the interface of Contact is complete."""
    assert adress is not None
    assert adress.Contact

    assert type(adress.Contact.add_Contact) == FunctionType


#------------------------------Calculate-ID-Class-------------------------------------#


def test_calculate_id_class_present():
    """Test if class is present."""
    assert adress is not None
    assert adress.CalculateID
    assert type(adress.CalculateID) is not None

def test_class_methods_present():
    """Test if the interface of CalculateID is complete."""
    assert adress is not None
    assert adress.CalculateID

    assert type(adress.CalculateID.calculate_phone_id) == FunctionType
    assert type(adress.CalculateID.calculate_adress_id) == FunctionType
    assert type(adress.CalculateID.calculate_contact_id) == FunctionType

#------------------------------Delete-Class-------------------------------------#


def test_delete_class_present():
    """Test if class is present."""
    assert adress is not None
    assert adress.Delete
    assert type(adress.Delete) is not None

def test_class_methods_present():
    """Test if the interface of Delete is complete."""
    assert adress is not None
    assert adress.Delete

    assert type(adress.Delete.get_del_id) == FunctionType
    assert type(adress.Delete.delete_adress) == FunctionType
    assert type(adress.Delete.delete_contact) == FunctionType
    assert type(adress.Delete.delete_phonenumber) == FunctionType


#------------------------------Create-Class-------------------------------------#


def test_create_class_present():
    """Test if class is present."""
    assert adress is not None
    assert adress.Create
    assert type(adress.Create) is not None

def test_class_methods_present():
    """Test if the interface of Create is complete."""
    assert adress is not None
    assert adress.Create

    assert type(adress.Create.create_Adress) == FunctionType
    assert type(adress.Create.create_Contact) == FunctionType
    assert type(adress.Create.create_Phonenumber) == FunctionType


#------------------------------Update-Class-------------------------------------#


def test_update_class_present():
    """Test if class is present."""
    assert adress is not None
    assert adress.Update
    assert type(adress.Update) is not None

def test_class_methods_present():
    """Test if the interface of Update is complete."""
    assert adress is not None
    assert adress.Update

    assert type(adress.Update.update_first_name) == FunctionType
    assert type(adress.Update.update_last_name) == FunctionType
    assert type(adress.Update.get_add_id) == FunctionType
    assert type(adress.Update.update_ort) == FunctionType
    assert type(adress.Update.update_plz) == FunctionType
    assert type(adress.Update.update_street) == FunctionType
    assert type(adress.Update.update_housenumber) == FunctionType
    assert type(adress.Update.get_id) == FunctionType
    assert type(adress.Update.update_tel) == FunctionType


#------------------------------Create_Contact-Class-------------------------------------#


def test_create_contact_class_present():
    """Test if class is present."""
    assert adress is not None
    assert adress.Create_Contact
    assert type(adress.Create_Contact) is not None

def test_class_methods_present():
    """Test if the interface of Create_Contact is complete."""
    assert adress is not None
    assert adress.Create_Contact

    assert type(adress.Create_Contact.create_Adress) == FunctionType
    assert type(adress.Create_Contact.create_Category) == FunctionType
    assert type(adress.Create_Contact.create_Phonenumber) == FunctionType
    assert type(adress.Create_Contact.create_Contact) == FunctionType

#------------------------------Win-Class-------------------------------------#


def test_win_class_present():
    """Test if class is present."""
    assert adress is not None
    assert adress.Win
    assert type(adress.Win) is not None

def test_class_methods_present():
    """Test if the interface of Win is complete."""
    assert adress is not None
    assert adress.Win

    assert type(adress.Win.Delete_Win) == FunctionType
    assert type(adress.Win.Window) == FunctionType
    assert type(adress.Win.Add_Win) == FunctionType
    assert type(adress.Win.Query_Win) == FunctionType
    assert type(adress.Win.Update_Win) == FunctionType

#------------------------------MainWin-Class-------------------------------------#


def test_mainwin_class_present():
    """Test if class is present."""
    assert adress is not None
    assert adress.MainWin
    assert type(adress.MainWin) is not None

def test_class_methods_present():
    """Test if the interface of MainWin is complete."""
    assert adress is not None
    assert adress.MainWin

    assert type(adress.MainWin.Delete_Win) == FunctionType
    assert type(adress.MainWin.Window_Main) == FunctionType
    assert type(adress.MainWin.BrowsePhoto) == FunctionType
    assert type(adress.MainWin.Query_Win) == FunctionType
    assert type(adress.MainWin.Update_Win) == FunctionType
    assert type(adress.MainWin.add_contact) == FunctionType

#------------------------------MainWinUpdate-Class-------------------------------------#


def test_mainwin_class_present():
    """Test if class is present."""
    assert adress is not None
    assert adress.MainWinUpdate
    assert type(adress.MainWin) is not None

def test_class_methods_present():
    """Test if the interface of MainWinUpdate is complete."""
    assert adress is not None
    assert adress.MainWinUpdate

    assert type(adress.MainWinUpdate.Delete_Win) == FunctionType
    assert type(adress.MainWinUpdate.Add_Win) == FunctionType
    assert type(adress.MainWinUpdate.query_contact) == FunctionType
    assert type(adress.MainWinUpdate.Query_Win) == FunctionType
    assert type(adress.MainWinUpdate.SearchByName) == FunctionType
    assert type(adress.MainWinUpdate.run_query) == FunctionType
    assert type(adress.MainWinUpdate.editing) == FunctionType
    assert type(adress.MainWinUpdate.update_records) == FunctionType
    assert type(adress.MainWinUpdate.viewing_records) == FunctionType

#------------------------------QuerySearchBy-Class-------------------------------------#
def test_query_search_by_class_present():
    """Test if class is present."""
    assert adress is not None
    assert adress.QuerySearchBy
    assert type(adress.QuerySearchBy) is not None


def test_class_methods_present():
    """Test if the interface of QuerySearchBy is complete."""
    assert adress is not None
    assert adress.QuerySearchBy

    assert type(adress.QuerySearchBy.askin_all_query) == FunctionType
    assert type(adress.QuerySearchBy.askin_phone_query) == FunctionType
    assert type(adress.QuerySearchBy.askin_query) == FunctionType

#------------------------------MainWinDelete-Class-------------------------------------#
def test_MainWinDelete_class_present():
    """Test if class is present."""
    assert adress is not None
    assert adress.MainWinDelete
    assert type(adress.MainWinDelete) is not None


def test_class_methods_present():
    """Test if the interface of MainWinDelete is complete."""
    assert adress is not None
    assert adress.MainWinDelete

    assert type(adress.MainWinDelete.delete_contact) == FunctionType
    assert type(adress.MainWinDelete.get_name_id) == FunctionType
    assert type(adress.MainWinDelete.SearchByName) == FunctionType
    assert type(adress.MainWinDelete.Window) == FunctionType
    assert type(adress.MainWinDelete.query_contact) == FunctionType
    assert type(adress.MainWinDelete.Add_Win) == FunctionType
    assert type(adress.MainWinDelete.Update_Win) == FunctionType
    assert type(adress.MainWinDelete.Query_Win) == FunctionType