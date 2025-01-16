from src.Genre.GenreDAO import GenreDAO
from src.Genre.Genre import *

class GenreApplication():

    def __init__(self,table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = GenreDAO(self)

    #add val function
    #send message with self.table_user_interface.print_message(message)
    #load from json by loading customers to list and than sending that instead of both at same time
    def SaveGenre(self):
        Name = self.table_user_interface.proces_input("Jmeno žánru: ")
        try:
            g = Genre(Name)
        except GenreNameValueError:
            print("Neplatný název žánru: Musí být alfanumerický a do 30 znaků.")
        else:
            self.table_DAO.Save(g)

    def UpdateGenre(self):
        id = self.table_user_interface.proces_input("id upravovaného žánru: ")
        Name = self.table_user_interface.proces_input("Upravené jmeno žánru: ")
        try:
            g = Genre(Name,id)
        except IDValueError:
            print("Neplatný ID: musí být kladný číslo")
        except GenreNameValueError:
            print("Neplatný název žánru: Musí být alfanumerický a do 30 znaků.")
        else:
            self.table_DAO.Update(g)

    def DeleteGenre(self):
        try:
            id = int(self.table_user_interface.proces_input("id žánru na smazání: "))
        except ValueError:
            print("id musí být číslo")
        else:
            self.table_DAO.Delete(id)
    
    def ReadGenre(self):
        self.table_user_interface.interface.print_line()
        self.table_user_interface.print_read(self.table_DAO.Read())
    
    def LoadGenre(self):
        self.table_DAO.Load()
