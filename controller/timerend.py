from flask import request, abort, jsonify, g
from flask.ext.classy import FlaskView, route
from model.migrateversion import MigrateVersion
from model.timer import Timer
from model.spot import Spot
from datetime import datetime
from sqlalchemy import func
import re

class TimerEndView(FlaskView):

    def post(self):
        checked_request = self.__check_request(request.form)
        timer = Timer.find(checked_request['id'])
        with Timer.transaction():
            if not timer:
                abort(404)
            res = datetime.strptime(checked_request['end_at'],'%Y-%m-%d %H:%M:%S') - timer.start_at
            [tmp_minutes, seconds] = divmod(res.total_seconds(), 60)
            [hours, minutes] = divmod(tmp_minutes,60)
            result_time = '%02d:%02d:%02d' % (hours, minutes, seconds)
            timer.update(
                         end_at=checked_request['end_at'],
                         result_time=result_time
            )
        # raking update
        session = Timer._get_session()
        sum_label = func.sec_to_time(func.sum(func.time_to_sec(Timer.result_time))).label('sum')
        ranking_data = (session
                        .query(Timer, sum_label)
                        .filter(Timer.end_at!=None, Timer.spot_id==timer.spot.id)
                        .group_by(Timer.user_id)
                        .order_by(sum_label.desc())
                        .all())
        n = 0
        ranking = []
        for row in ranking_data:
            n += 1;
            ranking.append(
                {
                    'rank':n,
                    'user':{
                        'id':row[0].user.id,
                        'name':row[0].user.name
                    },
                    'sum':str(row.sum)
                }
            )
        [lng,lat] = re.findall('[0-9]*\.[0-9]*', timer.spot.latlng)
        doc = g.mongo.focus
        rank = doc.ranking
        rank.update( {'spot_id': timer.spot.id},
                     {'$set':{'data':ranking,'spot':{'name':timer.spot.name,
                                                     'lat':lat,
                                                     'lng':lng,
                     }
                     }},
                      upsert=True,
                      multi=False)
        # end ranking update
        return jsonify(status=200, message='ok', request=request.form, response="")

    def __check_request(self, post):
        if not 'id' in post:
            abort(400)
        if not 'end_at' in post:
            abort(400)
        return post
