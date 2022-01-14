from bson import ObjectId
from flask import jsonify, request, abort
from flask_restful import Resource

from app import db, app


@app.route('/index')
def index():
    return '111'


class ApiIndex(Resource):

    def get(self):
        """Вывод всех записей из бд"""
        data = db.api.find()
        new = [i for i in data]
        return jsonify(new)

    def post(self):
        """Создание записи в бд"""
        insert_data = request.form.to_dict()
        if bool(insert_data) is True:
            id_create_obj = db.api.insert_one(insert_data)
            create_obj = db.api.find_one({"_id": id_create_obj.inserted_id})
            return jsonify(create_obj)
        abort(404, description="Arguments not found")


class ApiPut(Resource):

    def put(self, id_key):
        """
        Изменение записи в бд
        id_key - это _id в бд
        """
        data = db.api.find_one_and_update({'_id': ObjectId(id_key)},
                                          update={'$set': request.form.to_dict()},
                                          new=True)
        return jsonify(data)
