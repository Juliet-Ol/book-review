import os

class Config:
    # BOOK_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    BOOK_API_KEY = os.environ.get('BOOK_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'poduction':ProdConfig
}    