from src.Movie.MovieDAO import MovieDAO
from src.Movie.Movie import *
from mysql.connector.errors import *

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
        try:
            m = Movie(Genre_id,Name,Length,Price,Premiere_date)
        except GenreIDValueError:
            self.table_user_interface.print_message("Neplatný Genre_id: Musí to být kladné celé číslo.")
        except MovieNameValueError:
            self.table_user_interface.print_message("Neplatný název filmu: Musí být alfanumerický a do 50 znaků.")
        except MovieLengthValueError:
            self.table_user_interface.print_message("Neplatná délka filmu: Musí to být kladné celé číslo.")
        except MoviePriceValueError:
            self.table_user_interface.print_message("Neplatná cena filmu: Musí to být kladné číslo.")
        except MoviePremiereDateValueError:
            self.table_user_interface.print_message("Neplatné premiérové datum: Musí to být platné datum ve formátu YYYY-MM-DD.")
        else:
            try:
                self.table_DAO.Save(m)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")

    def UpdateMovie(self):
        id = self.table_user_interface.proces_input("ID filmu na úpravu: ")
        Genre_id = self.table_user_interface.proces_input("Nové ID žánru: ")
        Name = self.table_user_interface.proces_input("Nový název filmu: ")
        Length = self.table_user_interface.proces_input("Nová délka filmu (v minutách): ")
        Price = self.table_user_interface.proces_input("Nová cena: ")
        Premiere_date = self.table_user_interface.proces_input("Nové datum premiéry (YYYY-MM-DD): ")
        try:
            m = Movie(Genre_id,Name,Length,Price,Premiere_date,id)
        except IDValueError:
            self.table_user_interface.print_message("Neplatný ID: musí být kladný číslo")
        except GenreIDValueError:
            self.table_user_interface.print_message("Neplatný Genre_id: Musí to být kladné celé číslo.")
        except MovieNameValueError:
            self.table_user_interface.print_message("Neplatný název filmu: Musí být alfanumerický a do 50 znaků.")
        except MovieLengthValueError:
            self.table_user_interface.print_message("Neplatná délka filmu: Musí to být kladné celé číslo.")
        except MoviePriceValueError:
            self.table_user_interface.print_message("Neplatná cena filmu: Musí to být kladné číslo.")
        except MoviePremiereDateValueError:
            self.table_user_interface.print_message("Neplatné premiérové datum: Musí to být platné datum ve formátu YYYY-MM-DD.")
        else:
            try:
                self.table_DAO.Update(m)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")

    def DeleteMovie(self):
        try:
            id = int(self.table_user_interface.proces_input("ID filmu na smazání: "))
        except ValueError:
            self.table_user_interface.print_message("id musí být číslo")
        else:
            try:
                self.table_DAO.Delete(id)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")
    
    def ReadMovie(self):
        self.table_user_interface.interface.print_line()
        try:
            self.table_user_interface.print_read(self.table_DAO.Read())
        except DatabaseError:
            self.table_user_interface.print_message("Selhalo připojení k databázi")

    def LoadMovie(self):
        try:
            list = self.table_DAO.Load()
        except GenreIDValueError:
            self.table_user_interface.print_message("Neplatný Genre_id: Musí to být kladné celé číslo.")
        except MovieNameValueError:
            self.table_user_interface.print_message("Neplatný název filmu: Musí být alfanumerický a do 50 znaků.")
        except MovieLengthValueError:
            self.table_user_interface.print_message("Neplatná délka filmu: Musí to být kladné celé číslo.")
        except MoviePriceValueError:
            self.table_user_interface.print_message("Neplatná cena filmu: Musí to být kladné číslo.")
        except MoviePremiereDateValueError:
            self.table_user_interface.print_message("Neplatné premiérové datum: Musí to být platné datum ve formátu YYYY-MM-DD.")
        else:
            try:
                for i in list:
                    self.table_DAO.Save(i)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")
