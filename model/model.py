from sqlalchemy.ext.declarative import DeferredReflection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
import datetime
from contextlib import contextmanager

Base=declarative_base()

class AppModel(DeferredReflection, Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    modified_at = Column('modified_at',default=datetime.datetime.now)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def find(cls, id_):
        session = cls._get_session()
        return session.query(cls).filter_by(id=id_).first()

    @classmethod
    def find_by(cls, **kwargs):
        session = cls._get_session()
        return session.query(cls).filter_by(**kwargs).first()

    def insert(self):
        session = self._get_session()
        session.add(self)
        return self.id

    def update(self, id_, **kwargs):
        session = self._get_session()
        row = self.find(id_)
        for key, value in kwargs.items():
            setattr(row, key, value)
        session.add(row)

    def delete(self):
        session = self._get_session()
        session.delete(self)

    @classmethod
    def _get_session(cls):
        return cls.Session()

    @classmethod
    def _set_session(cls, Session):
        cls.Session = Session

    @classmethod
    @contextmanager
    def transaction(cls):
        session = cls.Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
        finally:
            session.commit()
