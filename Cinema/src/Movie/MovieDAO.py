from src.DatabaseSingleton import *
from src.Movie.Movie import Movie

class MovieDAO:

    def __init__(self,table_application):
        self.table_application = table_application

    def Save(self,m):
        sql = "INSERT INTO Movie(Genre_id, Name, Lenght, Price, Premiere_date)VALUES (%s, %s, %s, %s, %s);"
        val = [m.Genre_id, m.Name, m.Length, m.Price, m.Premiere_date]
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

    def Update(self,m):
        sql = "UPDATE Movie SET Genre_id = %s, Name = %s, Lenght = %s, Price = %s, Premiere_date = %sWHERE id = %s;"
        val = [m.Genre_id, m.Name, m.Length, m.Price, m.Premiere_date, m.id]
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
        sql = "DELETE FROM Movie WHERE id = %s;"
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
        sql = "SELECT * FROM Movie;"
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            myresult = cursor.fetchall()
        except Exception as e:
            print(e)
        else:
            list = []
            for i in myresult:
                m = Movie(i[1], i[2], i[3], i[4], i[5], i[0])
                list.append(m)        
        finally:
            DatabaseSingleton.close_conn()
            if(len(list)>0):
                return list

    def Load(self,data):
        with open("./Cinema/data.json",encoding="utf-8") as f:
            data = json.load(f)
            data = data["Movie"]
            for i in data:
                self.Save(i["Genre_id"],i["Name"],i["Length"],i["Length"],i["Premiere_date"])