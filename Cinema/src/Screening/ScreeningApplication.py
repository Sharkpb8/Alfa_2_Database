from src.Screening.ScreeningDAO import ScreeningDAO
from src.Screening.Screening import *
from mysql.connector.errors import *

class ScreeningApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = ScreeningDAO(self)

    def SaveScreening(self):
        Movie_id = self.table_user_interface.proces_input("ID filmu: ")
        Hall_id = self.table_user_interface.proces_input("ID sálu: ")
        Date = self.table_user_interface.proces_input("Datum a čas promítání (YYYY-MM-DD HH:MM): ")
        try:
            s = Screening(Movie_id, Hall_id, Date)
        except ScreeningMovieIDValueError:
            self.table_user_interface.print_message("Neplatný Movie_id: Musí to být kladné celé číslo.")
        except ScreeningHallIDValueError:
            self.table_user_interface.print_message("Neplatný Hall_id: Musí to být kladné celé číslo.")
        except ScreeningDateValueError:
            self.table_user_interface.print_message("Neplatné datum projekce: Musí to být platné datum a čas ve formátu YYYY-MM-DD HH:MM")
        else:
            try:
                self.table_DAO.Save(s)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")

    def UpdateScreening(self):
        id = self.table_user_interface.proces_input("ID promítání na úpravu: ")
        Movie_id = self.table_user_interface.proces_input("Nové ID filmu: ")
        Hall_id = self.table_user_interface.proces_input("Nové ID sálu: ")
        Date = self.table_user_interface.proces_input("Nový datum a čas promítání (YYYY-MM-DD HH:MM): ")
        try:
            s = Screening(Movie_id, Hall_id, Date, id)
        except IDValueError:
            self.table_user_interface.print_message("Neplatný ID: musí být kladný číslo")
        except ScreeningMovieIDValueError:
            self.table_user_interface.print_message("Neplatný Movie_id: Musí to být kladné celé číslo.")
        except ScreeningHallIDValueError:
            self.table_user_interface.print_message("Neplatný Hall_id: Musí to být kladné celé číslo.")
        except ScreeningDateValueError:
            self.table_user_interface.print_message("Neplatné datum projekce: Musí to být platné datum a čas ve formátu YYYY-MM-DD HH:MM")  
        else:
            try:
                self.table_DAO.Update(s)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")

    def DeleteScreening(self):
        try:
            id = int(self.table_user_interface.proces_input("ID promítání na smazání: "))
        except ValueError:
            self.table_user_interface.print_message("id musí být číslo")
        else:
            try:
                self.table_DAO.Delete(id)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")
    
    def ReadScreening(self):
        self.table_user_interface.interface.print_line()
        try:
            self.table_user_interface.print_read(self.table_DAO.Read())
        except DatabaseError:
            self.table_user_interface.print_message("Selhalo připojení k databázi")

    def LoadScreening(self):
        try:
            list = self.table_DAO.Load()
        except ScreeningMovieIDValueError:
            self.table_user_interface.print_message("Neplatný Movie_id: Musí to být kladné celé číslo.")
        except ScreeningHallIDValueError:
            self.table_user_interface.print_message("Neplatný Hall_id: Musí to být kladné celé číslo.")
        except ScreeningDateValueError:
            self.table_user_interface.print_message("Neplatné datum projekce: Musí to být platné datum a čas ve formátu YYYY-MM-DD HH:MM")
        else:
            try:
                for i in list:
                    self.table_DAO.Save(i)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")
