import mysql.connector
import json

class DatabaseSingleton:
    conn = None
    isolation_level = "REPEATABLE READ"

    def __new__(cls):
        if not cls.conn:
            cls.new_conn()
        cls.set_session_isolation_level()
        return cls.conn
    
    @classmethod
    def new_conn(cls):
        connection = mysql.connector.connect(
        host=cls.readconfig("host"),
        port=cls.readconfig("port"),
        user=cls.readconfig("user"),
        password=cls.readconfig("password"),
        database=cls.readconfig("database"),
        )
        cls.conn = connection
    
    @classmethod
    def close_conn(cls):
        if(cls.conn):
            cls.conn.close()
            cls.conn = None

    @classmethod
    def readconfig(cls,key):
        with open("./Cinema/appconfig.json","r") as f:
            config = json.load(f)
            return config["database"][key]
    
    @classmethod
    def set_session_isolation_level(cls):
        sql = f"SET SESSION TRANSACTION ISOLATION LEVEL {cls.isolation_level};"
        cursor = cls.conn.cursor()
        cursor.execute(sql)
    
    @classmethod
    def set_isolation_level(cls,new_level):
        cls.isolation_level = new_level


# conn = DatabaseSingleton.new_conn()
# DatabaseSingleton.close_conn()
# print("Konec")