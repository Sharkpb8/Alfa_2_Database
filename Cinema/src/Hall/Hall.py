from src.Inputs_check import *
from Error import *

class Hall:
    def __init__(self, Name, Type, id=0):
        if not NumberCheck(id,negative=False):
            raise IDValueError
        self.id = id

        if not StringCheck(Name, 30):
            raise HallNameValueError
        self.Name = Name

        if not EnumCheck(Type, ['Standartní', 'VIP']):
            raise HallTypeValueError
        self.Type = Type

    def __str__(self):
        return (f"ID: {self.id}, Název: {self.Name}, Typ: {self.Type}")