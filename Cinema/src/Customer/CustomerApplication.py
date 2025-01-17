from src.Customer.CustomerDAO import CustomerDAO
from src.Customer.Customer import *
from mysql.connector.errors import *

class CustomerApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = CustomerDAO(self)

    def SaveCustomer(self):
        Name = self.table_user_interface.proces_input("Jméno zákazníka")
        Last_name = self.table_user_interface.proces_input("Příjmení zákazníka")
        Registry_date = self.table_user_interface.proces_input("Den registrace (YYYY-MM-DD)")
        loyalty_program = self.table_user_interface.proces_input("Je zákazník členem věrnostního programu? (1 = Ano, 0 = Ne)")
        loyalty_points = 0
        if(loyalty_program == "1"):
            loyalty_points = self.table_user_interface.proces_input("Počet věrnostních bodů")
        try:
            if(loyalty_program not in ["0","1"]):
                raise LoyaltyPointsValueError
            c = Customer(Name,Last_name,loyalty_program,loyalty_points,Registry_date)
        except NameValueError:
            self.table_user_interface.print_message("Neplatné jméno: Musí být alfanumerické a do 30 znaků.")
        except LastNameValueError:
            self.table_user_interface.print_message("Neplatné příjmení: Musí být alfanumerické a do 30 znaků.")
        except LoyaltyProgramValueError:
            self.table_user_interface.print_message("Neplatný věrnostní program: Musí být buď 1 (True) nebo 0 (False).")
        except LoyaltyPointsValueError:
            self.table_user_interface.print_message("Neplatné počet věrnostních bodů: Musí to být kladné desetinné číslo.")
        except RegistryDateValueError:
            self.table_user_interface.print_message("Neplatný Datum registrace: Musí to být platné datum ve formátu YYYY-MM-DD.")
        else:
            try:
                self.table_DAO.Save(c)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")

    #need fix check id
    def UpdateCustomer(self,phenomenon):
        id = self.table_user_interface.proces_input("ID zákazníka na úpravu")
        Name = self.table_user_interface.proces_input("Nové jméno zákazníka")
        Last_name = self.table_user_interface.proces_input("Nové příjmení zákazníka")
        Registry_date = self.table_user_interface.proces_input("Nový den registrace (YYYY-MM-DD)")
        loyalty_program = self.table_user_interface.proces_input("Je zákazník členem věrnostního programu? (1 = Ano, 0 = Ne)")
        if(loyalty_program == "1"):
            loyalty_points = self.table_user_interface.proces_input("Nový počet věrnostních bodů")
        else:
            loyalty_points = 0
            try:
                int(id)
            except ValueError:
                id = "id"
            else:
                loyalty_points = self.table_DAO.Get_Customer_point(id)
        try:
            if(loyalty_program not in ["0","1"]):
                raise LoyaltyPointsValueError
            c = Customer(Name, Last_name, loyalty_program, loyalty_points,Registry_date,id)
        except IDValueError:
            self.table_user_interface.print_message("Neplatný ID: musí být kladný číslo")
        except NameValueError:
            self.table_user_interface.print_message("Neplatné jméno: Musí být alfanumerické a do 30 znaků.")
        except LastNameValueError:
            self.table_user_interface.print_message("Neplatné příjmení: Musí být alfanumerické a do 30 znaků.")
        except LoyaltyProgramValueError:
            self.table_user_interface.print_message("Neplatný věrnostní program: Musí být buď 1 (True) nebo 0 (False).")
        except LoyaltyPointsValueError:
            self.table_user_interface.print_message("Neplatné počet věrnostních bodů: Musí to být kladné číslo.")
        except RegistryDateValueError:
            self.table_user_interface.print_message("Neplatný Datum registrace: Musí to být platné datum ve formátu YYYY-MM-DD.")
        else:
            try:
                self.table_DAO.Update(c,phenomenon)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")

    def DeleteCustomer(self):
        try:
            id = int(self.table_user_interface.proces_input("ID zákazníka na smazání: "))
        except ValueError:
            self.table_user_interface.print_message("id musí být číslo")
        else:
            try:
                self.table_DAO.Delete(id)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")
    
    def ReadCustomer(self):
        self.table_user_interface.interface.print_line()
        try:
            self.table_user_interface.print_read(self.table_DAO.Read())
        except DatabaseError:
            self.table_user_interface.print_message("Selhalo připojení k databázi")

    def LoadCustomer(self):
        try:
            list = self.table_DAO.Load()
        except NameValueError:
            self.table_user_interface.print_message("Neplatné jméno: Musí být alfanumerické a do 30 znaků.")
        except LastNameValueError:
            self.table_user_interface.print_message("Neplatné příjmení: Musí být alfanumerické a do 30 znaků.")
        except LoyaltyProgramValueError:
            self.table_user_interface.print_message("Neplatný věrnostní program: Musí být buď 1 (True) nebo 0 (False).")
        except LoyaltyPointsValueError:
            self.table_user_interface.print_message("Neplatné počet věrnostních bodů: Musí to být kladné číslo.")
        except RegistryDateValueError:
            self.table_user_interface.print_message("Neplatný Datum registrace: Musí to být platné datum ve formátu YYYY-MM-DD.")
        else:
            try:
                for i in list:
                    self.table_DAO.Save(i)
            except DatabaseError:
                self.table_user_interface.print_message("Selhalo připojení k databázi")
    
    def confirmationCustomer(self):
        return self.table_user_interface.confirmation()
    
    def print_messageCustomer(self,message):
        self.table_user_interface.print_message(message)
