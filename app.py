from flask import Flask
from flask import request, abort, jsonify

from sqlalchemy import create_engine
from sqlalchemy import MetaData


app = Flask(__name__)
app.config.from_object('config.Config')

@app.before_request
def before_request():
    pass

@app.errorhandler(500)
def error500(error):
    return jsonify(status=error.code, message=error.description, request=request.form, response='')

@app.errorhandler(404)
def error404(error):
    return jsonify(status=error.code, message=error.description, request=request.form, response='')


from controller.example import Example
Example.register(app)

if "__main__" == __name__:
    app.run()
