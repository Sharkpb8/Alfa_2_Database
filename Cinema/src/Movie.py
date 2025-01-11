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

def MovieCRUD():
    running = True
    while running:
        options = ["Vložit","Upravit","Smazat","Číst","Načíst ze souboru","Ukončit"]
        print("Zadejte název tabulky, se kterou chcete pracovat.")
        showoptions(options)
        choice = input("Vybírám si: ")
        match choice:
            case "Film" | "1":
                print("Není implementovaný")
            case "Žánr" | "2":
                print("Není implementovaný")
            case "Sál" | "3":
                print("Není implementovaný")
            case "Promítání" | "4":
                print("Není implementovaný")
            case "Zákazník" | "5":
                print("Není implementovaný")
            case "Rezervace" | "6":
                print("Není implementovaný")
            case "Jiný" | "7":
                print("Není implementovaný")
            case "Ukončit" | "8":
                running = False
            case _:
                print("Špatná volba")
        print("")