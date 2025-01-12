from src.RezervationDAO import Save, Update, Delete, Read

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

def ReservationCRUD():
    running = True
    while running:
        options = ["Vložit", "Upravit", "Smazat", "Číst", "Načíst ze souboru", "Ukončit"]
        print("Vyberte operaci kterou chcete provést na tabulce Rezervace")
        showoptions(options)
        choice = input("Vybírám si: ")
        match choice:
            case "Vložit" | "1":
                customer_id = int(input("ID zákazníka: "))
                screening_id = int(input("ID promítání: "))
                date = input("Datum rezervace (YYYY-MM-DD): ")
                ticket_amount = int(input("Počet lístků: "))
                Save(customer_id, screening_id, date, ticket_amount)
            case "Upravit" | "2":
                id = int(input("ID upravované rezervace: "))
                customer_id = int(input("Nové ID zákazníka: "))
                screening_id = int(input("Nové ID promítání: "))
                date = input("Nové datum rezervace (YYYY-MM-DD): ")
                ticket_amount = int(input("Nový počet lístků: "))
                Update(id, customer_id, screening_id, date, ticket_amount)
            case "Smazat" | "3":
                id = int(input("ID rezervace, kterou chcete smazat: "))
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