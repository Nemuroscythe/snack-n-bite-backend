from main.dishes.service.dto.dishDTO import DishDTO


def get_dishes():
    return [DishDTO("cheese burger", 3), DishDTO("texas burger", 7)]