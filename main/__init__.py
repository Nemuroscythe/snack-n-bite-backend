from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('main.config')
app.logger.debug(app.config.get('SQLALCHEMY_DATABASE_URI'))

cors = CORS(app, origins=["http://localhost:3000"])

database = SQLAlchemy(app)
database.init_app(app)

from .hello.controller.helloController import bp

#     Blueprints
app.register_blueprint(bp)
