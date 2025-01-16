from src.Inputs_check import *
from Error import *

class Screening:
    def __init__(self, Movie_id, Hall_id, Date, id=0):

        if not NumberCheck(id,negative=False):
            raise IDValueError
        self.id = id

        if not NumberCheck(Movie_id, specialchar=None, negative=False):
            raise ScreeningMovieIDValueError
        self.Movie_id = Movie_id

        if not NumberCheck(Hall_id, specialchar=None, negative=False):
            raise ScreeningHallIDValueError
        self.Hall_id = Hall_id

        if not DateCheck(Date, specialchar=" "):
            raise ScreeningDateValueError
        self.Date = Date

    def __str__(self):
        return (f"ID: {self.id}, ID filmu: {self.Movie_id}, ID sálu: {self.Hall_id}, Datum a čas: {self.Date}")