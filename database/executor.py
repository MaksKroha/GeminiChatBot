from database import CONN
from exception import log_exception


# Executes a SQL command on the database. Can fetch
# results if specified (fetchall or fetchone).
# Commits changes to the database and handles
# exceptions by logging them. Ensures the cursor
# is closed after execution. Returns the fetched
# data or None if no fetch option is specified.
def execute(command, fetchall=False, fetchone=False):
    cursor = CONN.cursor()
    result = None
    try:
        cursor.execute(command)
        CONN.commit()
        if fetchall:
            result = cursor.fetchall()
        elif fetchone:
            result = cursor.fetchone()
    except FileExistsError as e:
        log_exception(str(e))
        if fetchall or fetchone:
            return []
    finally:
        cursor.close()
        return result
