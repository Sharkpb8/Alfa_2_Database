class Screening:
    def __init__(self, Movie_id, Hall_id, Date, id=0):
        self.id = id
        self.Movie_id = Movie_id
        self.Hall_id = Hall_id
        self.Date = Date

    def __str__(self):
        return (f"ID: {self.id}, ID filmu: {self.Movie_id}, ID sálu: {self.Hall_id}, Datum a čas: {self.Date}")