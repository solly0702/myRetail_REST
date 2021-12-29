from factory.database import Database
from factory.validation import Validator
from flask_restx import fields

from api.api_settings import api


class Product(object):
    def __init__(self):
        self.validator = Validator()
        self.db = Database()

        self.collection_name = "product"
        self.current_price_model = api.model("Current Price", {
            "value": fields.Float(required=True, description='The price of product'),
            "currency_code": fields.String(required=True, description='The currency of product')
        })

        self.product_model = api.model('Product', {
            'id': fields.Integer(required=True, description='The product unique identifier'),
            'name': fields.String(required=True, description='The name of product'),
            "current_price": fields.Nested(self.current_price_model)
        })

    def find(self, product):
        return self.db.find(product, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, payload):
        fields = self.product_model._schema["properties"]
        fields["current_price"] = self.current_price_model._schema["properties"]
        self.validator.validate(payload, fields)
        return self.db.update(id, payload, self.collection_name)
