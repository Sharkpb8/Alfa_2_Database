from src.DatabaseSingleton import *

class PointDAO:

    def __init__(self,table_application):
        self.table_application = table_application

    def Save(self,Customer_id,ammount,description):
        sql = "insert into Loyalty_points_transactions(Customer_id,ammount,description) values(%s,%s,%s);"
        val = [Customer_id,ammount,description]
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
        sql = "select id,ammount,description from Loyalty_points_transactions where Customer_id = %s"
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
        sql = "select * from Loyalty_points_transactions"
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

    def Load(self):
        with open("./Cinema/data.json",encoding="utf-8") as f:
            data = json.load(f)
            data = data["Points"]
            for i in data:
                self.Save(i["Customer_id"],i["ammount"],i["description"])