from sqlalchemy import Column, String, TypeDecorator
from model.model import AppModel
import hashlib

class Password(TypeDecorator):
    impl = String
    def process_bind_param(self, value, engine):
        sha = hashlib.sha256()
        sha.update(value.encode('utf-8'))
        return sha.digest()

class User(AppModel):
    __tablename__ = 'users'
    password = Column('password', Password,nullable=False)
