from database import CONN


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
        print(e)
    finally:
        cursor.close()
        return result
