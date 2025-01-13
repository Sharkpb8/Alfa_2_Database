from src.Rezervation.RezervationDAO import RezervationDAO

class ReservationApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = RezervationDAO(self)

    def SaveReservation(self):
        Customer_id = self.table_user_interface.proces_input("ID zákazníka: ")
        Screening_id = self.table_user_interface.proces_input("ID projekce: ")
        Date = self.table_user_interface.proces_input("Datum rezervace (YYYY-MM-DD): ")
        Ticket_ammount = self.table_user_interface.proces_input("Počet lístků: ")
        Total_price = self.table_user_interface.proces_input("Celková cena: ")
        self.table_DAO.Save(Customer_id, Screening_id, Date, Ticket_ammount, Total_price)

    def UpdateReservation(self):
        id = self.table_user_interface.proces_input("ID rezervace na úpravu: ")
        Customer_id = self.table_user_interface.proces_input("Nové ID zákazníka: ")
        Screening_id = self.table_user_interface.proces_input("Nové ID projekce: ")
        Date = self.table_user_interface.proces_input("Nové datum rezervace (YYYY-MM-DD): ")
        Ticket_ammount = self.table_user_interface.proces_input("Nový počet lístků: ")
        Total_price = self.table_user_interface.proces_input("Nová celková cena: ")
        self.table_DAO.Update(id, Customer_id, Screening_id, Date, Ticket_ammount, Total_price)

    def DeleteReservation(self):
        id = self.table_user_interface.proces_input("ID rezervace na smazání: ")
        self.table_DAO.Delete(id)
    
    def ReadReservation(self):
        self.table_user_interface.interface.print_line()
        self.table_DAO.Read()

    def LoadReservation(self):
        self.table_DAO.Load()