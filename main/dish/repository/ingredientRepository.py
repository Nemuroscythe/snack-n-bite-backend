from main import database as db
from main.dish.models.ingredient import Ingredient


def get_ingredient(ingredient_name):
    return db.get_or_404(Ingredient, ingredient_name)
