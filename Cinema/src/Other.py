from src.CustomerDAO import TransferPoints,NextScreeningCustomers
from src.MovieDAO import TotalMovieTickets

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

def Other():
    running = True
    while running:
        options = ["Převést body","Výpis zákazníků na nejbližší promítání","Celkový počet lístků na film","Ukončit"]
        print("Vyberte kterou akci chcete provést")
        showoptions(options)
        choice = input("Vybírám si: ")
        match choice:
            case "Vložit" | "1":
                from_id = int(input("Id zakaznika odkud se odeštou body: "))
                to_id = int(input("Id zakaznika komu se přičtou body: "))
                ammount = float(input("Množstvý bodů který se převedou: "))
                TransferPoints(from_id,to_id,ammount)
            case "Výpis zákazníků na nejbližší promítání" | "2":
                NextScreeningCustomers()
            case "Celkový počet lístků na film" | "3":
                TotalMovieTickets()
            case "Ukončit" | "4":
                running = False
            case _:
                print("Špatná volba")
        print("")