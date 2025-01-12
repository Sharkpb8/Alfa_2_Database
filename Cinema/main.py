import ast
from src.Genre import GenreCRUD
from src.Movie import MovieCRUD
from src.Hall import HallCRUD
from src.Screening import ScreeningCRUD
from src.Customer import CustomerCRUD
from src.Rezervation import ReservationCRUD
from src.Points import PointsOptions
from src.Report import ReportOptions

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
        options = ["Film","Žánr","Sál","Promítání","Zákazník","Rezervace","Body","Report","Ukončit"]
        print("Zadejte název tabulky, se kterou chcete pracovat.")
        showoptions(options)
        choice = input("Vybírám si: ")
        match choice:
            case "Film" | "1":
                MovieCRUD()
            case "Žánr" | "2":
                GenreCRUD()
            case "Sál" | "3":
                HallCRUD()
            case "Promítání" | "4":
                ScreeningCRUD()
            case "Zákazník" | "5":
                CustomerCRUD()
            case "Rezervace" | "6":
                ReservationCRUD()
            case "Body" | "7":
                PointsOptions()
            case "Report" | "8":
                ReportOptions()
            case "Ukončit" | "9":
                running = False
            case _:
                print("Špatná volba")
        print("")

if __name__ == "__main__":
    Run()