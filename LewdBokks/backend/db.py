# from pymongo import MongoClient
# from . import config as conf
#
#
# code = conf.db_password
#
#
# def get_connection():
#     return MongoClient(
#         "mongodb+srv://bobitybo:" + code + "@cluster0.rtdkg.mongodb.net/ISSProject?retryWrites=true&w=majority")
#
#
# def get_table(db_name: str):
#     return db[db_name]
#
#
# def get_db():
#     return db
#
#
# connection = get_connection()
# db = connection["ISSProject"]
# accounts = db["Accounts"]
# preferences = db["Preferences"]
