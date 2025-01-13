# from src.DatabaseSingleton import *

# def Transaction_by_id(id):
#     sql = "select id,ammount,description from Loyalty_points_transactions where Customer_id = %s"
#     val = [id]
#     conn = DatabaseSingleton()
#     cursor = conn.cursor()
#     try:
#         cursor.execute(sql,val)
#         myresult = cursor.fetchall()
#     except Exception as e:
#         print(e)
#     else:
#         for i in myresult:
#             print(f"id: {i[0]}, množsvý: {i[1]}, popis: {i[2]}")
#     finally:
#         DatabaseSingleton.close_conn()