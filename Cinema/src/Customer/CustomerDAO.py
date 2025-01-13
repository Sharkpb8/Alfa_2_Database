from src.DatabaseSingleton import *

class CustomerDAO:

    def __init__(self,table_application):
        self.table_application = table_application

    def Save(self,Name, Last_name, Loyalty_program, Loyalty_points):
        sql = "call CreateCustomer (%s, %s, %s, %s);"
        val = [Name, Last_name, Loyalty_program, Loyalty_points]
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

    def Update(self,id, Name, Last_name, Loyalty_program, Loyalty_points):
        sql = "UPDATE Customer SET Name = %s, Last_name = %s, Loyalty_program = %s, Loyalty_points = %s WHERE id = %s;"
        val = [Name, Last_name, Loyalty_program, Loyalty_points, id]
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
            for i in myresult:
                print(f"ID: {i[0]}, Jméno: {i[1]}, Příjmení: {i[2]}, Člen věrnostního programu: {'Ano' if i[3] else 'Ne'}, Body: {i[4]}, Registrace: {i[5]}")
        finally:
            DatabaseSingleton.close_conn()

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

    def NextScreeningCustomers(self):
        sql = "SELECT * FROM NextScreeningCustomers;"
        conn = DatabaseSingleton()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            myresult = cursor.fetchall()
        except Exception as e:
            print(e)
        else:
            for i in myresult:
                print(f"Jméno: {i[0]}, Příjmení: {i[1]}, Datum nákupu: {i[2]}, Množstvý vstupenek: {i[3]}, Celková cena: {i[4]}")
        finally:
            DatabaseSingleton.close_conn()