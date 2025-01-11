from src.DatabaseSingleton import *

def Save(Genreid,name,Lenght,Price,Premiere_date):
    sql = f"insert into Movie(id, Genre_id, Name, Lenght, Price, Premiere_date) values(%s,%s,%s,%s,%s,%s);"
    val = [Genreid,name,Lenght,Price,Premiere_date]
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

def Update(id,Genreid,name,Lenght,Price,Premiere_date):
    sql = f"update Movie set Genre_id = %s, Name = %s, Lenght=%s, Price=%s,Premiere_date=%s  where id = %s;"
    val = [Genreid,name,Lenght,Price,Premiere_date,id]
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

def Delete(id):
    sql = f"delete Movie where id = %s;"
    val = [id]
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

def Read():
    sql = f"select * from MovieJoin;"
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
            print(f"ID: {i[0]}, Film: {i[1]}, Žánr: {i[2]}, Délka: {i[3]}, Cena: {i[4]}, Den premiery {i[5]}")
    finally:
        DatabaseSingleton.close_conn()