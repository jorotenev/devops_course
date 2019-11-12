from flask import Flask
from flask_bootstrap import Bootstrap
import logging
from logging.config import dictConfig

from app.helpers.memoize import memoizer


def _base_app(app_config):
    """
    initialise a barebone flask app.
    :arg config_name [string] - the name of the environment; must be a key in the "config" dict
    """
    configure_logging(app_config)

    app = Flask(__name__)
    app.config.from_object(app_config)
    app_config.init_app(app)
    app.static_folder='templates/static'
    app.static_url_path='/static'
    Bootstrap(app)

    return app


def create_app(app_config):
    """
    The factory function that creates the Flask app.
    Register all blueprints here
    """

    import logging as log
    log.info(f"Creating an app for environment: {app_config.__class__.__name__}")

    app = _base_app(app_config)
    memoizer.init_app(app)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    from .pages import pages as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


def configure_logging(app_config):
    """
    http://flask.pocoo.org/docs/1.0/logging/
    "If possible, configure logging before creating the application object.
    """
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': app_config.LOG_LEVEL,
            'handlers': ['wsgi']
        }
    })
    logging.getLogger('botocore').setLevel(logging.CRITICAL)

