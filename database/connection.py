from psycopg2 import connect
from time import sleep
from exception import log_exception


# Establishes a connection to a PostgreSQL database
# using the provided credentials. Retries the
# connection if an exception occurs, with a 3-second
# delay between attempts. Logs any exceptions that
# occur during the connection process. Returns the
# connection object if successful.
def get_connection(db_name):
    try:
        connection = connect(host="postgresppp",
                            database=db_name,
                            user="root",
                            password="1234",
                            port="5432")
        return connection
    except Exception as e:
        log_exception(str(e))
        sleep(3)
        return get_connection(db_name)