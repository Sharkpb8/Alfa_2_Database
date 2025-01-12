from src.Genre import GenreCRUD
from src.Movie import MovieCRUD
from src.Hall import HallCRUD
from src.Screening import ScreeningCRUD
from src.Customer import CustomerCRUD
from src.Rezervation import ReservationCRUD

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
        options = ["Film","Žánr","Sál","Promítání","Zákazník","Rezervace","Jiný","Ukončit"]
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
            case "Jiný" | "7":
                print("Není implementovaný")
            case "Ukončit" | "8":
                running = False
            case _:
                print("Špatná volba")
        print("")

if __name__ == "__main__":
    Run()