import uuid

from sqlalchemy.dialects.postgresql import UUID

from main import database as db


class Dish(db.Model):
    __tablename__ = 'dishes'
    id_dishes = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(50))
    unit_price = db.Column(db.Integer)

    def __init__(self, name, unit_price, id):
        self.name = name
        self.unit_price = unit_price
        self.id_dishes = id
