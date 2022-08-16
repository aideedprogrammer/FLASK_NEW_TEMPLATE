from urllib.parse import quote
from sqlalchemy.engine import create_engine

class BaseConfig(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/uploads'  # changed to relative path
    TEMPLATE = 'static/template'  # changed to relative path
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    VERSION = ''


class DevelopmentConfig(BaseConfig):
    # DB
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@localhost:3306/flask_new' % quote('s@m@dfans')
    DEBUG = True


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@localhost:3306/flask_new_testing' % quote('s@m@dfans')
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@localhost:3306/flask_new' % quote('s@m@dfans')
    DEBUG = False


config_setting = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
