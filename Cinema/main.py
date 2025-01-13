from src.Interface import UserInterface
from src.Genre.Genre import GenreInterface
from src.Movie.Movie import MovieInterface
from src.Hall.Hall import HallInterface
from src.Screening.Screening import ScreeningInterface
from src.Customer.Customer import CustomerInterface
from src.Rezervation.Rezervation import RezervationInterface
from src.Point.Point import PointInterface
from src.Report.Report import ReportInterface

if __name__ == "__main__":
    ui = UserInterface()
    ui.table_user_interface.append(MovieInterface(ui))
    ui.table_user_interface.append(GenreInterface(ui))
    ui.table_user_interface.append(HallInterface(ui))
    ui.table_user_interface.append(ScreeningInterface(ui))
    ui.table_user_interface.append(CustomerInterface(ui))
    ui.table_user_interface.append(RezervationInterface(ui))
    ui.table_user_interface.append(PointInterface(ui))
    ui.table_user_interface.append(ReportInterface(ui))
    ui.run()