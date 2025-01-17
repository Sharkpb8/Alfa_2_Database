from src.DatabaseSingleton import *
from src.Customer.Customer import Customer
import multiprocessing
import traceback
import time

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
        except Exception as e:
            print(e)
            # print(traceback.format_exc())
            cursor.execute("ROLLBACK;")
        else:
            cursor.execute("COMMIT;")
        finally:
            DatabaseSingleton.close_conn()


    def Update(self,c,phenomenon = 1):
        sql = "UPDATE Customer SET Name = %s, Last_name = %s, Loyalty_program = %s, Loyalty_points = %s WHERE id = %s;"
        val = [c.Name, c.Last_name, c.Loyalty_program, c.Loyalty_points, c.id]
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            if(phenomenon == 1 or phenomenon == 2):
                cursor.execute("START TRANSACTION;")
                cursor.execute(sql, val)
                if(DatabaseSingleton.dirtyreads() and phenomenon == 2):
                    result = self.Get_by_id(c.id)
                    result = result[0]
                    self.table_application.print_messageCustomer(f"Upravovaná data: Jméno: {result[1]}, Příjmení: {result[2]}, Člen věrnostního programu: {'Ano' if result[3] else 'Ne'}, Body: {result[4]}, Registrace: {result[5]}")
                    if(not self.table_application.confirmationCustomer()):
                        raise Exception
            elif(phenomenon == 3):
                sql = "insert into temp_customer select * from Customer where id =%s;"
                val = [c.id]
                cursor.execute("START TRANSACTION;")
                cursor.execute("delete from temp_customer")
                cursor.execute(sql,val)
                cursor.execute("COMMIT;")
                DatabaseSingleton.close_conn(conn)
                self.dirtywrites(c)
                conn = DatabaseSingleton()
                cursor = conn.cursor()
                cursor.execute("call UpdateCustomer (%s)",val)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
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

    def Load(self):
        with open("./Cinema/data.json",encoding="utf-8") as f:
            data = json.load(f)
            data = data["Customer"]
            list = []
            for i in data:
                c = Customer(i["Name"],i["Last_name"],i["Loyalty_program"],i["Loyalty_points"],i["Registry_date"])
                list.append(c)
            return list
    
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
    
    def _transaction_a(self,c):
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        cursor.execute("START TRANSACTION;")
        sql = "UPDATE temp_customer SET Name = %s, Last_name = %s, Loyalty_program = %s, Loyalty_points = %s, Registry_date = %s WHERE id = %s"
        val = [c.Name, c.Last_name, c.Loyalty_program, c.Loyalty_points, c.Registry_date, c.id]
        cursor.execute(sql,val)
        cursor.execute("COMMIT;")
        DatabaseSingleton.close_conn(conn)

    def _transaction_b(self,id):
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        cursor.execute("START TRANSACTION;")
        sql = "UPDATE temp_customer SET Name = 'dirty', Last_name = 'write', Loyalty_program = 0, Loyalty_points = 666, Registry_date = '1900-01-01' WHERE id = %s"
        val = [id]
        cursor.execute(sql,val)
        cursor.execute("COMMIT;")
        DatabaseSingleton.close_conn(conn)


    def dirtywrites(self,c):
        process_a = multiprocessing.Process(target=self._transaction_a,args=(c,))
        process_b = multiprocessing.Process(target=self._transaction_b,args=(c.id,))

        process_a.start()
        time.sleep(0.1)
        process_b.start()

        process_a.join()
        process_b.join()