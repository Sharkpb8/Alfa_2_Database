from src.Interface import UserInterface
from src.Genre.Genre import GenreInterface

if __name__ == "__main__":
    ui = UserInterface()
    ui.table_user_interface.append(GenreInterface(ui))
    ui.table_user_interface.append(GenreInterface(ui))
    ui.table_user_interface.append(GenreInterface(ui))
    ui.table_user_interface.append(GenreInterface(ui))
    ui.table_user_interface.append(GenreInterface(ui))
    ui.table_user_interface.append(GenreInterface(ui))
    ui.run()