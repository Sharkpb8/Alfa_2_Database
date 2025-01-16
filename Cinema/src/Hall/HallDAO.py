from src.DatabaseSingleton import *
from src.Hall.Hall import Hall

class HallDAO:

    def __init__(self,table_application):
        self.table_application = table_application

    def Save(self,h):
        sql = "INSERT INTO Hall(Name, Type) VALUES (%s, %s);"
        val = [h.Name, h.Type]
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

    def Update(self,h):
        sql = "UPDATE Hall SET Name = %s, Type = %s WHERE id = %s;"
        val = [h.Name, h.Type, h.id]
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
        sql = "DELETE FROM Hall WHERE id = %s;"
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
        sql = "SELECT * FROM Hall;"
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
                h = Hall(i[1], i[2], i[0])
                list.append(h)
        finally:
            DatabaseSingleton.close_conn()
            if(len(list)>0):
                return list

    def Load(self,data):
        with open("./Cinema/data.json",encoding="utf-8") as f:
            data = json.load(f)
            data = data["Hall"]
            for i in data:
                self.Save(i["Name"],i["Type"])