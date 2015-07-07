from flask import request, abort, jsonify
from flask.ext.classy import FlaskView, route
from model.migrateversion import MigrateVersion

class Example(FlaskView):
    route_base = '/example'
    @route('success')
    def success(self):
        return jsonify(status=200, message='ok', request=request.form, response='')

    @route('error')
    def error(self):
        abort(500)

    @route('migrateversion')
    def migrateversion(self):
        datas = MigrateVersion.all()
        returns = []
        for data in datas:
            returns.append(dict(data))
        return jsonify(status=200, message='ok',request=request.form, response=returns)
