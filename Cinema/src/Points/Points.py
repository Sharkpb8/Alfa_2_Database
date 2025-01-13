# from src.Customer.CustomerDAO import TransferPoints
# from src.LoyaltyPointsDAO import Transaction_by_id

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

# def PointsOptions():
#     running = True
#     while running:
#         options = ["Převést body","Výpis transakcí bodů","Ukončit"]
#         print("Vyberte kterou akci chcete provést")
#         showoptions(options)
#         choice = input("Vybírám si: ")
#         match choice:
#             case "Převést body" | "1":
#                 from_id = int(input("Id zakaznika odkud se odeštou body: "))
#                 to_id = int(input("Id zakaznika komu se přičtou body: "))
#                 ammount = float(input("Množstvý bodů který se převedou: "))
#                 TransferPoints(from_id,to_id,ammount)
#             case "Výpis transakcí bodů" | "2":
#                 id = int(input("id zakazníka u koho chcete vypsat transakce bodů: "))
#                 Transaction_by_id(id)
#             case "Ukončit" | "3":
#                 running = False
#             case _:
#                 print("Špatná volba")
#         print("")