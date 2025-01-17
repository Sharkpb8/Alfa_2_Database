from src.Rezervation.RezervationDAO import RezervationDAO
from src.Rezervation.Rezervation import *
from mysql.connector.errors import *

class RezervationApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = RezervationDAO(self)

    def SaveReservation(self):
        Customer_id = self.table_user_interface.proces_input("ID zákazníka: ")
        Screening_id = self.table_user_interface.proces_input("ID projekce: ")
        Date = self.table_user_interface.proces_input("Datum rezervace (YYYY-MM-DD): ")
        Ticket_ammount = self.table_user_interface.proces_input("Počet lístků: ")
        try:
            r = Rezervation(Customer_id, Screening_id, Date, Ticket_ammount)
        except RezervationCustomerIDValueError:
            self.table_user_interface.print_message("Neplatný Customer_id: Musí to být kladné celé číslo.")
        except RezervationScreeningIDValueError:
            self.table_user_interface.print_message("Neplatný Screening_id: Musí to být kladné celé číslo.")
        except RezervationDateValueError:
            self.table_user_interface.print_message("Neplatné datum rezervace: Musí to být platné datum ve formátu YYYY-MM-DD.")
        except RezervationTicketAmountValueError:
            self.table_user_interface.print_message("Neplatný počet vstupenek: Musí to být kladné celé číslo.")
        except RezervationTotalPriceValueError:
            self.table_user_interface.print_message("Neplatná celková cena: Musí to být kladné desetinné číslo.")
        else:
            try:
                self.table_DAO.Save(r)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")

    def UpdateReservation(self):
        id = self.table_user_interface.proces_input("ID rezervace na úpravu: ")
        Customer_id = self.table_user_interface.proces_input("Nové ID zákazníka: ")
        Screening_id = self.table_user_interface.proces_input("Nové ID projekce: ")
        Date = self.table_user_interface.proces_input("Nové datum rezervace (YYYY-MM-DD): ")
        Ticket_ammount = self.table_user_interface.proces_input("Nový počet lístků: ")
        try:
            r = Rezervation(Customer_id, Screening_id, Date, Ticket_ammount,0, id)
        except IDValueError:
            self.table_user_interface.print_message("Neplatný ID: musí být kladný číslo")
        except RezervationCustomerIDValueError:
            self.table_user_interface.print_message("Neplatný Customer_id: Musí to být kladné celé číslo.")
        except RezervationScreeningIDValueError:
            self.table_user_interface.print_message("Neplatný Screening_id: Musí to být kladné celé číslo.")
        except RezervationDateValueError:
            self.table_user_interface.print_message("Neplatné datum rezervace: Musí to být platné datum ve formátu YYYY-MM-DD.")
        except RezervationTicketAmountValueError:
            self.table_user_interface.print_message("Neplatný počet vstupenek: Musí to být kladné celé číslo.")
        except RezervationTotalPriceValueError:
            self.table_user_interface.print_message("Neplatná celková cena: Musí to být kladné desetinné číslo.")
        else:
            try:
                self.table_DAO.Update(r)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")

    def DeleteReservation(self):
        try:
            id = int(self.table_user_interface.proces_input("ID rezervace na smazání: "))
        except ValueError:
            self.table_user_interface.print_message("id musí být číslo")
        else:
            try:
                self.table_DAO.Delete(id)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")
    
    def ReadReservation(self):
        self.table_user_interface.interface.print_line()
        try:
            self.table_user_interface.print_read(self.table_DAO.Read())
        except DatabaseError:
            self.table_user_interface.print_message("Selhalo připojení k databázi")

    def LoadReservation(self):
        try:
            list = self.table_DAO.Load()
        except RezervationCustomerIDValueError:
            self.table_user_interface.print_message("Neplatný Customer_id: Musí to být kladné celé číslo.")
        except RezervationScreeningIDValueError:
            self.table_user_interface.print_message("Neplatný Screening_id: Musí to být kladné celé číslo.")
        except RezervationDateValueError:
            self.table_user_interface.print_message("Neplatné datum rezervace: Musí to být platné datum ve formátu YYYY-MM-DD.")
        except RezervationTicketAmountValueError:
            self.table_user_interface.print_message("Neplatný počet vstupenek: Musí to být kladné celé číslo.")
        except RezervationTotalPriceValueError:
            self.table_user_interface.print_message("Neplatná celková cena: Musí to být kladné desetinné číslo.")
        else:
            try:
                for i in list:
                    self.table_DAO.Save(i)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")
