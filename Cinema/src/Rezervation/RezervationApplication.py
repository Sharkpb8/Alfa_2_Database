from src.Rezervation.RezervationDAO import RezervationDAO
from src.Rezervation.Rezervation import Rezervation

class RezervationApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = RezervationDAO(self)

    def SaveReservation(self):
        Customer_id = self.table_user_interface.proces_input("ID zákazníka: ")
        Screening_id = self.table_user_interface.proces_input("ID projekce: ")
        Date = self.table_user_interface.proces_input("Datum rezervace (YYYY-MM-DD): ")
        Ticket_ammount = self.table_user_interface.proces_input("Počet lístků: ")
        r = Rezervation(Customer_id, Screening_id, Date, Ticket_ammount)
        self.table_DAO.Save(r)

    def UpdateReservation(self):
        id = self.table_user_interface.proces_input("ID rezervace na úpravu: ")
        Customer_id = self.table_user_interface.proces_input("Nové ID zákazníka: ")
        Screening_id = self.table_user_interface.proces_input("Nové ID projekce: ")
        Date = self.table_user_interface.proces_input("Nové datum rezervace (YYYY-MM-DD): ")
        Ticket_ammount = self.table_user_interface.proces_input("Nový počet lístků: ")
        r = Rezervation(Customer_id, Screening_id, Date, Ticket_ammount,0, id)
        self.table_DAO.Update(r)

    def DeleteReservation(self):
        id = self.table_user_interface.proces_input("ID rezervace na smazání: ")
        self.table_DAO.Delete(id)
    
    def ReadReservation(self):
        self.table_user_interface.interface.print_line()
        self.table_user_interface.print_read(self.table_DAO.Read())

    def LoadReservation(self):
        self.table_DAO.Load()
