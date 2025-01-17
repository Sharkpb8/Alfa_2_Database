import ast
from src.Genre.GenreInterface import GenreInterface
from src.Movie.MovieInterface import MovieInterface
from src.Hall.HallInterface import HallInterface
from src.Screening.ScreeningInterface import ScreeningInterface
from src.Customer.CustomerInterface import CustomerInterface
from src.Rezervation.RezervationInterface import RezervationInterface
from src.Point.PointInterface import PointInterface
from src.Report.ReportInterface import ReportInterface
from src.IsolationLevel.IsolationLevelInterface import IsolationLevelInterface

class UserInterface:

    def __init__(self):
        self.isrunning = True
        self.table_user_interface = [
            MovieInterface(self),
            GenreInterface(self),
            HallInterface(self),
            ScreeningInterface(self),
            CustomerInterface(self),
            RezervationInterface(self),
            PointInterface(self),
            ReportInterface(self),
            IsolationLevelInterface(self)
        ]

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
        new_input = None
        while (new_input == None):
            new_input = input(f"{message}: ").strip()
            if (len(new_input) < 1):
                print("Neplatné zadání musíte zadat nějaký text")
                new_input = None
        return new_input

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