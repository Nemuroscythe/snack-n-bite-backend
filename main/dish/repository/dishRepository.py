from main import database as db
from main.dish.models.dish import Dish


def get_dishes():
    row_dish_list = db.session.execute(db.select(Dish)).all()
    return row_dish_list


def get_dish(dish_id):
    return db.get_or_404(Dish, dish_id)


def create_dish(dish):
    db.session.add(dish)
    db.session.commit()
    return dish.id_dishes


def update_dish(dish, dish_id):
    dish_db = db.get_or_404(Dish, dish_id)

    dish_db.name = dish.name
    dish_db.unit_price = dish.unit_price
    dish_db.id_cooks = dish.id_cooks
    dish_db.ingredients = dish.ingredients

    db.session.commit()
    return None


def delete_dish(dish_id):
    dish_db = db.get_or_404(Dish, dish_id)
    db.session.delete(dish_db)
    db.session.commit()
    return None
