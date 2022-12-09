from main import app
from main.dish.repository import dishRepository
from main.dish.service import dishMapper


def get_dishes():
    list_row_dish = dishRepository.get_dishes()
    return dishMapper.convert_row_dish_list_to_dish_dto_list(list_row_dish)


def get_dish(dish_id):
    dish = dishRepository.get_dish(dish_id)
    app.logger.debug(dish.ingredients)
    return dishMapper.to_dish_detail_dto(dish)


def create_dish(body):
    return None


def update_dish(id, body):
    return None


def delete_dish(id):
    return None
