import mysql.connector
from mysql.connector import pooling
import json

class DatabaseSingleton:
    conn = None
    isolation_level = "REPEATABLE READ"
    active_connections = []

    def __new__(cls):
        if not cls.conn:
            cls.new_conn()
        connection = cls.conn.get_connection()
        cls.set_session_isolation_level(connection)
        cls.active_connections.append(connection)
        return connection
    
    @classmethod
    def new_conn(cls):
        connection = pooling.MySQLConnectionPool(
        pool_name="Connection_pool",
        pool_size=2,
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
            for i in cls.active_connections:
                i.close()
            cls.conn = None

    @classmethod
    def readconfig(cls,key):
        with open("./Cinema/appconfig.json","r") as f:
            config = json.load(f)
            return config["database"][key]
    
    @classmethod
    def set_session_isolation_level(cls,connection):
        sql = f"SET SESSION TRANSACTION ISOLATION LEVEL {cls.isolation_level};"
        cursor = connection.cursor()
        cursor.execute(sql)
    
    @classmethod
    def set_isolation_level(cls,new_level):
        cls.isolation_level = new_level


# conn = DatabaseSingleton.new_conn()
# DatabaseSingleton.close_conn()
# print("Konec")