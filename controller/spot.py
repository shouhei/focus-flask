from flask import request, abort, jsonify
from flask.ext.classy import FlaskView, route
from model.spot import Spot

class SpotView(FlaskView):
    def index(self):
        spots = Spot.all()
        res = []
        for row in spots:
            print(row.name)
            res.append(
                {
                    'id':row.id,
                    'forsquare_id':row.forsquare_id,
                    'name':row.name,
                    'latlng':row.latlng
                }
            )
        return jsonify(status=200, message='ok', request=request.form, response=res)

    def get(self, id):
        pass
