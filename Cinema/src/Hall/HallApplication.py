from src.Hall.HallDAO import HallDAO
from src.Hall.Hall import *

class HallApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = HallDAO(self)

    #add val function
    #send message with self.table_user_interface.print_message(message)
    #load from json by loading customers to list and than sending that instead of both at same time
    def SaveHall(self):
        Name = self.table_user_interface.proces_input("Název sálu: ")
        Type = self.table_user_interface.proces_input("Typ sálu (Standartní/VIP): ")
        try:
            h = Hall(Name, Type)
        except HallNameValueError:
            print("Neplatný název haly: Musí být alfanumerický a do 30 znaků.")
        except HallTypeValueError:
            print("Neplatný typ haly: Musí to být buď 'Standartní' nebo 'VIP'.")
        else:
            self.table_DAO.Save(h)

    def UpdateHall(self):
        id = self.table_user_interface.proces_input("ID sálu na úpravu: ")
        Name = self.table_user_interface.proces_input("Nový název sálu: ")
        Type = self.table_user_interface.proces_input("Nový typ sálu (Standartní/VIP): ")
        try:
            h = Hall(Name, Type, id)
        except IDValueError:
            print("Neplatný ID: musí být kladný číslo")
        except HallNameValueError:
            print("Neplatný název haly: Musí být alfanumerický a do 30 znaků.")
        except HallTypeValueError:
            print("Neplatný typ haly: Musí to být buď 'Standartní' nebo 'VIP'.")
        else:
            self.table_DAO.Update(h)

    def DeleteHall(self):
        try:
            id = int(self.table_user_interface.proces_input("ID sálu na smazání: "))
        except ValueError:
            print("id musí být číslo")
        else:
            self.table_DAO.Delete(id)
    
    def ReadHall(self):
        self.table_user_interface.interface.print_line()
        self.table_user_interface.print_read(self.table_DAO.Read())

    def LoadHall(self):
        self.table_DAO.Load()
