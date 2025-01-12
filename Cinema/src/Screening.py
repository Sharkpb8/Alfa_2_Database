from src.ScreeningDAO import Save, Update, Delete, Read

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

def ScreeningCRUD():
    running = True
    while running:
        options = ["Vložit", "Upravit", "Smazat", "Číst", "Načíst ze souboru", "Ukončit"]
        print("Vyberte operaci kterou chcete provést na tabulce Projekce")
        showoptions(options)
        choice = input("Vybírám si: ")
        match choice:
            case "Vložit" | "1":
                movie_id = int(input("ID filmu: "))
                hall_id = int(input("ID sálu: "))
                date = input("Datum a čas (YYYY-MM-DD HH:MM): ")
                Save(movie_id, hall_id, date)
            case "Upravit" | "2":
                id = int(input("ID upravované projekce: "))
                movie_id = int(input("Nový ID filmu: "))
                hall_id = int(input("Nový ID sálu: "))
                date = input("Nové datum a čas (YYYY-MM-DD HH:MM): ")
                Update(id, movie_id, hall_id, date)
            case "Smazat" | "3":
                id = int(input("ID projekce, kterou chcete smazat: "))
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