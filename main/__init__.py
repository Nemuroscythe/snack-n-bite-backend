from flask import Flask
from flask_cors import CORS

from main.model import db


def create_app(config="LocalConfig"):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("main.config." + config)
    app.logger.debug(app.config.get("SQLALCHEMY_DATABASE_URI"))

    origins = (app.config.get("FRONTEND_ORIGINS")).split(",")
    app.logger.debug(origins)

    cors = CORS(app, origins=origins)

    db.init_app(app)

    from .hello.controller.helloController import bp as hello_blueprint
    from .dish.controller.dishController import bp as dish_blueprint

    #     Blueprints
    app.register_blueprint(hello_blueprint)
    app.register_blueprint(dish_blueprint)

    return app
