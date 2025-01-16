from src.Inputs_check import *
from Error import *

class Rezervation:
    def __init__(self, Customer_id, Screening_id, Date, Ticket_amount, Total_price = 0, id=0):

        if not NumberCheck(id,negative=False):
            raise IDValueError
        self.id = id

        if not NumberCheck(Customer_id, specialchar=None, negative=False):
            raise RezervationCustomerIDValueError
        self.Customer_id = Customer_id

        if not NumberCheck(Screening_id, specialchar=None, negative=False):
            raise RezervationScreeningIDValueError
        self.Screening_id = Screening_id

        if not DateCheck(Date, specialchar="-"):
            raise RezervationDateValueError
        self.Date = Date

        if not NumberCheck(str(Ticket_amount), specialchar=None, negative=False):
            raise RezervationTicketAmountValueError
        self.Ticket_amount = Ticket_amount

        if not NumberCheck(str(Total_price), 10, specialchar=None, negative=False):
            raise RezervationTotalPriceValueError
        self.Total_price = Total_price

    def __str__(self):
        return (f"ID: {self.id}, ID Zákazníka: {self.Customer_id}, ID Promítání: {self.Screening_id}, Datum nákupu: {self.Date}, Množstvý lístků: {self.Ticket_amount}, Celková cena: {self.Total_price}")
