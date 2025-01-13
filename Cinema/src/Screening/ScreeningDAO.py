from src.DatabaseSingleton import *

class ScreeningDAO:

    def __init__(self,table_application):
        self.table_application = table_application

    def Save(self,Movie_id, Hall_id, Date):
        sql = "INSERT INTO Screening(Movie_id, Hall_id, Date) VALUES (%s, %s, %s);"
        val = [Movie_id, Hall_id, Date]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute("START TRANSACTION;")
            cursor.execute(sql, val)
        except Exception as e:
            print(e)
            cursor.execute("ROLLBACK;")
        else:
            cursor.execute("COMMIT;")
        finally:
            DatabaseSingleton.close_conn()

    def Update(self,id, Movie_id, Hall_id, Date):
        sql = "UPDATE Screening SET Movie_id = %s, Hall_id = %s, Date = %s WHERE id = %s;"
        val = [Movie_id, Hall_id, Date, id]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute("START TRANSACTION;")
            cursor.execute(sql, val)
        except Exception as e:
            print(e)
            cursor.execute("ROLLBACK;")
        else:
            cursor.execute("COMMIT;")
        finally:
            DatabaseSingleton.close_conn()

    def Delete(self,id):
        sql = "DELETE FROM Screening WHERE id = %s;"
        val = [id]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute("START TRANSACTION;")
            cursor.execute(sql, val)
        except Exception as e:
            print(e)
            cursor.execute("ROLLBACK;")
        else:
            cursor.execute("COMMIT;")
        finally:
            DatabaseSingleton.close_conn()

    def Read(self):
        sql = "select id,Movie_id,Hall_id,DATE_FORMAT(Date, '%Y-%m-%d %H:%i') from Screening;"
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            myresult = cursor.fetchall()
        except Exception as e:
            print(e)
        else:
            for i in myresult:
                print(f"ID: {i[0]}, Film ID: {i[1]}, Sál ID: {i[2]}, Datum: {i[3]}")
        finally:
            DatabaseSingleton.close_conn()

    def Load(self,data):
        with open("./Cinema/data.json",encoding="utf-8") as f:
            data = json.load(f)
            data = data["Screening"]
            for i in data:
                self.Save(i["Movie_id"],i["Hall_id"],i["Date"])