from bson import ObjectId
from bson.errors import InvalidId
from django.core.exceptions import BadRequest


class IdParserMixin:
    def parse_obj_id(self, _id):
        try:
            return ObjectId(_id)
        except InvalidId:
            raise BadRequest('Error: Invalid object ID')
