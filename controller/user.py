from flask import request, abort, jsonify
from flask.ext.classy import FlaskView, route
from validate_email import validate_email
import string
from random import randint

from model.user import User
from model.timer import Timer

class UserView(FlaskView):
    def index(self, id):
        pass

    def post(self):
        post_data = self.__check_request(request.form)
        source = string.digits + string.ascii_letters
        token = ''.join(map(str, [source[randint(0, len(source) -1) ] for x in range(0,18)]))
        user = User(name=post_data['name'],
                    mail_address=post_data['mail_address'],
                    password=post_data['password'],
                    token=token,
                    organization_id=1
        )
        user.insert()
        return jsonify(status=200, message='ok', request=request.form, response={'token':token})

    def __check_request(self, post):
        rtn_ary = {}
        if 'name' in post:
            rtn_ary['name'] = post['name']
        if 'mail_address' in post and validate_email(post['mail_address']):
            rtn_ary['mail_address'] = post['mail_address']
        if 'password' in post:
            rtn_ary['password'] = post['password']
        return rtn_ary


    def history(self):
        session = Timer._get_session()
        timer = session.query(Timer).filter(Timer.user_id==1,Timer.end_at!=None).all()
        res = []
        for row in timer:
            res.append(
                {'id':row.id,
                 'result_time': row.result_time,
                 'spot':{
                     'id':row.spot_id,
                     'name':row.spot.name,
                     'latlng':row.spot.latlng
                 },
                 'created_at': row.created_at
                }
            )
        return jsonify(status=200, message="ok",request=request.form, response=res)
