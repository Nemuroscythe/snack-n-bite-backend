from flask import (
    Blueprint, jsonify, request
)

from main.dishes.service import dishesService

bp = Blueprint('dishes', __name__, url_prefix='/dishes')


@bp.route('')
def get_dishes():
    dishes = dishesService.get_dishes()
    dishes_dict = map(lambda dish: dish.__dict__, dishes)
    return jsonify(list(dishes_dict))

@bp.route('/<dish_id>', methods=["GET"])
def get_dish(dish_id):
    dish = dishesService.get_dish(dish_id)
    return jsonify(dish.__dict__)

@bp.route('', methods=["POST"])
def create_dishes():
    body = request.json
    message = dishesService.create_dish(body)
    return jsonify(message.__dict__), 201

@bp.route('', methods=["PUT"])
def update_dishes():
    body = request.json
    dishesService.update_dish(body)
    return "", 204

@bp.route('', methods=["DELETE"])
def delete_dishes(dish_id):
    dishesService.delete_dish(id)
    return "", 204