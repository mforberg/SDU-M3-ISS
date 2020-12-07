import psycopg2

from db_config import *


class DatabaseConnection:

    __instance__ = None
    __connection = None
    __cursor = None

    def __init__(self):
        if DatabaseConnection.__instance__ is None:
            DatabaseConnection.__instance__ = self
            try:
                self.__connection = psycopg2.connect(
                    host=db_host,
                    database=db_database,
                    user=db_user,
                    password=db_password
                )
                self.__cursor = self.__connection.cursor()
                self.__cursor.execute("SELECT VERSION();")
                record = self.__cursor.fetchone()
                print(record)
            except Exception as e:
                print("Whoops: " + str(e))
        else:
            raise Exception("Whoops")

    @staticmethod
    def get_instance():
        if not DatabaseConnection.__instance__:
            DatabaseConnection()
        return DatabaseConnection.__instance__

    def query(self, query):
        self.__cursor.execute(query)
        return self.__cursor.fetchall()
