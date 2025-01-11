from src.DatabaseSingleton import *

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

def Save(table_name):
    cursor = DatabaseSingleton()
    #just do DAO like in C#

def execute_crud(table_name):
    running = True
    while running:
        options = ["Vložit","Upravit","Smazat","Číst","Ukončit"]
        print("Zadejte název tabulky, se kterou chcete pracovat.")
        showoptions(options)
        choice = input("Vybírám si: ")
        match choice:
            case "Vložit" | "1":
                execute_crud("Movie")
            case "Upravit" | "2":
                print("Není implementovaný")
            case "Smazat" | "3":
                print("Není implementovaný")
            case "Číst" | "4":
                print("Není implementovaný")
            case "Ukončit" | "8":
                running = False
            case _:
                print("Špatná volba")
        print("")

def Run():
    running = True
    while running:
        options = ["Film","Žánr","Sál","Promítání","Zákazník","Rezervace","Jiný","Ukončit"]
        print("Zadejte název tabulky, se kterou chcete pracovat.")
        showoptions(options)
        choice = input("Vybírám si: ")
        match choice:
            case "Film" | "1":
                execute_crud("Movie")
            case "Žánr" | "2":
                execute_crud("Genre")
            case "Sál" | "3":
                execute_crud("Hall")
            case "Promítání" | "4":
                execute_crud("Screening")
            case "Zákazník" | "5":
                execute_crud("Customer")
            case "Rezervace" | "6":
                execute_crud("Rezervation")
            case "Jiný" | "7":
                print("Není implementovaný")
            case "Ukončit" | "8":
                running = False
            case _:
                print("Špatná volba")
        print("")

if __name__ == "__main__":
    Run()