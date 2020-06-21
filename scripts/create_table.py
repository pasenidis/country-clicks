import mysql.connector
from config import DevelopmentConfig

def create():
    _db = mysql.connector.connect(
        host = "localhost",
        user = DevelopmentConfig.DB_USERNAME,
        password = DevelopmentConfig.DB_PASSWORD
    )

    _cursor = _db.cursor()
    _cursor.execute("CREATE TABLE onoma (name)")