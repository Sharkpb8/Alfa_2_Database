from src.DatabaseSingleton import *

class ReportDAO():

    def __init__(self,table_application):
        self.table_application = table_application

    def TotalMovieTickets(self):
        sql = "SELECT * FROM TotalMovieTickets;"
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            myresult = cursor.fetchall()
        except Exception as e:
            print(e)
        else:
            for i in myresult:
                print(f"Jméno filmu: {i[0]}, Celkový počet lístků: {i[1]}")
        finally:
            DatabaseSingleton.close_conn()
    
    def NextScreeningCustomers(self):
        sql = "SELECT * FROM NextScreeningCustomers;"
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            myresult = cursor.fetchall()
        except Exception as e:
            print(e)
        else:
            for i in myresult:
                print(f"Jméno: {i[0]}, Příjmení: {i[1]}, Datum nákupu: {i[2]}, Množstvý vstupenek: {i[3]}, Celková cena: {i[4]}")
        finally:
            DatabaseSingleton.close_conn()
    
    def All_rezervations(self):
        sql = "SELECT * FROM All_rezervations;"
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            myresult = cursor.fetchall()
        except Exception as e:
            print(e)
        else:
            for i in myresult:
                print(f"Jméno: {i[0]}, Příjmení: {i[1]}, Datum rezervace: {i[2]}, Množstvý vstupenek: {i[3]}, Jméno filmu: {i[4]}, Jméno sálu: {i[5]}, typ sálu: {i[6]}")
        finally:
            DatabaseSingleton.close_conn()

    def MovieSummary(self):
        sql = "SELECT * FROM MovieSummary;"
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            myresult = cursor.fetchall()
        except Exception as e:
            print(e)
        else:
            for i in myresult:
                print(f"Název filmu: {i[0]}, Celkový počet rezervací: {i[1]}, Box Office: {i[2]}, Průměrný množstvý vstupenek: {i[3]}, Průměrná cena obědnávky: {i[4]}")
        finally:
            DatabaseSingleton.close_conn()