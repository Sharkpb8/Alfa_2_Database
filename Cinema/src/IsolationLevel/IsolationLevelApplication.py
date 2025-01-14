from src.IsolationLevel.IsolationLevelDAO import IsolationLevelDAO

class IsolationLevelApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = IsolationLevelDAO(self)

    def SetIsolationLevel(self):
        Level = None
        while not Level:
            Level = self.table_user_interface.proces_input("Izolační úroveň: ")

        self.table_DAO.Set(Level)
    
    def ReadIsolationLevel(self):
        self.table_user_interface.interface.print_line()
        self.table_DAO.Read()