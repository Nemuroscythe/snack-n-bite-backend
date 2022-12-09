class DishDetailDto:

    def __init__(self, name, unit_price, ingredients, id=None):
        self.name = name
        self.unit_price = unit_price
        self.ingredients = ingredients
        self.id = id
