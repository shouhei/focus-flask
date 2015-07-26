from flask import request, abort, jsonify, g
from flask.ext.classy import FlaskView, route
from model.timer import Timer
from model.spot import Spot

class TimerStartView(FlaskView):

    def post(self):
        checked_request = self.__check_request(request.form)
        spot = Spot.find_by(forsquare_id=checked_request['foursquare_id'])
        if not spot:
            checked_request = self.__re_check_request(request.form)
            spot = Spot(
                forsquare_id=checked_request['foursquare_id'],
                name=checked_request['_location'],
                latlng= 'POINT('+ checked_request['lng'] +' '+ checked_request['lat'] + ")"
            )
            spot.insert()
        with Timer.transaction():
            timer = Timer(user_id=g.user.id,
                          spot_id=spot.id,
                          start_at=checked_request["start_at"]
            )
            timer.insert()
        return jsonify(status=200, message='ok', request=request.form,
                       response={'timer_id':timer.id}
               )

    def __check_request(self,post):
        if not 'foursquare_id' in post:
            abort(400)
        if not 'start_at' in post:
            abort(400)
        return post

    def __re_check_request(self, post):
        if not '_location' in post:
            abort(400)
        if not 'lng' in post:
            abort(400)
        if not 'lng' in post:
            abort(400)
        return post
