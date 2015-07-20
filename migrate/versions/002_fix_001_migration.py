from sqlalchemy import *
from migrate import *

def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    spots = Table('spots', meta, autoload=True)
    spots.c.name.drop()
    name = Column('name', String(255), nullable=False)
    name.create(spots)



def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    spots = Table('spots', meta, autoload=True)
    spots.c.name.drop()
    name = Column('name', Integer, nullable=False)
    name.create(spots)
