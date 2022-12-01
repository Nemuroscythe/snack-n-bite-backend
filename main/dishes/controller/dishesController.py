from flask import (
    Blueprint, jsonify
)

from main.dishes.service import dishesService

bp = Blueprint('dishes', __name__, url_prefix='/dishes')


@bp.route('')
def get_dishes():
    dishes = dishesService.get_dishes()
    dishes_dict = map(lambda dish: dish.__dict__, dishes)
    return jsonify(list(dishes_dict))
