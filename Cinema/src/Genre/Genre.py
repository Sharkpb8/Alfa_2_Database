from src.Inputs_check import *
from Error import *

class Genre:
    def __init__(self, Name, id=0):

        if not NumberCheck(id,negative=False):
            raise IDValueError
        self.id = id

        if not StringCheck(Name, 30):
            raise GenreNameValueError("Neplatný název žánru: Musí být alfanumerický a do 30 znaků.")
        self.Name = Name

    def __str__(self):
        return f"ID: {self.id}, Název: {self.Name}"