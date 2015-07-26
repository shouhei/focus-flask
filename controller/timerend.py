from flask import request, abort, jsonify
from flask.ext.classy import FlaskView, route
from model.migrateversion import MigrateVersion
from model.timer import Timer
from datetime import datetime

class TimerEndView(FlaskView):
    def index(self):
        return jsonify(status=200, message='ok', request='hello', response='')

    def post(self):
        with Timer.transaction():
            timer = Timer.find(request.form['id'])
            timer.update(
                         end_at=request.form['end_at'],
                         result_time=(datetime.strptime(request.form['end_at'],'%Y-%m-%d %H:%M:%S') - timer.start_at)
            )
        return jsonify(status=200, message='ok', request=request.form, response="")
