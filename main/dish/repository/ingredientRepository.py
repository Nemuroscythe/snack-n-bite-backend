from main.dish.models.ingredient import Ingredient
from main.model import db


def get_ingredient(ingredient_name):
    return db.get_or_404(Ingredient, ingredient_name)
