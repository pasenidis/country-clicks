import mysql.connector
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import settings

def create():
    _db = mysql.connector.connect(
        host = "localhost",
        user = settings.DB_USERNAME,
        password = settings.DB_PASSWORD
    )

    _cursor = _db.cursor()
    _cursor.execute(f"CREATE DATABASE IF NOT EXISTS {settings.DB_NAME}")
    print("Done")

create()