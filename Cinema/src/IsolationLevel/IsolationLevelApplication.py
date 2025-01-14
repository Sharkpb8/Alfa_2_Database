from src.IsolationLevel.IsolationLevelDAO import IsolationLevelDAO

class IsolationLevelApplication:

    def __init__(self, table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = IsolationLevelDAO(self)

    def SetIsolationLevel(self):
        commands = [
            ("Read uncommitted", "READ UNCOMMITTED"),
            ("Read committed", "READ COMMITTED"),
            ("Repeatable read", "REPEATABLE READ"),
            ("Serializable", "SERIALIZABLE"),
        ]

        self.table_user_interface.interface.print_line()
        print("Vyberte izolační level:")
        num = 0
        for label, action in commands:
            num += 1
            print("\t" + str(num) + ". " + label)

        choosen_num = None
        while choosen_num is None:
            choosen_num = input("Zadejte číslo izolačního levelu (1-" + str(len(commands)) + "): ").strip()
            try:
                choosen_num = int(choosen_num)
                if not 0 < choosen_num <= len(commands):
                    raise Exception()
            except:
                print("Neplatné zadání musíte zadat číslo mezi 1 až " + str(len(commands)))
                choosen_num = None
        self.table_DAO.Set(commands[choosen_num-1][1])
    
    def ReadIsolationLevel(self):
        self.table_user_interface.interface.print_line()
        self.table_DAO.Read()