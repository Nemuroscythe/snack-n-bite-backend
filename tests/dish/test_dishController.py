import json
from http import HTTPStatus

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace

from main.dish.models.dish import Dish
from main.dish.service.dto.dishDto import DishDto


def test_get_dishes(client, mocker):
    return_value = [Dish("cheese burger", 3, "cooks_id")]
    mocker.patch('main.dish.repository.dishRepository.get_dishes',
                 return_value=return_value)
    expected_dish_list = [DishDto("cheese burger", 3)]

    response = client.get("/dishes")

    assert response.status_code == HTTPStatus.OK
    assert response.is_json

    actual_dish_list = json.loads(response.data, object_hook=lambda d: Namespace(**d))
    assert expected_dish_list[0].name == actual_dish_list[0].name
    assert expected_dish_list[0].unit_price == actual_dish_list[0].unit_price
    assert actual_dish_list[0].id
