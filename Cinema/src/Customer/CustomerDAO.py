from src.DatabaseSingleton import *
from src.Customer.Customer import Customer
import traceback

class CustomerDAO:

    def __init__(self,table_application):
        self.table_application = table_application

    def Save(self,c):
        sql = "call CreateCustomer (%s, %s, %s, %s,%s);"
        val = [c.Name, c.Last_name, c.Loyalty_program, c.Loyalty_points,c.Registry_date]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute("START TRANSACTION;")
            cursor.execute(sql, val)
            cursor.execute("SELECT max(id) from Customer;")
            id = cursor.fetchone()[0]
            result = self.Get_by_id(id)
            result = result[0]
            self.table_application.print_messageCustomer(f"Vkládané data: Jméno: {result[1]}, Příjmení: {result[2]}, Člen věrnostního programu: {'Ano' if result[3] else 'Ne'}, Body: {result[4]}, Registrace: {result[5]}")
            if(not self.table_application.confirmationCustomer()):
                raise Exception
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            cursor.execute("ROLLBACK;")
        else:
            cursor.execute("COMMIT;")
        finally:
            DatabaseSingleton.close_conn()


    def Update(self,c):
        sql = "UPDATE Customer SET Name = %s, Last_name = %s, Loyalty_program = %s, Loyalty_points = %s WHERE id = %s;"
        val = [c.Name, c.Last_name, c.Loyalty_program, c.Loyalty_points, c.id]
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
        sql = "DELETE FROM Customer WHERE id = %s;"
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
        sql = "SELECT * FROM Customer;"
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
                c = Customer(i[1], i[2], i[3], i[4], i[5], i[0])
                list.append(c)
        finally:
            DatabaseSingleton.close_conn()
            if(len(list)>0):
                return list

    def Get_Customer_point(self,id):
        sql = "select Loyalty_points from Customer where id = %s"
        val = [id]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute(sql,val)
            myresult = cursor.fetchall()
        except Exception as e:
            print(e)
        else:
            return myresult[0][0]
        finally:
            DatabaseSingleton.close_conn()

    def Load(self,data):
        with open("./Cinema/data.json",encoding="utf-8") as f:
            data = json.load(f)
            data = data["Customer"]
            for i in data:
                self.Save(i["Name"],i["Last_name"],i["Loyalty_program"],i["Loyalty_points"])
    
    def Get_by_id(self,id):
        sql = "SELECT * FROM Customer where id = %s;"
        val = [id]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute(sql,val)
            myresult = cursor.fetchall()
        except Exception as e:
            print(e)
        else:
            return myresult
        finally:
            DatabaseSingleton.close_conn(conn)