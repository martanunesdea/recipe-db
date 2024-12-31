"""Flask configuration."""
from os import environ, path
#from dotenv import load_dotenv

#basedir = path.abspath(path.dirname(__file__))
#load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask config variables."""

    FLASK_ENV = 'development'
    TESTING = False
    SECRET_KEY = environ.get('SECRET_KEY') or 'aWFWElcdñfl123CWelxjewdejxnc'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    #MONGO_URI = 'mongodb+srv://cooluser:password12345@cluster0.sbchk.mongodb.net/recipe-db?retryWrites=true&w=majority'
    #URI = 'mongodb+srv://cooluser:password12345@cluster0.sbchk.mongodb.net/recipe-db?retryWrites=true&w=majority'


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = False
    DATABASE_URI = environ.get('DEV_DATABASE_URI')

class TestConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
