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
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
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

    def get_user_names(self, username):
        self.__cursor.execute(
            "select business.users.username from business.users where username = %s union all select customers.users.username from customers.users where username = %s",
            (username, username))
        return self.__cursor.fetchall()

    def get_emails(self, email):
        self.__cursor.execute("select customers.users.email from customers.users where email = %s", (email,))
        return self.__cursor.fetchall()

    def get_company_names(self, company_name):
        self.__cursor.execute("select business.users.company_name from business.users where company_name = %s",
                              (company_name,))
        return self.__cursor.fetchall()

    def register_person(self, username, password, email):
        id = str(uuid.uuid4())
        self.__cursor.execute("INSERT INTO customers.users VALUES (%s, %s, %s, %s)", (id, username, password, email))
        self.__connection.commit()

    def register_company(self, company_name, website, username, password):
        id = str(uuid.uuid4())
        print(company_name)
        print(website)
        print(username)
        print(password)
        self.__cursor.execute("INSERT INTO business.users VALUES (%s, %s, %s, %s, %s)",
                              (id, company_name, website, username, password))
        self.__connection.commit()

    def delete_coupon_by_uuids(self, business_uuid, item_uuid):
        self.__cursor.execute("DELETE FROM coupons.coupon WHERE business_uuid = %s AND item_uuid = %s"
                              , (business_uuid, item_uuid,))
        self.__connection.commit()

    def get_distinct_categories(self) -> tuple:
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

    def get_preferences(self, user_uuid: str) -> []:
        self.__cursor.execute("SELECT * FROM preferences.user_preferences WHERE user_uuid = %s", (user_uuid,))
        temp = []
        for item in self.__cursor.fetchall():
            temp.append(item[1])
        return temp
    
    def get_preferences_items(self, preference: str) -> []:
        self.__cursor.execute("SELECT * FROM products.items where uuid in (SELECT item_uuid FROM coupons.coupon WHERE sub_category = %s)", (preference,))
        return self.__cursor.fetchall()

    
    def get_probability(self, item_uuid: str) -> []:
        self.__cursor.execute("SELECT min, max FROM coupons.coupon where item_uuid = %s", (item_uuid,))
        return self.__cursor.fetchall()


    def super_secure_credentials(self, username: str):
        business = self.__cursor.execute("SELECT * FROM business.users WHERE username = %s", (username,))
        result = self.__cursor.fetchall()
        #print(result)
        temp = {}
        if result:
            temp['BUSINESS'] = (result[0][0], result[0][3], result[0][4])
        customer = self.__cursor.execute("SELECT * FROM customers.users WHERE username = %s", (username,))
        result2 = self.__cursor.fetchall()
        if result2:
            temp['CUSTOMER'] = (result2[0][0], result2[0][1], result2[0][2])
        return temp

    def get_uuid_from_username(self, username):
        self.__cursor.execute("SELECT uuid FROM customers.users WHERE username = %s", (username,))
        return self.__cursor.fetchall()

    def update_users_preferences(self, uuid, pref_dict):
        self.__cursor.execute("DELETE FROM preferences.user_preferences WHERE user_uuid = %s", (uuid,))
        self.__connection.commit()
        for item in pref_dict:
            self.__cursor.execute("INSERT INTO preferences.user_preferences VALUES (%s, %s)", (uuid, item))
        self.__connection.commit()
        
    
    def get_products(self):
        self.__cursor.execute("SELECT uuid FROM products.items")    
        return self.__cursor.fetchall()
        
    def get_products_given_preferences(self, preferences):
        product_list = []
        row_list = []
        for preference in preferences:
            self.__cursor.execute("SELECT uuid FROM products.items WHERE sub_category = '{}'".format(preference))
            row_list.append(self.__cursor.fetchall())
        
        for row in row_list:
            product_list.append(row)
            
        return product_list
    
    def add_lootbox(self, user_uuid: str, item_uuid: str, discount: int):
        self.__cursor.execute("INSERT INTO lootbox.boxes VALUES (%s, %s, %s)", (user_uuid, item_uuid, discount,))
        self.__connection.commit()

    def delete_lootbox(self, user_uuid: str, item_uuid: str):
        self.__cursor.excecute("DELETE FROM lootbox.boxes WHERE user_uuid = %s AND item_uuid = %s", (user_uuid, item_uuid))

