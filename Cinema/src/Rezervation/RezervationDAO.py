from src.DatabaseSingleton import *
from src.Rezervation.Rezervation import Rezervation
# import traceback

class RezervationDAO:

    def __init__(self,table_application):
        self.table_application = table_application

    def Save(self,r):
        sql = "call InsertRezervation (%s, %s, %s, %s);"
        val = [r.Customer_id, r.Screening_id, r.Date, r.Ticket_amount]
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

    def Update(self,r):
        sql = "call UpdateRezervation(%s, %s, %s, %s, %s);"
        val = [r.id, r.Customer_id, r.Screening_id, r.Date, r.Ticket_amount]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute("START TRANSACTION;")
            cursor.execute(sql, val)   
        except Exception as e:
            print(e)
            # print(traceback.format_exc())
            cursor.execute("ROLLBACK;")
        else:
            cursor.execute("COMMIT;")    
        finally:
            DatabaseSingleton.close_conn()

    def Delete(self,id):
        sql = "DELETE FROM Rezervation WHERE id = %s;"
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
        sql = "SELECT * FROM Rezervation;"
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
                r = Rezervation(i[1], i[2], i[3], i[4], i[5], i[0])
                list.append(r)        
        finally:
            DatabaseSingleton.close_conn()
            if(len(list)>0):
                return list

    def Load(self,data):
        with open("./Cinema/data.json",encoding="utf-8") as f:
            data = json.load(f)
            data = data["Rezervation"]
            list = []
            for i in data:
                r = Rezervation(i["Customer_id"], i["Screening_id"], i["Date"], i["Ticket_ammount"], i["Total_price"])
                list.append(r)
            return list
