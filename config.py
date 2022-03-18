import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    BOOKS_URL = 'https://www.googleapis.com/books/v1/volumes?q=isbn'

    # Database
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/bookreview'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/bookreview'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}