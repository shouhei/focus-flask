from model.model import AppModel
from sqlalchemy import func
from sqlalchemy import Column
from sqlalchemy.types import UserDefinedType

class Geometry(UserDefinedType):
    def get_col_spec(self):
        return "GEOMETRY"

    def bind_expression(self, bindvalue):
        return func.GeomFromText(bindvalue, type_=self)

    def column_expression(self, col):
        return func.ASTEXT(col, type_=self)

class Spot(AppModel):
    __tablename__ = 'spots'
    latlng = Column('latlng', Geometry)
