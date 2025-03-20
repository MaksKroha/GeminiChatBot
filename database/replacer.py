from database import CONN
from exception import log_exception


# Replaces the data in a specified database table
# with new chat entries. Clears the existing table
# data using TRUNCATE and inserts the provided
# chat_1, chat_2, and chat_3 values. Ensures the
# changes are committed to the database. Logs any
# exceptions that occur and closes the cursor
# after the operation.
def replace_table_data(table_name, chat_1, chat_2, chat_3):
    cursor = CONN.cursor()
    try:
        cursor.execute(f"TRUNCATE TABLE {table_name}")
        cursor.execute(f"INSERT INTO {table_name} (chat_1, chat_2, chat_3) VALUES (%s, %s, %s)",
                       (chat_1, chat_2, chat_3))
        CONN.commit()
    except Exception as e:
        log_exception(str(e))
    finally:
        cursor.close()
