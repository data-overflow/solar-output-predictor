class Config:
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = "83b566496d124f798db6b92f17af5670"
    SECURITY_PASSWORD_SALT = "0nth3p41ho49e7om1ng6r3at8s1m4na1iv3"
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = "help.datable@outlook.com"
    MAIL_PASSWORD = "69!@#$%420^&*()Ppkv"
    DEFAULT_MAIL_SENDER = "help.datable@outlook.com"


class ProductionConfig(Config):
    DEBUG = False
    DEVELOPMENT = False
