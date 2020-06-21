class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "FSFrLa-ONw33vrTu6HgUWw"

    DB_NAME = "production-db"
    DB_USERNAME = "admin"
    DB_PASSWORD = "example"

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = "click_countries"
    DB_USERNAME = "click"
    DB_PASSWORD = "passcode"