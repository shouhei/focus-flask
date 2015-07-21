from sqlalchemy import *
from migrate import *
import datetime

def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    organizations = Table('organizations', meta, autoload=True)
    users = Table('users', meta, autoload=True)
    spots = Table('spots', meta, autoload=True)
    timers = Table('timers', meta, autoload=True)

    organizations.c.modified_at.alter(default=datetime.datetime.now)
    users.c.modified_at.alter(default=datetime.datetime.now)
    spots.c.modified_at.alter(default=datetime.datetime.now)
    timers.c.modified_at.alter(default=datetime.datetime.now)



def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    organizations = Table('organizations', meta, autoload=True)
    users = Table('users', meta, autoload=True)
    spots = Table('spots', meta, autoload=True)
    timers = Table('timers', meta, autoload=True)

    organizations.c.modified_at.alter(default=null)
    users.c.modified_at.alter(default=null)
    spots.c.modified_at.alter(default=null)
    timers.c.modified_at.alter(default=null)

