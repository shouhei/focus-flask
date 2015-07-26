from flask import request, abort, jsonify, g
from flask.ext.classy import FlaskView, route
from sqlalchemy import func
from model.spot import Spot
from model.timer import Timer
from bson.json_util import dumps

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
        f = g.mongo.focus
        print(f)
        rank = f.ranking
        return jsonify(status=200, message='ok', request={'id':id}, response=rank.find_one({'spot_id':int(id)},{"_id":0}))
