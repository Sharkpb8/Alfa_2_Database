from src.DatabaseSingleton import *
from src.Genre.Genre import Genre

class GenreDAO():

    def __init__(self,table_application):
        self.table_application = table_application

    def Save(self,g):
        sql = f"insert into Genre(Name) values(%s);"
        val = [g.Name]
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

    def Update(self,g):
        sql = f"update Genre set Name = %s where id = %s;"
        val = [g.Name,g.id]
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
            list = []
            for i in myresult:
                g = Genre(i[1], i[0])
                list.append(g)
        finally:
            DatabaseSingleton.close_conn()
            if(len(list)>0):
                return list
        
    def Load(self):
        with open("./Cinema/data.json",encoding="utf-8") as f:
            data = json.load(f)
            data = data["Genre"]
            for i in data:
                self.Save(i["Name"])