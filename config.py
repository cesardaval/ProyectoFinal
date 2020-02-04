import os


class Config(object):
    """docstring for Config"""
    SECRET_KEY = "lnsaldkaksd"


class Configuracion_desarrollo(Config):
    DEBUG = True
    PORT = 7000
<<<<<<< HEAD
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:proquinteroXDXD@localhost/Prueba3'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cesardaval:12345678cc@cesardaval.mysql.pythonanywhere-services.com/cesardaval$Prueba3'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///databases/Prueba3.db'
=======
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:proquinteroXDXD@localhost/Prueba3'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cesardaval:12345678cc@cesardaval.mysql.pythonanywhere-services.com/cesardaval$Prueba3'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///databases/Prueba3.db'
>>>>>>> dcd4f3467b18b73fb15b20e39546f80107b1bb22
    SQLALCHEMY_TRACK_MODIFICATIONS = False
