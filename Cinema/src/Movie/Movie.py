from src.Inputs_check import *
from src.Error import *

class Movie:
    def __init__(self, Genre_id, Name, Length, Price, Premiere_date, id=0):

        if not NumberCheck(str(id),decimal=False ,negative=False):
            raise IDValueError
        self.id = int(id)

        if not NumberCheck(str(Genre_id),decimal=False , negative=False):
            raise GenreIDValueError
        self.Genre_id = int(Genre_id)

        if not StringCheck(Name, 50):
            raise MovieNameValueError
        self.Name = Name

        if not NumberCheck(str(Length),decimal=False, negative=False):
            raise MovieLengthValueError
        self.Length = int(Length)

        if not NumberCheck(str(Price), 10, negative=False):
            raise MoviePriceValueError
        self.Price = float(Price)

        if Premiere_date and not DateCheck(str(Premiere_date), specialchar="-"):
            raise MoviePremiereDateValueError
        self.Premiere_date = Premiere_date

    def __str__(self):
        return (f"ID: {self.id}, Žánr ID: {self.Genre_id}, Název: {self.Name}, Délka: {self.Length} minut, Cena: {self.Price} Kč, Premiéra: {self.Premiere_date}")