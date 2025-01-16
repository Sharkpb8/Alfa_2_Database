class Rezervation:
    def __init__(self, Customer_id, Screening_id, Date, Ticket_amount, Total_price = 0, id=0):
        self.id = id
        self.Customer_id = Customer_id
        self.Screening_id = Screening_id
        self.Date = Date
        self.Ticket_amount = Ticket_amount
        self.Total_price = Total_price

    def __str__(self):
        return (f"ID: {self.id}, ID Zákazníka: {self.Customer_id}, ID Promítání: {self.Screening_id}, Datum nákupu: {self.Date}, Množstvý lístků: {self.Ticket_amount}, Celková cena: {self.Total_price}")
