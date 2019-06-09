from config import config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import os

bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from .main import main as main_blueprint
    from .api import api as api_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api/v1.0')

    return app
