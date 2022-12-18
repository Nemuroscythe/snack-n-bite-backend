from pytest import raises

from main.dish.models.dish import Dish

COOKS_UUID = "00000000-e89b-12d3-a456-426614174000"


def test_create_two_dishes_with_different_ids():
    cheese_burger = Dish("cheese burger", 5, COOKS_UUID)
    texas_burger = Dish("texas burger", 3, COOKS_UUID)
    assert cheese_burger.id_dishes != texas_burger.id_dishes


def test_create_dish_with_negative_unit_price_throws_error():
    with raises(ValueError):
        Dish("cheese burger", -2, COOKS_UUID)


def test_create_dish_with_0_unit_price_throws_error():
    with raises(ValueError):
        Dish("cheese burger", 0, COOKS_UUID)


def test_create_dish_with_empty_name_throws_error():
    with raises(ValueError):
        Dish("", 5, COOKS_UUID)


def test_create_dish_with_blank_name_throws_error():
    with raises(ValueError):
        Dish("   ", 5, COOKS_UUID)


def test_create_dish_with_number_name_throws_error():
    with raises(ValueError):
        Dish(5, 5, COOKS_UUID)


def test_create_dish_with_wrong_format_id_throws_error():
    with raises(ValueError):
        Dish("cheese burger", 5, COOKS_UUID, "wrong_id")


def test_create_dish_with_wrong_format_cooks_id_throws_error():
    with raises(ValueError):
        Dish("cheese burger", 5, "wrong_id")