from main.dishes.repository import dishesRepository
from main.dishes.service import dishesMapper
from main.dishes.service.dto.dishDTO import DishDTO


def get_dishes():
    list_row_dish = dishesRepository.get_dishes()
    return dishesMapper.convert_row_dish_list_to_dish_dto_list(list_row_dish)


def create_dish(body):
    return None


def update_dish(id, body):
    return None


def delete_dish(id):
    return None


def get_dish():
    return DishDTO("pizza", 3, "id")