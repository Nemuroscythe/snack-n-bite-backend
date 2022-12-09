import uuid

from sqlalchemy.dialects.postgresql import UUID

from main import database as db
from main.dish.models.ingredient import Ingredient

dishes_ingredients = db.Table('dishes_ingredients',
                              db.Column('id_dishes', db.Integer, db.ForeignKey('dishes.id_dishes')),
                              db.Column('name', db.Integer, db.ForeignKey('ingredients.name')))


class Dish(db.Model):
    __tablename__ = 'dishes'
    id_dishes = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(50))
    unit_price = db.Column(db.Integer)
    ingredients = db.relationship(Ingredient, secondary=dishes_ingredients, backref='dishes')

    def __init__(self, name, unit_price, id):
        self.name = name
        self.unit_price = unit_price
        self.id_dishes = id
