class Customer:
    def __init__(self,Name,Last_name,loyalty_program,loyalty_points,Registry_date,id = 0):
        self.id = id
        self.Name = Name
        self.Last_name = Last_name
        self.Loyalty_program = loyalty_program
        self.Loyalty_points = loyalty_points
        self.Registry_date = Registry_date
    
    def __str__(self):
        return (f"ID: {self.id}, Jméno: {self.Name}, Příjmení: {self.Last_name}, Člen věrnostního programu: {'Ano' if self.Loyalty_program else 'Ne'}, Body: {self.Loyalty_points}, Registrace: {self.Registry_date}")