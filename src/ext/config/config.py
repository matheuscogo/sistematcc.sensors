class Config(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = "secret"
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector:///root:@localhost/sistemaTCC"
    SQLALCHEMY_DATABASE_URI = "sqlite:///...sistemaTCC.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # will become default in the future


class ProductionConfig(Config):
    DATABASE_URI = ''


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True