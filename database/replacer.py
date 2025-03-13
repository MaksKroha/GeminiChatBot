from database import CONN


def replace_table_data(table_name, chat_1, chat_2, chat_3):
    cursor = CONN.cursor()
    try:
        cursor.execute(f"TRUNCATE TABLE {table_name}")
        cursor.execute(f"INSERT INTO {table_name} (chat_1, chat_2, chat_3) VALUES (%s, %s, %s)",
                       (chat_1, chat_2, chat_3))
        CONN.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
