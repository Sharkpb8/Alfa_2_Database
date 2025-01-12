from src.DatabaseSingleton import *
import traceback

def Save(Genre_id, Name, Length, Price, Premiere_date):
    sql = "INSERT INTO Movie(Genre_id, Name, Lenght, Price, Premiere_date)VALUES (%s, %s, %s, %s, %s);"
    val = [Genre_id, Name, Length, Price, Premiere_date]
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

def Update(id, Genre_id, Name, Length, Price, Premiere_date):
    sql = "UPDATE Movie SET Genre_id = %s, Name = %s, Lenght = %s, Price = %s, Premiere_date = %sWHERE id = %s;"
    val = [Genre_id, Name, Length, Price, Premiere_date, id]
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
    sql = "DELETE FROM Movie WHERE id = %s;"
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
    sql = "SELECT * FROM Movie;"
    conn = DatabaseSingleton()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        myresult = cursor.fetchall()
    except Exception as e:
        print(e)
    else:
        for i in myresult:
            print(f"ID: {i[0]}, Žánr ID: {i[1]}, Jméno: {i[2]}, Délka: {i[3]} minut, Cena: {i[4]} Kč, Premiéra: {i[5]}")
    finally:
        DatabaseSingleton.close_conn()