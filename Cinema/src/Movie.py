from src.MovieDAO import Save,Update,Delete,Read

def showoptions(list):
    """
    Displays the items in a list with numbered options.

    :param list: A list of items to display as options.
    :type list: list
    """
    count =1
    for i in list:
        print(f"{count}. {i}")
        count +=1

def GenreCRUD():
    running = True
    while running:
        options = ["Vložit","Upravit","Smazat","Číst","Načíst ze souboru","Ukončit"]
        print("Vyberte operaci kterou chcete provést na tabulce Žánr")
        showoptions(options)
        choice = input("Vybírám si: ")
        match choice:
            case "Vložit" | "1":
                
            case "Upravit" | "2":
                print("Není implementovaný")
            case "Smazat" | "3":
                print("Není implementovaný")
            case "Číst" | "4":
                print("Není implementovaný")
            case "Načíst ze souboru" | "5":
                print("Není implementovaný")
            case "Ukončit" | "6":
                running = False
            case _:
                print("Špatná volba")
        print("")