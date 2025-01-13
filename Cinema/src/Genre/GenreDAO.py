from src.DatabaseSingleton import *

class GenreDAO():

    def __init__(self,table_application):
        self.table_application = table_application

    def Save(self,Name):
        sql = f"insert into Genre(Name) values(%s);"
        val = [Name]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute("start transaction;")
            cursor.execute(sql,val)
        except Exception as e:
            print(e)
            cursor.execute("ROLLBACK;")
        else:
            cursor.execute("COMMIT;")
        finally:
            DatabaseSingleton.close_conn()

    def Update(self,id,Name):
        sql = f"update Genre set Name = %s where id = %s;"
        val = [Name,id]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute("start transaction;")
            cursor.execute(sql,val)
        except Exception as e:
            print(e)
            cursor.execute("ROLLBACK;")
        else:
            cursor.execute("COMMIT;")
        finally:
            DatabaseSingleton.close_conn()

    def Delete(self,id):
        sql = f"delete from Genre where id = %s;"
        val = [id]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute("start transaction;")
            cursor.execute(sql,val)
        except Exception as e:
            print(e)
            cursor.execute("ROLLBACK;")
        else:
            cursor.execute("COMMIT;")
        finally:
            DatabaseSingleton.close_conn()

    def Read(self):
        sql = f"select * from Genre order by id;"
        val = []
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute(sql,val)
            myresult = cursor.fetchall()
        except Exception as e:
            print(e)
        else:
            for i in myresult:
                print(f"ID: {i[0]}, Nazev {i[1]}")
        finally:
            DatabaseSingleton.close_conn()
        
    def Load(self):
        with open("./Cinema/data.json",encoding="utf-8") as f:
            data = json.load(f)
            data = data["Genre"]
            for i in data:
                self.Save(i["Name"])