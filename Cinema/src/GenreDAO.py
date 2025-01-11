from src.DatabaseSingleton import *

def Save(Name):
    sql = f"insert into Genre(Name) values(%s);"
    val = (Name)
    conn = DatabaseSingleton
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

def Update(id,Name):
    sql = f"update Genre set Name = %s where id = %s;"
    val = (Name,id)
    conn = DatabaseSingleton
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
    sql = f"delete Genre where id = %s;"
    val = (id)
    conn = DatabaseSingleton
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
    sql = f"select * Genre;"
    val = ()
    conn = DatabaseSingleton
    cursor = conn.cursor()
    try:
        cursor.execute(sql,val)
        myresult = cursor.fetchall()
    except Exception as e:
        print(e)
    else:
        for i in myresult:
            print(f"ID: {i[0]}, Nazev {i[1]}")
    finally:
        DatabaseSingleton.close_conn()