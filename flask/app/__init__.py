from flask import Flask, request
from instance.config import app_config
import sys
import os
import logging
from logging.handlers import RotatingFileHandler
from logging import INFO, ERROR, DEBUG, Formatter


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    try:
        app.config.from_object(app_config[config_name])
    except:
        app.config.from_object(app_config['production'])

    # Define logging handler settings
    file_handler = RotatingFileHandler(
        "/var/log/flask/app.log", maxBytes=1024*1024, backupCount=2)
    file_handler.setFormatter(
        Formatter('%(asctime)s pid/%(process)d %(levelname)s: %(message)s'))
    file_handler.setLevel(INFO)

    # logging handler init
    logger = logging.getLogger(__name__)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Register Error handler
    # blueprint doesnt support
    @app.errorhandler(404)
    def handle_error(error):
        print('vao day')
        app.logger.info(f"Page not found {request.path}")
        return ('alochym', 404)

    ####################
    #### blueprints ####
    ####################
    from app.views.mqtt import mqtt
    app.register_blueprint(mqtt, url_prefix="/")

    return app
