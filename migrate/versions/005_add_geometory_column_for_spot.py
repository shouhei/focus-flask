from sqlalchemy import *
from migrate import *
from sqlalchemy.types import UserDefinedType

class Geometory(UserDefinedType):
    def get_col_spec(self):
        return "GEOMETRY"


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    spots = Table('spots', meta, autoload=True)
    latlng = Column('latlng', Geometory, nullable=False)
    latlng.create(spots)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    spots = Table('spots', meta, autoload=True)
    spots.c.latlng.drop()
