import os

class Config(object):
    if os.environ == 'production':
        DATABASE_URI = ''
        DEBUG = False
        TESTING = False
    else:
        DEBUG = True
        TESTING = True
        DATABASE_URI = 'mysql://root@localhost/focus_development'

