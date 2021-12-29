import logging
from flask_restx import Api

log = logging.getLogger(__name__)


api = Api(
    version="1.0",
    title="myRetail REST API",
    description="Target myRetail RESTful Service",
)


@api.errorhandler
def default_error_handler(e):
    message = "An unhandled exception occurred."
    log.exception(message)

    return {"message": message}, 500
