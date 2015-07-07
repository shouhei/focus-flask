from flask import Flask
from flask import request, abort, jsonify
from flask.ext.classy import FlaskView, route

app = Flask(__name__)

class Example(FlaskView):
    route_base = '/example'
    @route('success')
    def success(self):
        return jsonify(status=200, message='ok', request=request.form, response='')

    @route('error')
    def error(self):
        abort(500)

@app.errorhandler(500)
def error500(error):
    return jsonify(status=error.code, message=error.description, request=request.form, response='')

@app.errorhandler(404)
def error404(error):
    return jsonify(status=error.code, message=error.description, request=request.form, response='')


Example.register(app)
app.config.from_object('config.Config')


if "__main__" == __name__:
    app.run()
