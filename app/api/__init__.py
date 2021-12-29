from flask import Blueprint

from api.api_settings import api
from api.product.endpoint import rs, ns as product_ns

bp = Blueprint("api", __name__, url_prefix="")

api.init_app(bp)

api.add_namespace(product_ns)
api.add_namespace(rs)
