from sqlalchemy.engine import Row

from main.dish.service.dto.dishDetailDto import DishDetailDto
from main.dish.service.dto.dishDto import DishDto


def convert_row_dish_list_to_dish_dto_list(row_dish_list):
    dish_dto_map = map(lambda row_dish: convert_row_dish_to_dish_dto(row_dish), row_dish_list)
    return list(dish_dto_map)


def convert_row_dish_to_dish_dto(row_dish):
    dish = row_dish[0] if type(row_dish) == Row else row_dish
    return DishDto(dish.name, dish.unit_price, dish.id_dishes)


def to_dish_detail_dto(dish):
    return DishDetailDto(dish.name,
                         dish.unit_price,
                         list(map(lambda ingredient: ingredient.name, dish.ingredients)))
