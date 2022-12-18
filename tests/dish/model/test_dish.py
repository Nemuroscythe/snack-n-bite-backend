from main.dish.models.dish import Dish


def test_create_two_dishes_with_different_ids():
    cheese_burger = Dish("cheese burger", 5, "id_cooks")
    texas_burger = Dish("texas burger", 3, "id_cooks")
    assert cheese_burger.id_dishes != texas_burger.id_dishes