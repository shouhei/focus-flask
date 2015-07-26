from model.model import AppModel
from model.spot import Spot
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relation

class Timer(AppModel):
    __tablename__ = 'timers'
    spot = relation('Spot', order_by='Spot.id',
                          uselist=False, backref='timer')
