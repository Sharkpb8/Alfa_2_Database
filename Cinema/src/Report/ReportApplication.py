from src.Report.ReportDAO import ReportDAO

class ReportApplication():

    def __init__(self,table_user_interface):
        self.table_user_interface = table_user_interface
        self.table_DAO = ReportDAO(self)

    def TotalMovieTicketsReport(self):
        self.table_user_interface.interface.print_line()
        self.table_DAO.TotalMovieTickets()

    def NextScreeningCustomersReport(self):
        self.table_user_interface.interface.print_line()
        self.table_DAO.NextScreeningCustomers()
