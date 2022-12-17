class CreateDishDto:

    def __init__(self, id_cooks, name, unit_price, ingredients):
        self.id_cooks = id_cooks
        self.name = name
        self.unit_price = unit_price
        self.ingredients = ingredients
