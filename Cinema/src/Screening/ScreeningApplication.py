from src.Screening.ScreeningDAO import ScreeningDAO

class ScreeningApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = ScreeningDAO(self)

    def SaveScreening(self):
        Movie_id = self.table_user_interface.proces_input("ID filmu: ")
        Hall_id = self.table_user_interface.proces_input("ID sálu: ")
        Date = self.table_user_interface.proces_input("Datum a čas projekce (YYYY-MM-DD HH:MM:SS): ")
        self.table_DAO.Save(Movie_id, Hall_id, Date)

    def UpdateScreening(self):
        id = self.table_user_interface.proces_input("ID projekce na úpravu: ")
        Movie_id = self.table_user_interface.proces_input("Nové ID filmu: ")
        Hall_id = self.table_user_interface.proces_input("Nové ID sálu: ")
        Date = self.table_user_interface.proces_input("Nový datum a čas projekce (YYYY-MM-DD HH:MM:SS): ")
        self.table_DAO.Update(id, Movie_id, Hall_id, Date)

    def DeleteScreening(self):
        id = self.table_user_interface.proces_input("ID projekce na smazání: ")
        self.table_DAO.Delete(id)
    
    def ReadScreening(self):
        self.table_user_interface.interface.print_line()
        self.table_DAO.Read()

    def LoadScreening(self):
        self.table_DAO.Load()
