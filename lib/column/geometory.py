from sqlalchemy import func
from sqlalchemy.types import UserDefinedType

class Geometory(UserDefinedType):
    def get_col_spec(self):
        return "GEOMETRY"

    def bind_expression(self, bindvalue):
        return func.GeomFromText(bindvalue, type_=self)

    def column_expression(self, col):
        return func.ASTEXT(col, type_=self)