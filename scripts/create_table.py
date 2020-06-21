import mysql.connector
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import settings

from country_list import countries_for_language
countries = dict(countries_for_language('en'))

def create():
    _db = mysql.connector.connect(
        host = "localhost",
        user = settings.DB_USERNAME,
        password = settings.DB_PASSWORD,
        database = settings.DB_NAME
    )

    _cursor = _db.cursor()
    _cursor.execute("CREATE TABLE IF NOT EXISTS countries (name VARCHAR(50), code VARCHAR(2), clicks INT)")
    
    for country in countries:
        print("Creating row " + country)
        _cursor.execute(f"INSERT INTO countries (name, code, clicks) VALUES ('{countries[country]}', '{country}', 0)")
        _db.commit()

    print("Done")

create()