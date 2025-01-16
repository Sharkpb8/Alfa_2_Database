from src.Inputs_check import *
from src.Error import *

class Genre:
    def __init__(self, Name, id=0):

        if not NumberCheck(id,decimal=False ,negative=False):
            raise IDValueError
        self.id = int(id)

        if not StringCheck(Name, 30):
            raise GenreNameValueError
        self.Name = Name

    def __str__(self):
        return f"ID: {self.id}, Název: {self.Name}"