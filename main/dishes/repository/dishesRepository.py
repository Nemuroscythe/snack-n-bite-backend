from main import database as db
from main.dishes.models.dish import Dish


def get_dishes():
    row_dish_list = db.session.execute(db.select(Dish)).all()
    return row_dish_list
