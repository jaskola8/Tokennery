class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    with open('.env', 'r') as env:
        db_password = env.readline().split('=')[1].strip('\n')

    debug = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://api:" + db_password + "@db/tokennery"
    SQLALCHEMY_ECHO = True

