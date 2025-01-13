from src.Customer.CustomerDAO import CustomerDAO

class CustomerApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = CustomerDAO(self)

    def SaveCustomer(self):
        Name = self.table_user_interface.proces_input("Jméno zákazníka: ")
        Last_name = self.table_user_interface.proces_input("Příjmení zákazníka: ")
        Loyalty_program = self.table_user_interface.proces_input("Chcete připojit zákazníka do věrnostního programu? (Ano/Ne): ")
        self.table_DAO.Save(Name, Last_name, Loyalty_program)

    def UpdateCustomer(self):
        id = self.table_user_interface.proces_input("ID zákazníka na úpravu: ")
        Name = self.table_user_interface.proces_input("Nové jméno zákazníka: ")
        Last_name = self.table_user_interface.proces_input("Nové příjmení zákazníka: ")
        Loyalty_program = self.table_user_interface.proces_input("Chcete připojit zákazníka do věrnostního programu? (Ano/Ne): ")
        self.table_DAO.Update(id, Name, Last_name, Loyalty_program)

    def DeleteCustomer(self):
        id = self.table_user_interface.proces_input("ID zákazníka na smazání: ")
        self.table_DAO.Delete(id)
    
    def ReadCustomer(self):
        self.table_user_interface.interface.print_line()
        self.table_DAO.Read()

    def LoadCustomer(self):
        self.table_DAO.Load()
