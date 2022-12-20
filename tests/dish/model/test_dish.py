from pytest import raises

from main.dish.models.dish import Dish

COOKS_UUID = "00000000-e89b-12d3-a456-426614174000"


def test_create_two_dishes_with_different_ids():
    cheese_burger = Dish("cheese burger", 5, COOKS_UUID)
    texas_burger = Dish("texas burger", 3, COOKS_UUID)
    assert cheese_burger.id_dishes != texas_burger.id_dishes