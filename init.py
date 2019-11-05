from config import Config, app

c = Config()
c.__init__()


class init: 

     
     def __init__(self):        

        if app.config["ENV"] == "development":
            app.config.from_object("config.DevelopmentConfig")
        elif app.config["ENV"] == "testing" :
            app.config.from_object("config.TestingConfig")
        elif app.config["ENV"] == "production":
            app.config.from_object("config.ProductionConfig") 

    
    
a = init()
a.__init__()
print (app.config)