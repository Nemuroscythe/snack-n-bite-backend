from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('main.config')
app.logger.debug(app.config.get('SQLALCHEMY_DATABASE_URI'))

cors = CORS(app, origins=["http://127.0.0.1:5173", "http://localhost:5173"])

database = SQLAlchemy(app)
database.init_app(app)

from .hello.controller.helloController import bp as hello_blueprint
from .dishes.controller.dishesController import bp as dishes_blueprint

#     Blueprints
app.register_blueprint(hello_blueprint)
app.register_blueprint(dishes_blueprint)
