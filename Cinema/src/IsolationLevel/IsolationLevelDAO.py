from src.DatabaseSingleton import *

class IsolationLevelDAO():

    def __init__(self,table_application):
        self.table_application = table_application

    def Set(self,Level):
        sql = "idk"
        val = [Level]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute("START TRANSACTION;")
            cursor.execute(sql,val)
        except Exception as e:
            cursor.execute("ROLLBACK;")
        else:
            cursor.execute("COMMIT;")
        finally:
            DatabaseSingleton.close_conn()

    def Read(self):
        sql = "SELECT @@transaction_isolation;"
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            myresult = cursor.fetchall()
        except Exception as e:
            print(e)
        else:
            for i in myresult:
                print(f"Aktuální izolační level: {i[0]}")
        finally:
            DatabaseSingleton.close_conn()