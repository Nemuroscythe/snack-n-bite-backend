from flask import (
    Blueprint, jsonify, request
)

from main.dish.service import dishService

bp = Blueprint('dish', __name__, url_prefix='/dishes')


@bp.route('')
def get_dishes():
    dishes = dishService.get_dishes()
    dishes_dict = map(lambda dish: dish.__dict__, dishes)
    return jsonify(list(dishes_dict))


@bp.route('/<dish_id>', methods=["GET"])
def get_dish(dish_id):
    dish = dishService.get_dish(dish_id)
    return jsonify(dish.__dict__)


@bp.route('/', methods=["POST"])
def create_dish():
    create_dish_request = request.json
    message = dishService.create_dish(create_dish_request)
    return jsonify(message), 201


@bp.route('', methods=["PUT"])
def update_dish():
    body = request.json
    dishService.update_dish(body)
    return "", 204


@bp.route('', methods=["DELETE"])
def delete_dish(dish_id):
    dishService.delete_dish(id)
    return "", 204
