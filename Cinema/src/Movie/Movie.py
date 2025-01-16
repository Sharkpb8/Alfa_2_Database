class Movie:
    def __init__(self, Genre_id, Name, Length, Price, Premiere_date, id=0):
        self.id = id
        self.Genre_id = Genre_id
        self.Name = Name
        self.Length = Length
        self.Price = Price
        self.Premiere_date = Premiere_date

    def __str__(self):
        return (f"ID: {self.id}, Žánr ID: {self.Genre_id}, Název: {self.Name}, Délka: {self.Length} minut, Cena: {self.Price} Kč, Premiéra: {self.Premiere_date}")