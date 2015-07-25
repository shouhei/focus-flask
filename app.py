import re
import inspect
import os
from flask import Flask
from flask import request, abort, jsonify, g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import DeferredReflection
import controller
from model.model import AppModel

# prepare application
app = Flask(__name__)
app.config.from_object('config.Config')

# prepare controller
for pack in os.listdir(controller.__path__[0])[2:]:
    data = __import__(inspect.getmodulename("controller."+pack), fromlist=['controller'])
    for view in filter(lambda item: (re.search("[^Flask]View$", item[0])), inspect.getmembers(data,inspect.isclass)):
        view[1].register(app)


# prepare database and model
engine = create_engine(app.config['DATABASE'])
Session = scoped_session(sessionmaker(bind=engine))
AppModel._set_session(Session)
DeferredReflection.prepare(engine)

# for global action
@app.before_request
def before_request():
    pass

@app.after_request
def after_request(*args, **kwargs):
    session = Session()
    session.commit()
    return args[0]

@app.errorhandler(500)
def error500(error):
    return jsonify(status=error.code, message=error.description, request=request.form, response='')

@app.errorhandler(404)
def error404(error):
    return jsonify(status=error.code, message=error.description, request=request.form, response='')


# if you run this script
if "__main__" == __name__:
    app.run()
