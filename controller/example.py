from flask import request, abort, jsonify
from flask.ext.classy import FlaskView, route
from model.migrateversion import MigrateVersion

class ExampleView(FlaskView):
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
            returns.append({'repository_id':data.repository_id,
                            'repository_path':data.repository_path,
                            'version':data.version})
        return jsonify(status=200, message='ok',request=request.form, response=returns)
