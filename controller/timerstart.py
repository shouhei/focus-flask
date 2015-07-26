from flask import request, abort, jsonify
from flask.ext.classy import FlaskView, route
from model.timer import Timer


class TimerStartView(FlaskView):
    def index(self):
        return jsonify(status=200, message='ok', request='timer_start', response='')

    def post(self):
        with Timer.transaction():
            timer = Timer(user_id=request.form["user_id"],
                          spot_id=request.form["spot_id"],
                          start_at=request.form["start_at"]
            )
            timer.insert()
        return jsonify(status=200, message='ok', request=request.form,
                       response={'timer_id':timer.id}
               )
