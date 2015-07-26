from flask import request, abort, jsonify
from flask.ext.classy import FlaskView, route
from sqlalchemy import func
from model.spot import Spot
from model.timer import Timer

class SpotsView(FlaskView):

    def index(self):
        spots = Spot.all()
        res = []
        for row in spots:
            res.append(
                {
                    'id':row.id,
                    'foursquare_id':row.forsquare_id,
                    'name':row.name,
                    'latlng':row.latlng
                }
            )
        return jsonify(status=200, message='ok', request='', response=res)

    def get(self, id):
        session = Timer._get_session()
        spot = Spot.find(id)
        if not spot:
            abort(500)
        res = []
        sum_label = func.sec_to_time(func.sum(func.time_to_sec(Timer.result_time))).label('sum')
        timer = session.query(Timer, sum_label).filter(Timer.end_at!=None, Timer.spot_id==spot.id).group_by(Timer.user_id).order_by(sum_label.desc()).all()
        n = 0
        for row in timer:
            n += 1;
            res.append(
                {
                    'rank':n,
                    'user':{
                        'id':row[0].user.id,
                        'name':row[0].user.name
                    },
                    'sum':str(row.sum)
                }
            )
        return jsonify(status=200, message='ok', request={'id':id}, response=res)
