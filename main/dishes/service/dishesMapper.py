from main.dishes.service.dto.dishDTO import DishDTO


def convert_row_dish_list_to_dish_dto_list(row_dish_list):
    dish_dto_map = map(lambda row_dish: convert_row_dish_to_dish_dto(row_dish), row_dish_list)
    return list(dish_dto_map)


def convert_row_dish_to_dish_dto(row_dish):
    dish = row_dish[0]
    return DishDTO(dish.name, dish.unit_price, dish.id_dishes)
