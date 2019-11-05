from datetime import datetime, timedelta
from flask import Flask

app = Flask(__name__)

class  Config: 

    

    def __init__(self):
        
        app.SESSION_REFRESH_EACH_REQUEST = False
        app.SESSION_COOKIE_SECURE = True
        app.PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)    

        app.DEBUG = False
        app.TESTING = False 
        app.SECRET_KEY = None

        app.config["APPLICATION_NAME"] = "AAPI"
        app.config["APPLICATION_DESCRIPTION"] = "The application API for reading charactor from images" 

        app.config["ENV"] = "development"   #The available value are development,  testing, production


class DevelopmentConfig(Config):   
    app.DEBUG = True
    app.TESTING = True 
    app.SECRET_KEY = "0000"  
    app.PERMANENT_SESSION_LIFETIME = timedelta(minutes=2)

class TestingConfig(Config):
    app.DEBUG = True
    app.TESTING = True 
    app.SECRET_KEY = "1111" 
    app.PERMANENT_SESSION_LIFETIME = timedelta(minutes=30) 

class ProductionConfig(Config):
    app.DEBUG = False
    app.TESTING = False
    app.SECRET_KEY = "2222"  
    app.PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)


