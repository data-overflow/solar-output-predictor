class Config:
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = "83b566496d124f798db6b92f17af5670"
    SECURITY_PASSWORD_SALT = "0nth3p41ho49e7om1ng6r3at8s1m4na1iv3"

class ProductionConfig(Config):
    DEBUG = False
    DEVELOPMENT = False
