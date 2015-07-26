from model.model import AppModel
from model.spot import Spot
from model.user import User
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relation

class Timer(AppModel):
    __tablename__ = 'timers'
    spot = relation('Spot', order_by='Spot.id',
                          uselist=False, backref='timer'
    )
    user = relation('User', order_by='User.id',
                          uselist=False, backref='timer'
    )
