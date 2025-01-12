from src.GenreDAO import Save,Update,Delete,Read,LoadGenre

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
                name = input("Jmeno žánru: ")
                Save(name)
            case "Upravit" | "2":
                id = int(input("id upravovaného žánru: "))
                newname = input("jmeno nově upraveného žánru: ")
                Update(id,newname)
            case "Smazat" | "3":
                id = int(input("id žánru který chcete smazat: "))
                Delete(id)
            case "Číst" | "4":
                Read()
            case "Načíst ze souboru" | "5":
                LoadGenre()
            case "Ukončit" | "6":
                running = False
            case _:
                print("Špatná volba")
        print("")