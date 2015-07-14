from sqlalchemy import *
from migrate import *
import datetime

meta = MetaData()

organizations = Table(
    'organizations', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('created_at', DateTime, server_default=func.now(), nullable=False),
    Column('modified_at', DateTime, onupdate=func.now(),nullable=False),
)

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('password', String(255), nullable=False),
    Column('organization_id', ForeignKey('organizations.id')),
    Column('created_at', DateTime, server_default=func.now(), nullable=False),
    Column('modified_at', DateTime, onupdate=func.now(),nullable=False),
)

spots = Table(
    'spots', meta,
    Column('id', Integer, primary_key=True),
    Column('forsquare_id', String(255), nullable=False),
    Column('name', Integer, nullable=False),
    Column('created_at', DateTime, server_default=func.now(), nullable=False),
    Column('modified_at', DateTime, onupdate=func.now(),nullable=False),
)

timers = Table(
    'timers', meta,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('users.id')),
    Column('spot_id', ForeignKey('spots.id')),
    Column('start_at', DateTime, nullable=False),
    Column('end_at', DateTime),
    Column('result_time', Time),
    Column('created_at', DateTime, server_default=func.now(), nullable=False),
    Column('modified_at', DateTime, onupdate=func.now(),nullable=False),
)

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    organizations.create()
    users.create()
    spots.create()
    timers.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    timers.drop()
    spots.drop()
    users.drop()
    organizations.drop()

