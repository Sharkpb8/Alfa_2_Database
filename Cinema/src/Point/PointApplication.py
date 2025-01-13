from src.Point.PointDAO import PointDAO

class PointApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = PointDAO(self)

    def TransferPoints(self):
        from_id = self.table_user_interface.proces_input("Id zakaznika odkud se odeštou body: ")
        to_id = self.table_user_interface.proces_input("Id zakaznika komu se přičtou body: ")
        ammount = self.table_user_interface.proces_input("Množstvý bodů který se převedou: ")
        self.table_DAO.TransferPoints(from_id, to_id, ammount)

    def Transaction_by_id_Points(self):
        id = self.table_user_interface.proces_input("id zakazníka u koho chcete vypsat transakce bodů: ")
        self.table_DAO.Transaction_by_id(id)

    
    def ReadPoints(self):
        self.table_user_interface.interface.print_line()
        self.table_DAO.Read()

    def LoadPoints(self):
        self.table_DAO.Load()
