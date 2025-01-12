from src.DatabaseSingleton import *

def Save(Name, Last_name, Loyalty_program, Loyalty_points):
    sql = "INSERT INTO Customer(Name, Last_name, Loyalty_program, Loyalty_points) VALUES (%s, %s, %s, %s);"
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

def Update(id, Name, Last_name, Loyalty_program, Loyalty_points):
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

def Delete(id):
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

def Read():
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

def Get_Customer_point(id):
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

def LoadCustomer(data):
    with open("./Cinema/data.json",encoding="utf-8") as f:
        data = json.load(f)
        data = data["Customer"]
        for i in data:
            Save(i["Name"],i["Last_name"],i["Loyalty_program"],i["Loyalty_points"])