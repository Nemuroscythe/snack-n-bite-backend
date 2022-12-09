from main.dishes.repository import dishesRepository
from main.dishes.service import dishesMapper


def get_dishes():
    list_row_dish = dishesRepository.get_dishes()
    return dishesMapper.convert_row_dish_list_to_dish_dto_list(list_row_dish)


def get_dish(dish_id):
    dish = dishesRepository.get_dish(dish_id)
    return dishesMapper.convert_row_dish_to_dish_dto(dish)


def create_dish(body):
    return None


def update_dish(id, body):
    return None


def delete_dish(id):
    return None
