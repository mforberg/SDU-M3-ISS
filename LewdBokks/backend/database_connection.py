import uuid

import psycopg2

from .db_config import *


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
        result = self.__cursor.execute(query)

        if result:
            return result
        return None

    def insert_dummy_data(self, query, records):

        self.__cursor.executemany(query, records)
        self.__connection.commit()
        print(self.__cursor.rowcount)

    def get_coupons_by_uuid(self, uuid):
        self.__cursor.execute("select * from coupons.coupon where business_uuid = %s", (uuid,))
        return self.__cursor.fetchall()

    def get_user_names(self, username):
        self.__cursor.execute("select business.users.username from business.users where username = %s union all select customers.users.username from customers.users where username = %s", (username, username))
        return self.__cursor.fetchall()

    def get_emails(self, email):
        self.__cursor.execute("select customers.users.email from customers.users where email = %s", (email,))
        return self.__cursor.fetchall()

    def register_person(self, username, password, email):
        id = str(uuid.uuid4())
        self.__cursor.execute("INSERT INTO customers.users VALUES (%s, %s, %s, %s)", (id, username, password, email))
        self.__connection.commit()

    def register_company(self, company_name, website, username, password):
        id = str(uuid.uuid4())
        self.__cursor.execute("INSERT INTO business.users VALUES (%s, %s, %s, %s, %s)", (id, company_name, website, username, password))
        self.__connection.commit()
