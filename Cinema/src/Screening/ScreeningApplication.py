from src.Screening.ScreeningDAO import ScreeningDAO
from src.Screening.Screening import *

class ScreeningApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = ScreeningDAO(self)

    #add val function
    #send message with self.table_user_interface.print_message(message)
    #load from json by loading customers to list and than sending that instead of both at same time
    #dont convert types here but in class
    def SaveScreening(self):
        Movie_id = self.table_user_interface.proces_input("ID filmu: ")
        Hall_id = self.table_user_interface.proces_input("ID sálu: ")
        Date = self.table_user_interface.proces_input("Datum a čas promítání (YYYY-MM-DD HH:MM): ")
        try:
            s = Screening(Movie_id, Hall_id, Date)
        except ScreeningMovieIDValueError:
            print("Neplatný Movie_id: Musí to být kladné celé číslo.")
        except ScreeningHallIDValueError:
            print("Neplatný Hall_id: Musí to být kladné celé číslo.")
        except ScreeningDateValueError:
            print("Neplatné datum projekce: Musí to být platné datum a čas ve formátu YYYY-MM-DD HH:MM")
        else:
            self.table_DAO.Save(s)

    def UpdateScreening(self):
        id = self.table_user_interface.proces_input("ID promítání na úpravu: ")
        Movie_id = self.table_user_interface.proces_input("Nové ID filmu: ")
        Hall_id = self.table_user_interface.proces_input("Nové ID sálu: ")
        Date = self.table_user_interface.proces_input("Nový datum a čas promítání (YYYY-MM-DD HH:MM): ")
        try:
            s = Screening(Movie_id, Hall_id, Date, id)
        except IDValueError:
            print("Neplatný ID: musí být kladný číslo")
        except ScreeningMovieIDValueError:
            print("Neplatný Movie_id: Musí to být kladné celé číslo.")
        except ScreeningHallIDValueError:
            print("Neplatný Hall_id: Musí to být kladné celé číslo.")
        except ScreeningDateValueError:
            print("Neplatné datum projekce: Musí to být platné datum a čas ve formátu YYYY-MM-DD HH:MM")  
        else:
            self.table_DAO.Update(s)

    def DeleteScreening(self):
        try:
            id = int(self.table_user_interface.proces_input("ID promítání na smazání: "))
        except ValueError:
            print("id musí být číslo")
        else:
            self.table_DAO.Delete(id)
    
    def ReadScreening(self):
        self.table_user_interface.interface.print_line()
        self.table_user_interface.print_read(self.table_DAO.Read())

    def LoadScreening(self):
        self.table_DAO.Load()
