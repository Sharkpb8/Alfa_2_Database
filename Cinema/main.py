from src.JsonLoad import load
import ast

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

def convert_input(value):
    """
    Tries to convert a string input into a Python literal (e.g., int, float, list, etc.).
    If conversion fails, returns the original string.

    :param value: The input string to be evaluated.
    :type value: str
    :return: The converted value or the original string if conversion fails.
    :rtype: any
    """
    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value


def Run():
    running = True
    while running:
        options = ["Načís ze souboru","Reporty","Ukončit"]
        print("Zadejte název tabulky, se kterou chcete pracovat.")
        showoptions(options)
        choice = input("Vybírám si: ")
        match choice:
            case "Načís ze souboru" | "1":
                options = ["Film","Žánr","Sál","Promítání","Zákazník","Rezervace"]
                showoptions(options)
                table = convert_input(input("Vybírám si: "))
                if(table in options):
                    load(table)
                elif(table>=1 and table<= len(options)):
                    load(options[table-1])
            case "Reporty" | "2":
                
            case "Ukončit" | "3":
                running = False
            case _:
                print("Špatná volba")
        print("")

if __name__ == "__main__":
    Run()