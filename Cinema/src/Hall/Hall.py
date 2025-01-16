class Hall:
    def __init__(self, Name, Type, id=0):
        self.id = id
        self.Name = Name
        self.Type = Type

    def __str__(self):
        return (f"ID: {self.id}, Název: {self.Name}, Typ: {self.Type}")