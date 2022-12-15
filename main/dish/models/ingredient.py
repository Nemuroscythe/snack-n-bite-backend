from main.model import db


class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    name = db.Column(db.String(50), primary_key=True)
    stock_amount = db.Column(db.Integer)
    alerting_amount = db.Column(db.Integer)

    def __init__(self, name, stock_amount=None, alerting_stock=None):
        self.name = name
        self.stock_amount = stock_amount
        self.alerting_stock = alerting_stock
