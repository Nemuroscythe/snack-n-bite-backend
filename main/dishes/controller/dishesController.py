from flask import (
    Blueprint, jsonify
)

bp = Blueprint('dishes', __name__, url_prefix='/dishes')


@bp.route('')
def get_dishes():
    return jsonify(["cheese burger", "texas burger"])
