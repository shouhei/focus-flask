from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    users = Table('users', meta, autoload=True)
    token = Column('token', String(255), nullable=False)
    token.create(users)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    users = Table('users', meta, autoload=True)
    users.c.token.drop()
