from sqlalchemy import *
from migrate import *

def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    timers = Table('timers', meta, autoload=True)
    timers.c.result_time.alter(type=String(255), nullable=True)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    timers = Table('timers', meta, autoload=True)
    timers.c.result_time.alter(type=Time, nullable=True)
