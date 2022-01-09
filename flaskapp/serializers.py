from bson import ObjectId
from flask.json import JSONEncoder


class ObjectIdJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(ObjectIdJSONEncoder, self).default(obj)
