from src.Genre.GenreDAO import GenreDAO
from src.Genre.Genre import Genre

class GenreApplication():

    def __init__(self,table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = GenreDAO(self)

    def SaveGenre(self):
        Name = self.table_user_interface.proces_input("Jmeno žánru: ")
        g = Genre(Name)
        self.table_DAO.Save(g)

    def UpdateGenre(self):
        id = self.table_user_interface.proces_input("id upravovaného žánru: ")
        Name = self.table_user_interface.proces_input("Upravené jmeno žánru: ")
        g = Genre(Name,id)
        self.table_DAO.Update(g)

    def DeleteGenre(self):
        id = self.table_user_interface.proces_input("id žánru na smazání: ")
        self.table_DAO.Delete(id)
    
    def ReadGenre(self):
        self.table_user_interface.interface.print_line()
        self.table_user_interface.print_read(self.table_DAO.Read())
    
    def LoadGenre(self):
        self.table_DAO.Load()
