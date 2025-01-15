from src.Customer.CustomerDAO import CustomerDAO

class CustomerApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = CustomerDAO(self)

    def SaveCustomer(self):
        Name = self.table_user_interface.proces_input("Jméno zákazníka")
        Last_name = self.table_user_interface.proces_input("Příjmení zákazníka")
        loyalty_program = int(self.table_user_interface.proces_input("Je zákazník členem věrnostního programu? (1 = Ano, 0 = Ne)"))
        if(loyalty_program == 1):
            loyalty_points = float(input("Počet věrnostních bodů"))
            self.table_DAO.Save(Name, Last_name, loyalty_program, loyalty_points)
        else:
            self.table_DAO.Save(Name, Last_name, loyalty_program, 0)

    def UpdateCustomer(self):
        id = self.table_user_interface.proces_input("ID zákazníka na úpravu")
        Name = self.table_user_interface.proces_input("Nové jméno zákazníka")
        Last_name = self.table_user_interface.proces_input("Nové příjmení zákazníka")
        loyalty_program = int(self.table_user_interface.proces_input("Je zákazník členem věrnostního programu? (1 = Ano, 0 = Ne)"))
        if(loyalty_program == 1):
            loyalty_points = float(self.table_user_interface.proces_input("Nový počet věrnostních bodů"))
            self.table_DAO.Update(id, Name, Last_name, loyalty_program, loyalty_points)
        else:
            self.table_DAO.Update(id,Name,Last_name,loyalty_program,self.table_DAO.Get_Customer_point(id))

    def DeleteCustomer(self):
        id = self.table_user_interface.proces_input("ID zákazníka na smazání: ")
        self.table_DAO.Delete(id)
    
    def ReadCustomer(self):
        self.table_user_interface.interface.print_line()
        self.table_DAO.Read()

    def LoadCustomer(self):
        self.table_DAO.Load()
    
    def confirmationCustomer(self):
        return self.table_user_interface.confirmation()
    
    def print_messageCustomer(self,message):
        self.table_user_interface.print_message(message)
