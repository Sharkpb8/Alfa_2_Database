from src.Customer.CustomerDAO import CustomerDAO
from src.Customer.Customer import *

class CustomerApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = CustomerDAO(self)

    #add val function
    #send message with self.table_user_interface.print_message(message)
    def SaveCustomer(self):
        Name = self.table_user_interface.proces_input("Jméno zákazníka")
        Last_name = self.table_user_interface.proces_input("Příjmení zákazníka")
        Registry_date = self.table_user_interface.proces_input("Den registrace (YYYY-MM-DD)")
        loyalty_program = int(self.table_user_interface.proces_input("Je zákazník členem věrnostního programu? (1 = Ano, 0 = Ne)"))
        loyalty_points = 0
        if(loyalty_program == 1):
            loyalty_points = float(self.table_user_interface.proces_input("Počet věrnostních bodů"))
        try:
            c = Customer(Name,Last_name,loyalty_program,loyalty_points,Registry_date)
        except NameValueError:
            print("Neplatné jméno: Musí být alfanumerické a do 30 znaků.")
        except LastNameValueError:
            print("Neplatné příjmení: Musí být alfanumerické a do 30 znaků.")
        except LoyaltyProgramValueError:
            print("Neplatný věrnostní program: Musí být buď 1 (True) nebo 0 (False).")
        except LoyaltyPointsValueError:
            print("Neplatné počet věrnostních bodů: Musí to být kladné desetinné číslo.")
        except RegistryDateValueError:
            print("Neplatný Datum registrace: Musí to být platné datum ve formátu YYYY-MM-DD.")
        else:
            self.table_DAO.Save(c)

    def UpdateCustomer(self):
        id = self.table_user_interface.proces_input("ID zákazníka na úpravu")
        Name = self.table_user_interface.proces_input("Nové jméno zákazníka")
        Last_name = self.table_user_interface.proces_input("Nové příjmení zákazníka")
        Registry_date = self.table_user_interface.proces_input("Nový den registrace (YYYY-MM-DD)")
        loyalty_program = int(self.table_user_interface.proces_input("Je zákazník členem věrnostního programu? (1 = Ano, 0 = Ne)"))
        loyalty_points = 0
        if(loyalty_program == 1):
            loyalty_points = float(self.table_user_interface.proces_input("Nový počet věrnostních bodů"))
        else:
            loyalty_points = self.table_DAO.Get_Customer_point(id)
        try:
            c = Customer(id, Name, Last_name, loyalty_program, loyalty_points,Registry_date)
        except NameValueError:
            print("Neplatné jméno: Musí být alfanumerické a do 30 znaků.")
        except LastNameValueError:
            print("Neplatné příjmení: Musí být alfanumerické a do 30 znaků.")
        except LoyaltyProgramValueError:
            print("Neplatný věrnostní program: Musí být buď 1 (True) nebo 0 (False).")
        except LoyaltyPointsValueError:
            print("Neplatné počet věrnostních bodů: Musí to být kladné desetinné číslo.")
        except RegistryDateValueError:
            print("Neplatný Datum registrace: Musí to být platné datum ve formátu YYYY-MM-DD.")
        else:
            self.table_DAO.Update(c)

    def DeleteCustomer(self):
        try:
            id = int(self.table_user_interface.proces_input("ID zákazníka na smazání: "))
        except ValueError:
            print("id musí být číslo")
        else:
            self.table_DAO.Delete(id)
    
    def ReadCustomer(self):
        self.table_user_interface.interface.print_line()
        self.table_user_interface.print_read(self.table_DAO.Read())

    def LoadCustomer(self):
        self.table_DAO.Load()
    
    def confirmationCustomer(self):
        return self.table_user_interface.confirmation()
    
    def print_messageCustomer(self,message):
        self.table_user_interface.print_message(message)
