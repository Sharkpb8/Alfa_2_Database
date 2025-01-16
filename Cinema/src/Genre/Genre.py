class Genre:
    def __init__(self, Name, id=0):
        self.id = id
        self.Name = Name

    def __str__(self):
        return f"ID: {self.id}, Název: {self.Name}"