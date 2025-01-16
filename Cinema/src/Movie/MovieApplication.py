from src.Movie.MovieDAO import MovieDAO
from src.Movie.Movie import *

class MovieApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = MovieDAO(self)

    #load from json by loading customers to list and than sending that instead of both at same time
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
            self.table_DAO.Save(m)

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
            self.table_DAO.Update(m)

    def DeleteMovie(self):
        try:
            id = int(self.table_user_interface.proces_input("ID filmu na smazání: "))
        except ValueError:
            self.table_user_interface.print_message("id musí být číslo")
        else:
            self.table_DAO.Delete(id)
    
    def ReadMovie(self):
        self.table_user_interface.interface.print_line()
        self.table_user_interface.print_read(self.table_DAO.Read())

    def LoadMovie(self):
        self.table_DAO.Load()
