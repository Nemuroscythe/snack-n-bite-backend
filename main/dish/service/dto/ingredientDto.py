class IngredientDto:

    def __init__(self, name, stock_amount=None, alerting_stock=None):
        self.name = name
        self.stock_amount = stock_amount
        self.alerting_stock = alerting_stock
