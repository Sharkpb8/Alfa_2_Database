from src.Screening.ScreeningApplication import ScreeningApplication

class ScreeningInterface:

    def __init__(self, interface):
        self.isrunning = True
        self.interface = interface
        self.table_application = ScreeningApplication(self)

    def run(self):
        self.isrunning = True
        while self.isrunning:
            self.menu_input()

    def print_message(self, message):
        self.interface.print_line()
        print(message)

    def menu_input(self):
        commands = [
            ("Vložit", self.table_application.SaveScreening),
            ("Upravit", self.table_application.UpdateScreening),
            ("Smazat", self.table_application.DeleteScreening),
            ("Číst", self.table_application.ReadScreening),
            ("načíst ze souboru", self.table_application.LoadScreening),
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

    def print_read(self,list):
        for i in list:
            print(i)