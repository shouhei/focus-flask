from sqlalchemy import create_engine
from sqlalchemy import MetaData
from flask import Flask, current_app

app = Flask(__name__)
with app.app_context():
    current_app.config.from_object('config.Config')

DATABASE = create_engine(app.config['DATABASE'])
METADATA = MetaData(bind=DATABASE, reflect=True)
