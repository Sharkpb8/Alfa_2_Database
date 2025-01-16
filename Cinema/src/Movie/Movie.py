from src.Inputs_check import *
from Error import *

class Movie:
    def __init__(self, Genre_id, Name, Length, Price, Premiere_date, id=0):

        if not NumberCheck(id,negative=False):
            raise IDValueError
        self.id = id

        if not NumberCheck(Genre_id, specialchar=None, negative=False):
            raise GenreIDValueError
        self.Genre_id = Genre_id

        if not StringCheck(Name, 50):
            raise MovieNameValueError
        self.Name = Name

        if not NumberCheck(str(Length), specialchar=None, negative=False):
            raise MovieLengthValueError
        self.Length = Length

        if not NumberCheck(str(Price), 10, specialchar=None, negative=False):
            raise MoviePriceValueError
        self.Price = Price

        if Premiere_date and not DateCheck(Premiere_date, specialchar="-"):
            raise MoviePremiereDateValueError
        self.Premiere_date = Premiere_date

    def __str__(self):
        return (f"ID: {self.id}, Žánr ID: {self.Genre_id}, Název: {self.Name}, Délka: {self.Length} minut, Cena: {self.Price} Kč, Premiéra: {self.Premiere_date}")