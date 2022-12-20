from flask import current_app

from main.dish.repository import dishRepository, ingredientRepository
from main.dish.service import dishMapper
from main.dish.service.dishMapper import to_update_dish_dto
from main.utils.validator.validation import validate_not_blank, validate_strict_positive, validate_uuid


def get_dishes():
    list_row_dish = dishRepository.get_dishes()
    return dishMapper.to_dish_dto_list(list_row_dish)


def get_dish(dish_id):
    dish = dishRepository.get_dish(dish_id)
    current_app.logger.debug(dish.ingredients)
    return dishMapper.to_dish_detail_dto(dish)


def create_dish(create_dish_request):
    validate_not_blank(create_dish_request["name"], "dish name")
    validate_strict_positive(create_dish_request["unit_price"], "unit price")
    validate_uuid(create_dish_request["id_cooks"])

    dish = dishMapper.to_dish(create_dish_request)
    dish.ingredients = list(
        map(lambda ingredient: ingredientRepository.get_ingredient(ingredient.name), dish.ingredients))
    current_app.logger.debug(dish.ingredients)
    return dishRepository.create_dish(dish)


def update_dish(dish_id, update_dish_request):
    validate_not_blank(update_dish_request["name"], "dish name")
    validate_strict_positive(update_dish_request["unit_price"], "unit price")
    validate_uuid(update_dish_request["id_cooks"])

    update_dish_dto = to_update_dish_dto(update_dish_request)
    update_dish_dto.ingredients = list(
        map(lambda ingredient: ingredientRepository.get_ingredient(ingredient.name), update_dish_dto.ingredients))
    dishRepository.update_dish(update_dish_dto, dish_id)
    return None


def delete_dish(dish_id):
    dishRepository.delete_dish(dish_id)
    return None
