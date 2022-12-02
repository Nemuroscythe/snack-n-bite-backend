from main.dishes.repository import dishesRepository
from main.dishes.service import dishesMapper


def get_dishes():
    list_row_dish = dishesRepository.get_dishes()
    return dishesMapper.convert_row_dish_list_to_dish_dto_list(list_row_dish)
