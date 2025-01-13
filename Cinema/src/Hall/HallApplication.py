from src.Hall.HallDAO import HallDAO

class HallApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = HallDAO(self)

    def SaveHall(self):
        Name = self.table_user_interface.proces_input("Název sálu: ")
        Type = self.table_user_interface.proces_input("Typ sálu (Standartní/VIP): ")
        self.table_DAO.Save(Name, Type)

    def UpdateHall(self):
        id = self.table_user_interface.proces_input("ID sálu na úpravu: ")
        Name = self.table_user_interface.proces_input("Nový název sálu: ")
        Type = self.table_user_interface.proces_input("Nový typ sálu (Standartní/VIP): ")
        self.table_DAO.Update(id, Name, Type)

    def DeleteHall(self):
        id = self.table_user_interface.proces_input("ID sálu na smazání: ")
        self.table_DAO.Delete(id)
    
    def ReadHall(self):
        self.table_user_interface.interface.print_line()
        self.table_DAO.Read()

    def LoadHall(self):
        self.table_DAO.Load()
