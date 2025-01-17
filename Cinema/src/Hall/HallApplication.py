from src.Hall.HallDAO import HallDAO
from src.Hall.Hall import *
from mysql.connector.errors import *

class HallApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = HallDAO(self)

    def SaveHall(self):
        Name = self.table_user_interface.proces_input("Název sálu: ")
        Type = self.table_user_interface.proces_input("Typ sálu (Standartní/VIP): ")
        try:
            h = Hall(Name, Type)
        except HallNameValueError:
            self.table_user_interface.print_message("Neplatný název haly: Musí být alfanumerický a do 30 znaků.")
        except HallTypeValueError:
            self.table_user_interface.print_message("Neplatný typ haly: Musí to být buď 'Standartní' nebo 'VIP'.")
        else:
            self.table_DAO.Save(h)

    def UpdateHall(self):
        id = self.table_user_interface.proces_input("ID sálu na úpravu: ")
        Name = self.table_user_interface.proces_input("Nový název sálu: ")
        Type = self.table_user_interface.proces_input("Nový typ sálu (Standartní/VIP): ")
        try:
            h = Hall(Name, Type, id)
        except IDValueError:
            self.table_user_interface.print_message("Neplatný ID: musí být kladný číslo")
        except HallNameValueError:
            self.table_user_interface.print_message("Neplatný název haly: Musí být alfanumerický a do 30 znaků.")
        except HallTypeValueError:
            self.table_user_interface.print_message("Neplatný typ haly: Musí to být buď 'Standartní' nebo 'VIP'.")
        else:
            self.table_DAO.Update(h)

    def DeleteHall(self):
        try:
            id = int(self.table_user_interface.proces_input("ID sálu na smazání: "))
        except ValueError:
            self.table_user_interface.print_message("id musí být číslo")
        else:
            self.table_DAO.Delete(id)
    
    def ReadHall(self):
        self.table_user_interface.interface.print_line()
        try:
            self.table_user_interface.print_read(self.table_DAO.Read())
        except DatabaseError:
            self.table_user_interface.print_message("Selhalo připojení k databázi")

    def LoadHall(self):
        try:
            list = self.table_DAO.Load()
        except HallNameValueError:
            self.table_user_interface.print_message("Neplatný název haly: Musí být alfanumerický a do 30 znaků.")
        except HallTypeValueError:
            self.table_user_interface.print_message("Neplatný typ haly: Musí to být buď 'Standartní' nebo 'VIP'.")
        else:
            try:
                for i in list:
                    self.table_DAO.Save(i)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")
