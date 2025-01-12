from src.HallDAO import Save, Update, Delete, Read

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

def HallCRUD():
    running = True
    while running:
        options = ["Vložit", "Upravit", "Smazat", "Číst", "Načíst ze souboru", "Ukončit"]
        print("Vyberte operaci kterou chcete provést na tabulce Sál")
        showoptions(options)
        choice = input("Vybírám si: ")
        match choice:
            case "Vložit" | "1":
                name = input("Jméno sálu: ")
                type = input("Typ sálu (Standartní/VIP): ")
                Save(name, type)
            case "Upravit" | "2":
                id = int(input("ID upravovaného sálu: "))
                name = input("Nové jméno sálu: ")
                type = input("Nový typ sálu (Standartní/VIP): ")
                Update(id, name, type)
            case "Smazat" | "3":
                id = int(input("ID sálu, který chcete smazat: "))
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
