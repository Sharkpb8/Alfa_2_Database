from src.DatabaseSingleton import *

class PointDAO:

    def __init__(self,table_application):
        self.table_application = table_application

    def TransferPoints(self,from_id,to_id,ammount):
        sql = "call TransferPoints(%s,%s,%s)"
        val = [from_id, to_id, ammount]
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

    def Transaction_by_id(self,id):
        sql = "select id,ammount,description from Points where Customer_id = %s"
        val = [id]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute(sql,val)
            myresult = cursor.fetchall()
        except Exception as e:
            print(e)
        else:
            for i in myresult:
                print(f"id: {i[0]}, množsvý: {i[1]}, popis: {i[2]}")
        finally:
            DatabaseSingleton.close_conn()
    
    def Read(self):
        sql = "select * from Points"
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
                print(f"id: {i[0]}, id zákazníka: {i[1]}, množstvý {i[2]}, popis: {i[3]}")
        finally:
            DatabaseSingleton.close_conn()