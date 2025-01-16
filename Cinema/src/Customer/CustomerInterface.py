from src.Customer.CustomerApplication import CustomerApplication

class CustomerInterface:

    def __init__(self, interface):
        self.isrunning = True
        self.interface = interface
        self.table_application = CustomerApplication(self)

    def run(self):
        self.isrunning = True
        while self.isrunning:
            self.menu_input()

    def print_message(self, message):
        self.interface.print_line()
        print(message)

    def menu_input(self):
        commands = [
            ("Vložit", self.table_application.SaveCustomer),
            ("Upravit", self.table_application.UpdateCustomer),
            ("Smazat", self.table_application.DeleteCustomer),
            ("Číst", self.table_application.ReadCustomer),
            ("načíst ze souboru", self.table_application.LoadCustomer),
            ("Ukončit program", self.terminate),
        ]

        self.interface.print_line()
        print("Vyberte operaci:")
        num = 0
        for label, action in commands:
            num += 1
            print("\t" + str(num) + ". " + label)

        choosen_num = None
        while choosen_num is None:
            choosen_num = input("Zadejte číslo příkazu (1-" + str(len(commands)) + "): ").strip()
            try:
                choosen_num = int(choosen_num)
                if not 0 < choosen_num <= len(commands):
                    raise Exception()
            except:
                print("Neplatné zadání musíte zadat číslo mezi 1 až " + str(len(commands)))
                choosen_num = None

        commands[choosen_num - 1][1]()
        if self.isrunning:
            self.run()

    def terminate(self):
        self.isrunning = False

    def proces_input(self, message):
        return self.interface.new_input(message)

    def confirmation(self):
        self.interface.print_line()
        answer = None
        while not answer:
            try:
                answer = input("Opravdu chcete provést tuto akci? (ano/ne): ").lower()
                if(answer not in ["ano","ne"]):
                    raise Exception
            except Exception:
                print("Neplatné zadání musíte zadat číslo 0 nebo 1")
                answer = None
        if(answer == "ano"):
            return True
        else:
            return False
    
    def print_read(self,list):
        for i in list:
            print(i)
