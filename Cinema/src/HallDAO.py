from src.DatabaseSingleton import *

def Save(Name, Type):
    sql = "INSERT INTO Hall(Name, Type) VALUES (%s, %s);"
    val = [Name, Type]
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

def Update(id, Name, Type):
    sql = "UPDATE Hall SET Name = %s, Type = %s WHERE id = %s;"
    val = [Name, Type, id]
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
    sql = "DELETE FROM Hall WHERE id = %s;"
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
    sql = "SELECT * FROM Hall;"
    conn = DatabaseSingleton()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        myresult = cursor.fetchall()
    except Exception as e:
        print(e)
    else:
        for i in myresult:
            print(f"ID: {i[0]}, Jméno: {i[1]}, Typ: {i[2]}")
    finally:
        DatabaseSingleton.close_conn()

def LoadHall(data):
    with open("./Cinema/data.json",encoding="utf-8") as f:
        data = json.load(f)
        data = data["Hall"]
        for i in data:
            Save(i["Name"],i["Type"])