import psycopg2
import uuid
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

    def get_coupons_by_uuid(self, uuid) -> list:
        self.__cursor.execute("select * from coupons.coupon where business_uuid = %s", (uuid,))
        return self.__cursor.fetchall()

    def delete_coupon_by_uuids(self, business_uuid, item_uuid):
        self.__cursor.execute("DELETE FROM coupons.coupon WHERE business_uuid = %s AND item_uuid = %s"
                              , (business_uuid, item_uuid,))
        self.__connection.commit()

    def get_distinct_primary_categories(self) -> tuple:
        self.__cursor.execute("select distinct primary_category from products.items")
        primary_categories = []
        for item in self.__cursor.fetchall():
            primary_categories.append(item[0])
        self.__cursor.execute("select distinct sub_category from products.items")
        sub_categories = []
        for item in self.__cursor.fetchall():
            sub_categories.append(item[0])
        primary_categories.sort()
        sub_categories.sort()
        tup = (primary_categories, sub_categories)
        return tup

    def add_coupon(self, b_uuid, coupon_data):

        item_uuid = str(uuid.uuid4())
        prime_category = coupon_data['prime_category']
        sub_category = coupon_data['sub_category']
        brand = coupon_data['brand']
        color = coupon_data['color']
        price = coupon_data['price']
        style = coupon_data['style']
        min_p = coupon_data['min_p']
        max_p = coupon_data['max_p']

        self.__cursor.execute("INSERT INTO coupons.coupon VALUES (%s, %s, %s, %s)", (b_uuid, item_uuid, min_p, max_p,))
        self.__cursor.execute("INSERT INTO products.items VALUES (%s, %s, %s, %s, %s, %s, %s)"
                              , (item_uuid, prime_category, sub_category, brand, color, price, style))
        self.__connection.commit()

