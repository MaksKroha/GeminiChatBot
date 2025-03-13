from psycopg2 import connect
from time import sleep


def get_connection(db_name):
    try:
        connection = connect(host="localhost",
                            database=db_name,
                            user="root",
                            password="1234",
                            port="5432")
        return connection
    except Exception as e:
        print(f"--- {e} ---")
        sleep(3)
        return connect(db_name)