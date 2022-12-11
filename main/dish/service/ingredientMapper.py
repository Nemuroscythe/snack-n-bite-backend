from main.dish.models.ingredient import Ingredient


def to_ingredient_list(ingredients):
    return list(map(lambda ingredient: to_ingredient(ingredient), ingredients))


def to_ingredient(ingredient):
    return Ingredient(ingredient)
