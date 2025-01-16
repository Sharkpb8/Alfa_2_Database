from src.Inputs_check import *
from Error import *

class Customer:
    def __init__(self,Name,Last_name,loyalty_program,loyalty_points,Registry_date,id = 0):

        if not NumberCheck(id,decimal=False ,negative=False):
            raise IDValueError
        self.id = int(id)

        if not StringCheck(Name, 30):
            raise NameValueError
        self.Name = Name

        if not StringCheck(Last_name, 30):
            raise LastNameValueError
        self.Last_name = Last_name

        if not BoolCheck(loyalty_program, 1, 0):
            raise LoyaltyProgramValueError
        self.Loyalty_program = loyalty_program

        if not NumberCheck(loyalty_points, 10, negative=False):
            raise LoyaltyPointsValueError
        self.Loyalty_points = float(loyalty_points)

        if not DateCheck(Registry_date, specialchar="-"):
            raise RegistryDateValueError
        self.Registry_date = Registry_date
    
    def __str__(self):
        return (f"ID: {self.id}, Jméno: {self.Name}, Příjmení: {self.Last_name}, Člen věrnostního programu: {'Ano' if self.Loyalty_program else 'Ne'}, Body: {self.Loyalty_points}, Registrace: {self.Registry_date}")