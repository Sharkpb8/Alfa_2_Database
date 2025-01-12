import json
from src.DatabaseSingleton import *

def SaveGenre(data):
    cursor = DatabaseSingleton().cursor()
    cursor.execute("start transaction;")
    try:
        for i in data:
            sql = f"insert into Genre(Name) values(%s);"
            val = [i["Name"]]
            cursor.execute(sql,val)
    except Exception as e:
        cursor.execute("ROLLBACK;")
    else:
        cursor.execute("COMMIT;")
    finally:
        DatabaseSingleton.close_conn()

def SaveMovie(data):
    cursor = DatabaseSingleton().cursor()
    cursor.execute("start transaction;")
    try:
        for i in data:
            sql = "insert into Movie(Genre_id, Name, Lenght, Price, Premiere_date) values(%s, %s, %s, %s, %s);"
            val = [i["Genre_id"], i["Name"], i["Lenght"], i["Price"], i["Premiere_date"]]
            cursor.execute(sql, val)
    except Exception as e:
        print(e)
        cursor.execute("ROLLBACK;")
    else:
        cursor.execute("COMMIT;")
    finally:
        DatabaseSingleton.close_conn()

def SaveHall(data):
    cursor = DatabaseSingleton().cursor()
    cursor.execute("start transaction;")
    try:
        for i in data:
            sql = "insert into Hall(Name, Type) values(%s, %s);"
            val = [i["Name"], i["Type"]]
            cursor.execute(sql, val)
    except Exception as e:
        print(e)
        cursor.execute("ROLLBACK;")
    else:
        cursor.execute("COMMIT;")
    finally:
        DatabaseSingleton.close_conn()

def SaveScreening(data):
    cursor = DatabaseSingleton().cursor()
    cursor.execute("start transaction;")
    try:
        for i in data:
            sql = "insert into Screening(Movie_id, Hall_id, Date) values(%s, %s, %s);"
            val = [i["Movie_id"], i["Hall_id"], i["Date"]]
            cursor.execute(sql, val)
    except Exception as e:
        print(e)
        cursor.execute("ROLLBACK;")
    else:
        cursor.execute("COMMIT;")
    finally:
        DatabaseSingleton.close_conn()

def SaveCustomer(data):
    cursor = DatabaseSingleton().cursor()
    cursor.execute("start transaction;")
    try:
        for i in data:
            sql = "insert into Customer(Name, Last_name, Loyalty_program, Loyalty_points, Registry_date) values(%s, %s, %s, %s, %s);"
            val = [i["Name"], i["Last_name"], i.get("Loyalty_program", 0), i.get("Loyalty_points", 0), i.get("Registry_date", None)]
            cursor.execute(sql, val)
    except Exception as e:
        print(e)
        cursor.execute("ROLLBACK;")
    else:
        cursor.execute("COMMIT;")
    finally:
        DatabaseSingleton.close_conn()

def SaveReservation(data):
    cursor = DatabaseSingleton().cursor()
    cursor.execute("start transaction;")
    try:
        for i in data:
            sql = "insert into Rezervation(Customer_id, Screening_id, Date, Ticket_ammount, Total_price) values(%s, %s, %s, %s, %s);"
            val = [i["Customer_id"], i["Screening_id"], i["Date"], i["Ticket_ammount"], i["Total_price"]]
            cursor.execute(sql, val)
    except Exception as e:
        print(e)
        cursor.execute("ROLLBACK;")
    else:
        cursor.execute("COMMIT;")
    finally:
        DatabaseSingleton.close_conn()


def load(table):
    with open("./Cinema/data.json",encoding="utf-8") as f:
        data = json.load(f)

        if table == "Genre":
            SaveGenre(data["Genre"])
        if table == "Movie":
            SaveMovie(data["Movie"])
        if table == "Hall":
            SaveHall(data["Hall"])
        if table == "Screening":
            SaveScreening(data["Screening"])
        if table == "Customer":
            SaveCustomer(data["Customer"])
        if table == "Rezervation":
            SaveReservation(data["Rezervation"])
