import ast

class UserInterface:

    def __init__(self):
        self.isrunning = True
        self.table_user_interface = []

    def run(self):
        while self.isrunning:
            self.menu_input()

    def print_line(self, symbol="="):
        print(symbol * 50)

    def print_message(self, message):
        self.print_line()
        print(message)

    def new_input(self,message):
        self.print_line()
        new_task = None
        while (new_task == None):
            new_task = input(f"{message}: ").strip()
            if (len(new_task) < 1):
                print("Neplatné zadání musíte zadat nějaký text")
                new_task = None
        return self.convert_input(new_task)

    def menu_input(self):
        commands = [
            ("Úprava Filmů", self.table_user_interface[0].menu_input),
            ("Úprava Žánrů", self.table_user_interface[1].menu_input),
            ("Úprava Sálů", self.table_user_interface[2].menu_input),
            ("Úprava Promítání", self.table_user_interface[3].menu_input),
            ("Úprava Zákazníků", self.table_user_interface[4].menu_input),
            ("Úprava Rezervací", self.table_user_interface[5].menu_input),
            ("Transakce bodů", self.table_user_interface[6].menu_input),
            ("Souhrné reporty", self.table_user_interface[7].menu_input),
            ("Nastavení izolačního levelu", self.table_user_interface[8].menu_input),
            ("Ukončit program", self.terminate),
        ]

        self.print_line()
        print("Vyberte operaci:")
        num = 0
        for label, action in commands:
            num += 1
            print("\t" + str(num) + ". " + label)

        choosen_num = None
        while (choosen_num == None):
            choosen_num = input("Zadejte číslo příkazu (1-" + str(len(commands)) + "): ").strip()
            try:
                choosen_num = int(choosen_num)
                if (not 0 < choosen_num <= len(commands)):
                    raise Exception()
            except:
                print("Neplatné zadání musíte zadat číslo mezi 1 až " + str(len(commands)))
                choosen_num = None

        commands[choosen_num - 1][1]()
    
    def terminate(self):
        self.isrunning = False

    def convert_input(self,value):
        """
        Tries to convert a string input into a Python literal (e.g., int, float, list, etc.).
        If conversion fails, returns the original string.

        :param value: The input string to be evaluated.
        :type value: str
        :return: The converted value or the original string if conversion fails.
        :rtype: any
        """
        try:
            return ast.literal_eval(value)
        except (ValueError, SyntaxError):
            return value