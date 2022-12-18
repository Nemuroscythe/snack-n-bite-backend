from pytest import raises

from main.dish.models.dish import Dish


def test_create_two_dishes_with_different_ids():
    cheese_burger = Dish("cheese burger", 5, "id_cooks")
    texas_burger = Dish("texas burger", 3, "id_cooks")
    assert cheese_burger.id_dishes != texas_burger.id_dishes

def test_dish_with_negative_unit_price_throws_error():
    with raises(ValueError):
        Dish("cheese burger", -2, "id_cooks")


def test_dish_with_0_unit_price_throws_error():
    with raises(ValueError):
        Dish("cheese burger", 0, "id_cooks")

def test_dish_with_empty_name_throws_error():
    with raises(ValueError):
        Dish("", 5, "id_cooks")

def test_dish_with_blank_name_throws_error():
    with raises(ValueError):
        Dish("   ", 5, "id_cooks")


def test_dish_with_number_name_throws_error():
    with raises(ValueError):
        Dish(5, 5, "id_cooks")
