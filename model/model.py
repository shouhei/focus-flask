from sqlalchemy.ext.declarative import DeferredReflection
from sqlalchemy.ext.declarative import declarative_base


Base=declarative_base()

class AppModel(DeferredReflection, Base):
    __abstract__ = True
    @classmethod
    def _get_session(cls):
        return cls.Session()

    @classmethod
    def _set_session(cls, Session):
        cls.Session = Session
