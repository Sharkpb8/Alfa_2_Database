from src.MovieDAO import Save, Update, Delete, Read

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

def MovieCRUD():
    running = True
    while running:
        options = ["Vložit", "Upravit", "Smazat", "Číst", "Načíst ze souboru", "Ukončit"]
        print("Vyberte operaci kterou chcete provést na tabulce Film")
        showoptions(options)
        choice = input("Vybírám si: ")
        match choice:
            case "Vložit" | "1":
                genre_id = int(input("ID žánru: "))
                name = input("Jméno filmu: ")
                length = int(input("Délka filmu (minuty): "))
                price = float(input("Cena: "))
                premiere_date = input("Datum premiéry (YYYY-MM-DD): ")
                Save(genre_id, name, length, price, premiere_date)
            case "Upravit" | "2":
                id = int(input("ID upravovaného filmu: "))
                genre_id = int(input("Nové ID žánru: "))
                name = input("Nové jméno filmu: ")
                length = int(input("Nová délka filmu (minuty): "))
                price = float(input("Nová cena: "))
                premiere_date = input("Nový datum premiéry (YYYY-MM-DD): ")
                Update(id, genre_id, name, length, price, premiere_date)
            case "Smazat" | "3":
                id = int(input("ID filmu, který chcete smazat: "))
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