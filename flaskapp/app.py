import os
from flask import Flask

import serializers
from flask_pymongo import PyMongo
from flask_restful import Api

app = Flask(__name__)
app.json_encoder = serializers.ObjectIdJSONEncoder

if os.getenv('HOST') is None:
    app.config["MONGO_URI"] = "mongodb://localhost:27017/api"
else:
    app.config["MONGO_URI"] = "mongodb://mongodb:27017/api"

mongodb_client = PyMongo(app)
db = mongodb_client.db

api = Api(app)
