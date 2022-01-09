from bson import ObjectId
from flask import jsonify, request, abort
from flask_restful import Resource

import app


class ApiIndex(Resource):

    def get(self):
        data = app.db.api.find()
        new = [i for i in data]
        return jsonify(new)

    def post(self):
        insert_data = request.form.to_dict()
        if bool(insert_data) is True:
            id_create_obj = app.db.api.insert_one(insert_data)
            create_obj = app.db.api.find_one({"_id": id_create_obj.inserted_id})
            return jsonify(create_obj)
        abort(404, description="Arguments not found")


class ApiPut(Resource):

    def put(self, id_key):
        data = app.db.api.find_one_and_update({'_id': ObjectId(id_key)},
                                              update={'$set': request.form.to_dict()},
                                              new=True)
        return jsonify(data)
