from src.DatabaseSingleton import *

def Save(Customer_id, Screening_id, Date, Ticket_amount):
    sql = "call InsertRezervation (%s, %s, %s, %s);"
    val = [Customer_id, Screening_id, Date, Ticket_amount]
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

def Update(id, Customer_id, Screening_id, Date, Ticket_amount):
    sql = "call UpdateRezervation(%s, %s, %s, %s, %s);"
    val = [id, Customer_id, Screening_id, Date, Ticket_amount]
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

def Read():
    sql = "SELECT * FROM Rezervation;"
    conn = DatabaseSingleton()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        myresult = cursor.fetchall()
    except Exception as e:
        print(e)
    else:
        for i in myresult:
            print(f"ID: {i[0]}, Zákazník ID: {i[1]}, Promítání ID: {i[2]}, Datum: {i[3]}, Počet lístků: {i[4]}, Celková cena: {i[5]}")
    finally:
        DatabaseSingleton.close_conn()

def LoadCustomer(data):
    with open("./Cinema/data.json",encoding="utf-8") as f:
        data = json.load(f)
        data = data["Rezervation"]
        for i in data:
            sql = "insert into Rezervation(Customer_id,Screening_id,Date,Ticket_ammount,Total_price) values(%s,%s,%s,%s,%s)"
            val = [i["Customer_id"], i["Screening_id"], i["Date"], i["Ticket_ammount"], i["Total_price"]]
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
