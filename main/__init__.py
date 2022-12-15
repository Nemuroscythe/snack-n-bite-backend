from flask import Flask
from flask_cors import CORS

from main.model import db


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('main.config')
    app.logger.debug(app.config.get('SQLALCHEMY_DATABASE_URI'))

    cors = CORS(app, origins=["http://127.0.0.1:5173", "http://localhost:5173"])

    db.init_app(app)

    from .hello.controller.helloController import bp as hello_blueprint
    from .dish.controller.dishController import bp as dish_blueprint

    #     Blueprints
    app.register_blueprint(hello_blueprint)
    app.register_blueprint(dish_blueprint)

    return app
