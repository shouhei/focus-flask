import os

class Config(object):
    if 'FOCUS_ENV' in os.environ and os.environ['FOCUS_ENV'] == 'production':
        DATABASE = ''
        DEBUG = False
        TESTING = False
    else:
        DEBUG = True
        TESTING = True
        DATABASE = 'mysql+pymysql://root@localhost/focus_development?charset=utf8'

