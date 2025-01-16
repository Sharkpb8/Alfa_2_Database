from src.Inputs_check import *
from src.Error import *

class Rezervation:
    def __init__(self, Customer_id, Screening_id, Date, Ticket_amount, Total_price = 0, id=0):

        if not NumberCheck(str(id),decimal=False ,negative=False):
            raise IDValueError
        self.id = int(id)

        if not NumberCheck(str(Customer_id),decimal=False , negative=False):
            raise RezervationCustomerIDValueError
        self.Customer_id = int(Customer_id)

        if not NumberCheck(str(Screening_id),decimal=False , negative=False):
            raise RezervationScreeningIDValueError
        self.Screening_id = int(Screening_id)

        if not DateCheck(str(Date), specialchar="-"):
            raise RezervationDateValueError
        self.Date = Date

        if not NumberCheck(str(Ticket_amount), decimal=False, negative=False):
            raise RezervationTicketAmountValueError
        self.Ticket_amount = int(Ticket_amount)

        if not NumberCheck(str(Total_price), 10, negative=False):
            raise RezervationTotalPriceValueError
        self.Total_price = float(Total_price)

    def __str__(self):
        return (f"ID: {self.id}, ID Zákazníka: {self.Customer_id}, ID Promítání: {self.Screening_id}, Datum nákupu: {self.Date}, Množstvý lístků: {self.Ticket_amount}, Celková cena: {self.Total_price}")
