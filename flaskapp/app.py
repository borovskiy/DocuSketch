from flask import Flask
import serializers
from flask_pymongo import PyMongo
from flask_restful import Api

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongodb:27017/api"
app.json_encoder = serializers.ObjectIdJSONEncoder

mongodb_client = PyMongo(app)
db = mongodb_client.db

api = Api(app)
