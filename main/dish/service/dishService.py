from main import app
from main.dish.repository import dishRepository, ingredientRepository
from main.dish.service import dishMapper


def get_dishes():
    list_row_dish = dishRepository.get_dishes()
    return dishMapper.convert_row_dish_list_to_dish_dto_list(list_row_dish)


def get_dish(dish_id):
    dish = dishRepository.get_dish(dish_id)
    app.logger.debug(dish.ingredients)
    return dishMapper.to_dish_detail_dto(dish)


def create_dish(create_dish_request):
    dish = dishMapper.to_dish(create_dish_request)
    dish.ingredients = list(map(lambda ingredient: ingredientRepository.get_ingredient(ingredient.name), dish.ingredients))
    app.logger.debug(dish.ingredients)
    return dishRepository.create_dish(dish)


def update_dish(dish_id, update_dish_request):
    dish = dishMapper.to_dish(update_dish_request)
    dish.ingredients = list(map(lambda ingredient: ingredientRepository.get_ingredient(ingredient.name), dish.ingredients))
    dishRepository.update_dish(dish, dish_id)
    return None


def delete_dish(dish_id):
    dishRepository.delete_dish(dish_id)
    return None
