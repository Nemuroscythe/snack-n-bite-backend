from flask import (
    Blueprint, jsonify, request, current_app
)

from main.hello.service import helloService

bp = Blueprint('hello', __name__, url_prefix='/')


@bp.route('/hello')
def get_hello_messages():
    hello_messages = helloService.get_hello_messages()
    current_app.logger.info(hello_messages)
    hello_messages_dict = map(lambda hello_message: hello_message.__dict__, hello_messages)
    return jsonify(list(hello_messages_dict))


@bp.route('/hello/<id>')
def get_hello_message(id):
    message = helloService.get_hello_message(id)
    return jsonify(message.__dict__)


@bp.route('/hello', methods=["POST"])
def create_hello_message():
    body = request.json
    message = helloService.create_hello_message(body)
    return jsonify(message.__dict__), 201


@bp.route('/hello/<id>', methods=["PUT"])
def update_hello_message(id):
    body = request.json
    helloService.update_hello_message(id, body)
    return "", 204


@bp.route('/hello/<id>', methods=["DELETE"])
def delete_hello_message(id):
    helloService.delete_hello_message(id)
    return "", 204
