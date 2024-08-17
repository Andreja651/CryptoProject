from datetime import timedelta


class Config:
    SECRET_KEY = 'c70e2d4f0b899bf8b6f0f01e1e5a03e42575b0b1a7fe123f'
    JWT_SECRET_KEY = 'GUpAvS4Pn0Jsb6JYrv2jYwx6p-AHz5CgeL6SYdc3kRo'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=8700) # set to lower expiration date, only for testing
    COIN_API_KEY = 'C36E1AE6-4A57-40F6-AFD1-ED500381AB72'
    COIN_API_ENDPOINT = 'https://rest.coinapi.io/v1/exchangerate/{}/{}'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable SQLAlchemy event system tracker
    SQLALCHEMY_ECHO = False
    DEBUG = True
