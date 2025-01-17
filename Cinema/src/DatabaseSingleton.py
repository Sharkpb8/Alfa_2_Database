import mysql.connector
from mysql.connector import pooling
import json

class DatabaseSingleton:
    conn = None
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
    def close_conn(cls,connection = None):
        if(cls.conn):
            if(connection):
                cls.active_connections.remove(connection)
                connection.close()
            else:
                for i in cls.active_connections:
                    cls.active_connections.remove(i)
                    i.close()
                cls.conn = None

    @classmethod
    def readconfig(cls,key):
        with open("./Cinema/appconfig.json","r") as f:
            config = json.load(f)
            return config["database"][key]
    
    @classmethod
    def set_session_isolation_level(cls,connection):
        sql = f"SET SESSION TRANSACTION ISOLATION LEVEL {cls.readisolationlevel()};"
        cursor = connection.cursor()
        cursor.execute(sql)
    
    @classmethod
    def set_isolation_level(cls,new_level):
        with open("./Cinema/config.json","w") as f:
            config = {"izolation_level":new_level}
            json.dump(config,f,indent=4)

    @classmethod
    def readisolationlevel(cls):
        with open("./Cinema/config.json","r") as f:
            config = json.load(f)
            return config["izolation_level"]
    
    @classmethod
    def dirtyreads(cls):
        if(cls.readisolationlevel() == "READ UNCOMMITTED"):
            return True
        else:
            return False


# conn = DatabaseSingleton.new_conn()
# DatabaseSingleton.close_conn()
# print("Konec")