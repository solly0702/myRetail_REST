import jwt
import datetime
from flask import jsonify, request, current_app as app
from flask_restx import Resource, fields, reqparse

from api.api_settings import api
from .model import Product


ns = api.namespace('products', description='Product operations')

products = Product()


@ns.route('/')
class ProductList(Resource):
    '''Shows a list of all products, and lets you POST to add new tasks'''
    @ns.doc('list_products')
    @ns.marshal_list_with(products.product_model)
    def get(self):
        '''List all products'''
        return products.find({}), 200

    @ns.route('/<int:id>')
    @ns.param('id', 'The product identifier')
    class Product(Resource):
        '''Show a single product item and lets you delete them'''
        @ns.doc('get_product')
        @ns.marshal_with(products.product_model)
        @ns.response(404, 'Product not found')
        def get(self, id):
            '''Fetch a given resource'''
            res = products.find_by_id(id)
            return res if res is not None else api.abort(404, "Product id {} doesn't exist".format(id))

        @ns.expect(products.product_model)
        @ns.marshal_with(products.product_model)
        @ns.response(400, 'Bad Reqeust')
        def put(self, id):
            '''Update a product given its identifier'''
            if int(id) != int(api.payload["id"]):
                return api.abort(400, "ID cannot be modified")
            res = products.update(id, api.payload)
            return res if res is not None else api.abort(400, "Bad Request")


rs = api.namespace("v1/redsky",
                   description="External resource 'API KEY REQUIRED'")

auth = api.model("User", {
    "username": fields.String(required=True, description='username'),
    "password": fields.String(required=True, description='password')
})


@rs.route("/auth")
class Auth(Resource):
    @ns.doc("request_key")
    @ns.expect(auth)
    def post(self):
        '''Creata a key for endpoint "case_study_v1'''
        if api.payload["username"] and api.payload["password"] == "password":
            token = jwt.encode(
                {
                    'user': api.payload["username"],
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
                },
                app.config["SECRET_KEY"],
                algorithm="HS256")
            return jsonify({"key": token})
        else:
            return api.abort(403, "Unable to verify user")


parser = reqparse.RequestParser()
parser.add_argument("key", required=True, help="Required Field")
parser.add_argument("tcin", type=int, help="Product ID")


@rs.route("/case_study_v1")
class External(Resource):
    '''Shows a list of all products, and lets you POST to add new tasks'''
    @ns.doc("external_get")
    @ns.marshal_list_with(products.product_model)
    @api.expect(parser)
    def get(self):
        '''List all products'''
        key = request.args.get("key")

        if not key:
            return api.abort(403, "API key is required")

        try:
            jwt.decode(
                key,
                app.config["SECRET_KEY"],
                algorithms=["HS256"])
        except:
            return api.abort(403, "Invalid key")

        id = request.args.get("tcin")

        if not id:
            return products.find({}), 200
        else:
            res = products.find_by_id(int(id))
            return res if res is not None else api.abort(404, "Product id {} doesn't exist".format(id))
