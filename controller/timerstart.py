from flask import request, abort, jsonify
from flask.ext.classy import FlaskView, route
from model.timer import Timer


class TimerStartView(FlaskView):

    def post(self):
        checked_request = self.__check_request(request.form)
        with Timer.transaction():
            timer = Timer(user_id=checked_request["user_id"],
                          spot_id=checked_request["spot_id"],
                          start_at=checked_request["start_at"]
            )
            timer.insert()
        return jsonify(status=200, message='ok', request=request.form,
                       response={'timer_id':timer.id}
               )

    def __check_request(post):
        if not 'spot_id' in post:
            abort(400)
        if not 'start_at' in post:
            abort(400)
        return post
