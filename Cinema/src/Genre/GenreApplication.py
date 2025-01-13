from src.Genre.GenreDAO import GenreDAO

class GenreApplication():

    def __init__(self,table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = GenreDAO(self)

    def SaveGenre(self):
        Name = self.table_user_interface.proces_input("Jmeno žánru: ")
        self.table_DAO.Save(Name)

    def UpdateGenre(self):
        id = self.table_user_interface.proces_input("id upravovaného žánru: ")
        Name = self.table_user_interface.proces_input("Upravené jmeno žánru: ")
        self.table_DAO.Update(id,Name)

    def DeleteGenre(self):
        id = self.table_user_interface.proces_input("id žánru na smazání: ")
        self.table_DAO.Delete(id)
    
    def ReadGenre(self):
        self.table_user_interface.interface.print_line()
        self.table_DAO.Read()
    
    def LoadGenre(self):
        self.table_DAO.Load()
