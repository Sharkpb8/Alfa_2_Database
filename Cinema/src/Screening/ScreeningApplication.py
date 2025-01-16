from src.Screening.ScreeningDAO import ScreeningDAO
from src.Screening.Screening import Screening

class ScreeningApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = ScreeningDAO(self)

    def SaveScreening(self):
        Movie_id = self.table_user_interface.proces_input("ID filmu: ")
        Hall_id = self.table_user_interface.proces_input("ID sálu: ")
        Date = self.table_user_interface.proces_input("Datum a čas promítání (YYYY-MM-DD HH:MM): ")
        s = Screening(Movie_id, Hall_id, Date)
        self.table_DAO.Save(s)

    def UpdateScreening(self):
        id = self.table_user_interface.proces_input("ID promítání na úpravu: ")
        Movie_id = self.table_user_interface.proces_input("Nové ID filmu: ")
        Hall_id = self.table_user_interface.proces_input("Nové ID sálu: ")
        Date = self.table_user_interface.proces_input("Nový datum a čas promítání (YYYY-MM-DD HH:MM): ")
        s = Screening(Movie_id, Hall_id, Date, id)
        self.table_DAO.Update(s)

    def DeleteScreening(self):
        id = self.table_user_interface.proces_input("ID promítání na smazání: ")
        self.table_DAO.Delete(id)
    
    def ReadScreening(self):
        self.table_user_interface.interface.print_line()
        self.table_user_interface.print_read(self.table_DAO.Read())

    def LoadScreening(self):
        self.table_DAO.Load()
