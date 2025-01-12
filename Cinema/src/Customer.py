from src.CustomerDAO import Save, Update, Delete, Read,Get_Customer_point

def showoptions(list):
    """
    Displays the items in a list with numbered options.

    :param list: A list of items to display as options.
    :type list: list
    """
    count = 1
    for i in list:
        print(f"{count}. {i}")
        count += 1

def CustomerCRUD():
    running = True
    while running:
        options = ["Vložit", "Upravit", "Smazat", "Číst", "Načíst ze souboru", "Ukončit"]
        print("Vyberte operaci kterou chcete provést na tabulce Zákazník")
        showoptions(options)
        choice = input("Vybírám si: ")
        match choice:
            case "Vložit" | "1":
                name = input("Jméno zákazníka: ")
                last_name = input("Příjmení zákazníka: ")
                loyalty_program = int(input("Je zákazník členem věrnostního programu? (1 = Ano, 0 = Ne): "))
                if(loyalty_program == 1):
                    loyalty_points = float(input("Počet věrnostních bodů: "))
                    Save(name, last_name, loyalty_program, loyalty_points)
                else:
                    Save(name, last_name, loyalty_program, 0)
            case "Upravit" | "2":
                id = int(input("ID upravovaného zákazníka: "))
                name = input("Nové jméno zákazníka: ")
                last_name = input("Nové příjmení zákazníka: ")
                loyalty_program = int(input("Je zákazník členem věrnostního programu? (1 = Ano, 0 = Ne): "))
                if(loyalty_program == 1):
                    loyalty_points = float(input("Nový počet věrnostních bodů: "))
                    Update(id, name, last_name, loyalty_program, loyalty_points)
                else:
                    Update(id,name,last_name,loyalty_program,Get_Customer_point(id))
            case "Smazat" | "3":
                id = int(input("ID zákazníka, kterého chcete smazat: "))
                Delete(id)
            case "Číst" | "4":
                Read()
            case "Načíst ze souboru" | "5":
                print("Není implementovaný")
            case "Ukončit" | "6":
                running = False
            case _:
                print("Špatná volba")
        print("")