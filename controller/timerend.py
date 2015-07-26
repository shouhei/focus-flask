from flask import request, abort, jsonify
from flask.ext.classy import FlaskView, route
from model.migrateversion import MigrateVersion
from model.timer import Timer
from datetime import datetime

class TimerEndView(FlaskView):

    def post(self):
        checked_request = self.__check_request(request.form)
        with Timer.transaction():
            timer = Timer.find(checked_request['id'])
            if not timer:
                abort(404)
            res = datetime.strptime(checked_request['end_at'],'%Y-%m-%d %H:%M:%S') - timer.start_at
            [tmp_minutes, seconds] = divmod(res.total_seconds(), 60)
            [hours, minutes] = divmod(tmp_minutes,60)
            result_time = '%02d:%02d:%02d' % (hours, minutes, seconds)
            timer.update(
                         end_at=request.form['end_at'],
                         result_time=result_time
            )
        return jsonify(status=200, message='ok', request=request.form, response="")

    def __check_request(post):
        if not 'id' in post:
            abort(400)
        if not 'checked_request' in post:
            abort(400)
        return post
