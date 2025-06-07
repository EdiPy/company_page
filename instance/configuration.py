class BaseConfig:
    DEBUG = True
    TESTING = False
    

class ProdConfig(BaseConfig):
    DEBUG = False
    

class DevConfig(BaseConfig):
    DEBUG = True
    TESTING = True