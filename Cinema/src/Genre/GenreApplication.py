from src.Genre.GenreDAO import GenreDAO
from src.Genre.Genre import *
from mysql.connector.errors import *

class GenreApplication():

    def __init__(self,table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = GenreDAO(self)

    def SaveGenre(self):
        Name = self.table_user_interface.proces_input("Jmeno žánru: ")
        try:
            g = Genre(Name)
        except GenreNameValueError:
            self.table_user_interface.print_message("Neplatný název žánru: Musí být alfanumerický a do 30 znaků.")
            try:
                self.table_DAO.Save(g)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")

    def UpdateGenre(self):
        id = self.table_user_interface.proces_input("id upravovaného žánru: ")
        Name = self.table_user_interface.proces_input("Upravené jmeno žánru: ")
        try:
            g = Genre(Name,id)
        except IDValueError:
            self.table_user_interface.print_message("Neplatný ID: musí být kladný číslo")
        except GenreNameValueError:
            self.table_user_interface.print_message("Neplatný název žánru: Musí být alfanumerický a do 30 znaků.")
        else:
            try:
                self.table_DAO.Update(g)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")

    def DeleteGenre(self):
        try:
            id = int(self.table_user_interface.proces_input("id žánru na smazání: "))
        except ValueError:
            self.table_user_interface.print_message("id musí být číslo")
        else:
            try:
                self.table_DAO.Delete(id)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")
    
    def ReadGenre(self):
        self.table_user_interface.interface.print_line()
        try:
            self.table_user_interface.print_read(self.table_DAO.Read())
        except DatabaseError:
            self.table_user_interface.print_message("Selhalo připojení k databázi")
    
    def LoadGenre(self):
        try:
            list = self.table_DAO.Load()
        except GenreNameValueError:
            self.table_user_interface.print_message("Neplatný název žánru: Musí být alfanumerický a do 30 znaků.")
        else:
            try:
                for i in list:
                    self.table_DAO.Save(i)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")
