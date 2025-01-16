from src.Hall.HallDAO import HallDAO
from src.Hall.Hall import Hall

class HallApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = HallDAO(self)

    def SaveHall(self):
        Name = self.table_user_interface.proces_input("Název sálu: ")
        Type = self.table_user_interface.proces_input("Typ sálu (Standartní/VIP): ")
        h = Hall(Name, Type)
        self.table_DAO.Save(h)

    def UpdateHall(self):
        id = self.table_user_interface.proces_input("ID sálu na úpravu: ")
        Name = self.table_user_interface.proces_input("Nový název sálu: ")
        Type = self.table_user_interface.proces_input("Nový typ sálu (Standartní/VIP): ")
        h = Hall(Name, Type, id)
        self.table_DAO.Update(h)

    def DeleteHall(self):
        id = self.table_user_interface.proces_input("ID sálu na smazání: ")
        self.table_DAO.Delete(id)
    
    def ReadHall(self):
        self.table_user_interface.interface.print_line()
        self.table_user_interface.print_read(self.table_DAO.Read())

    def LoadHall(self):
        self.table_DAO.Load()
