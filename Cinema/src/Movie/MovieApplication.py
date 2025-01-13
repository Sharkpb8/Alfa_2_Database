from src.Movie.MovieDAO import MovieDAO

class MovieApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = MovieDAO(self)

    def SaveMovie(self):
        Genre_id = self.table_user_interface.proces_input("ID žánru: ")
        Name = self.table_user_interface.proces_input("Název filmu: ")
        Length = self.table_user_interface.proces_input("Délka filmu (v minutách): ")
        Price = self.table_user_interface.proces_input("Cena: ")
        Premiere_date = self.table_user_interface.proces_input("Datum premiéry (YYYY-MM-DD): ")
        self.table_DAO.Save(Genre_id, Name, Length, Price, Premiere_date)

    def UpdateMovie(self):
        id = self.table_user_interface.proces_input("ID filmu na úpravu: ")
        Genre_id = self.table_user_interface.proces_input("Nové ID žánru: ")
        Name = self.table_user_interface.proces_input("Nový název filmu: ")
        Length = self.table_user_interface.proces_input("Nová délka filmu (v minutách): ")
        Price = self.table_user_interface.proces_input("Nová cena: ")
        Premiere_date = self.table_user_interface.proces_input("Nové datum premiéry (YYYY-MM-DD): ")
        self.table_DAO.Update(id, Genre_id, Name, Length, Price, Premiere_date)

    def DeleteMovie(self):
        id = self.table_user_interface.proces_input("ID filmu na smazání: ")
        self.table_DAO.Delete(id)
    
    def ReadMovie(self):
        self.table_user_interface.interface.print_line()
        self.table_DAO.Read()

    def LoadMovie(self):
        self.table_DAO.Load()
