# from src.CustomerDAO import NextScreeningCustomers
# from src.MovieDAO import TotalMovieTickets

# def showoptions(list):
#     """
#     Displays the items in a list with numbered options.

#     :param list: A list of items to display as options.
#     :type list: list
#     """
#     count = 1
#     for i in list:
#         print(f"{count}. {i}")
#         count += 1

# def ReportOptions():
#     running = True
#     while running:
#         options = ["Výpis zákazníků na nejbližší promítání","Celkový počet lístků na film","Ukončit"]
#         print("Vyberte kterou akci chcete provést")
#         showoptions(options)
#         choice = input("Vybírám si: ")
#         match choice:
#             case "Výpis zákazníků na nejbližší promítání" | "1":
#                 NextScreeningCustomers()
#             case "Celkový počet lístků na film" | "1":
#                 TotalMovieTickets()
#             case "Ukončit" | "3":
#                 running = False
#             case _:
#                 print("Špatná volba")
#         print("")