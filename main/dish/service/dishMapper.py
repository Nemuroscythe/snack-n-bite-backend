from sqlalchemy.engine import Row

from main.dish.models.dish import Dish
from main.dish.service.dto.dishDetailDto import DishDetailDto
from main.dish.service.dto.dishDto import DishDto
from main.dish.service.ingredientMapper import to_ingredient_list


def to_dish_dto_list(row_dish_list):
    dish_dto_map = map(lambda row_dish: to_dish_dto(row_dish), row_dish_list)
    return list(dish_dto_map)


def to_dish_dto(row_dish):
    dish = row_dish[0] if type(row_dish) == Row else row_dish
    return DishDto(dish.name, dish.unit_price, dish.id_dishes)


def to_dish_detail_dto(dish):
    return DishDetailDto(dish.id_dishes,
                         dish.name,
                         dish.unit_price,
                         list(map(lambda ingredient: ingredient.name, dish.ingredients)))


def to_dish(create_dish_request):
    dish = Dish(create_dish_request["name"], create_dish_request["unit_price"], create_dish_request["id_cooks"])
    dish.ingredients = to_ingredient_list(create_dish_request["ingredients"])
    return dish
