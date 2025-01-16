from src.Rezervation.RezervationDAO import RezervationDAO
from src.Rezervation.Rezervation import *

class RezervationApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = RezervationDAO(self)

    #load from json by loading customers to list and than sending that instead of both at same time
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
            self.table_DAO.Save(r)

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
            self.table_DAO.Update(r)

    def DeleteReservation(self):
        try:
            id = int(self.table_user_interface.proces_input("ID rezervace na smazání: "))
        except ValueError:
            self.table_user_interface.print_message("id musí být číslo")
        else:
            self.table_DAO.Delete(id)
    
    def ReadReservation(self):
        self.table_user_interface.interface.print_line()
        self.table_user_interface.print_read(self.table_DAO.Read())

    def LoadReservation(self):
        self.table_DAO.Load()
