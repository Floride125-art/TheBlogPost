import os


class Config:
    SECRET_KEY = 'SECRET_KEY'
    
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://floride:fofo1234@localhost/blog'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") 

class ProdConfig(Config):
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://floride:fofo123@localhost/blog'
    pass


class DevConfig(Config):
     DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}