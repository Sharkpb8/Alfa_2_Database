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


def Run():
    running = True
    while running:
        options = ["Načís ze souboru","Ukončit"]
        print("Zadejte název tabulky, se kterou chcete pracovat.")
        showoptions(options)
        choice = input("Vybírám si: ")
        match choice:
            case "Načís ze souboru" | "1":
                print("Není implementovaný")
            case "Ukončit" | "2":
                running = False
            case _:
                print("Špatná volba")
        print("")

if __name__ == "__main__":
    Run()