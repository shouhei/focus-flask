from sqlalchemy import *
from migrate import *
import datetime

meta = MetaData()
timer_start = Table(
    'timer_start', meta,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, nullable=False),
    Column('timer_key', Integer, nullable=False),
    Column('created_at', DateTime, server_default=func.now(), nullable=False),
    Column('modified_at', DateTime, server_default=func.now(), onupdate=func.now(),nullable=False),
)

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    timer_start.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    timer_start.drop()

