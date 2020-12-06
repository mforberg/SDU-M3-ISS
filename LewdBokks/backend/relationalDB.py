import psycopg2
from config import config

connection = psycopg2.connect(
        host="localhost",
        database="Suppliers",
        user="postgres",
        password="1234")

def connect():
    conn = None
    try:
        conn = connection
        cur = conn.cursor()

        cur.execute('SELECT version()')

        db_version =  cur.fetchone()
        print(db_version)

        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    connect()