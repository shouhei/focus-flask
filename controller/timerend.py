from flask import request, abort, jsonify
from flask.ext.classy import FlaskView, route
from model.migrateversion import MigrateVersion
from model.timer import Timer

class TimerEndView(FlaskView):
    def index(self):
        return jsonify(status=200, message='ok', request='hello', response='')

    def post(self):
        timer = Timer(id=form.request['id'],
                      end_at=form.request['end_at']
        )
        timer.update()
        return jsonify(status=200, message='ok', request=request.form, response="")
