from flask import Flask
from flask import request, abort, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeferredReflection

from controller.example import Example
from model.model import AppModel

# prepare application
app = Flask(__name__)
app.config.from_object('config.Config')

# prepare controller
Example.register(app)


# prepare database and model
engine = create_engine(app.config['DATABASE'])
AppModel._set_session(sessionmaker(bind=engine))
DeferredReflection.prepare(engine)

# for global action
@app.before_request
def before_request():
    pass

@app.errorhandler(500)
def error500(error):
    return jsonify(status=error.code, message=error.description, request=request.form, response='')

@app.errorhandler(404)
def error404(error):
    return jsonify(status=error.code, message=error.description, request=request.form, response='')


# if you run this script
if "__main__" == __name__:
    app.run()
