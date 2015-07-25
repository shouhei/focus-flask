from flask import request, abort, jsonify
from flask.ext.classy import FlaskView, route
from model.timer import Timer


class TimerStartView(FlaskView):
    def index(self):
        return jsonify(status=200, message='ok', request='timer_start', response='')

    @route('/timerstart/timer/', methods=['GET','POST'])
    def timer(self):
        datas = Timer.all()
        returns = []
        for data in datas:
            returns.append({'id':data.id,
			    'user_id':data.user_id,
			    'spot_id':data.spot_id,
			    'start_at':data.start_at,
			    'end_at':data.end_at,
			    'result_time':data.result_time,
			    'modified':data.modified_at
			   })
        return jsonify(response=returns)

    def post(self):
        timer = Timer(user_id=request.form["user_id"],
                      spot_id=request.form["spot_id"],
                      start_at=request.form["start_at"]
        )
        timer.insert()
        return jsonify(status=200, message='ok', request=request.form,
                       response={'timer_id':timer.id}
               )
