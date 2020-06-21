import settings
import mysql.connector
import os
import sys
import inspect
import traceback
current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


def get(country):
    _db = mysql.connector.connect(
        host="localhost",
        user=settings.DB_USERNAME,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME
    )

    cursor = _db.cursor()

    try:
        skata = f"SELECT * FROM countries WHERE code = '{country}'"
        cursor.execute(skata)
        final = cursor.fetchone()

        return final
    except:
        traceback.print_exc()
