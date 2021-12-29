import os
import logging.config

from app import create_app

logging_conf_path = os.path.normpath(os.path.join(
    os.path.dirname(__file__), "./logging.conf"))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

app = create_app()

if __name__ == "__main__":
    host = app.config["HOST"]
    port = app.config["PORT"]
    log.info(">>>>> Dev server at http://{}:{}/ <<<<<".format(host, port,))
    app.run(host=host, port=port, debug=app.config["FLASK_DEBUG"])
