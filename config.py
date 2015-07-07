import os

class Config(object):
    if 'FOCUS_ENV' in os.environ and os.environ['FOCUS_ENV'] == 'production':
        DATABASE_URI = ''
        DEBUG = False
        TESTING = False
    else:
        DEBUG = True
        TESTING = True
        DATABASE_URI = 'mysql+pymysql://root@localhost/focus_development'

