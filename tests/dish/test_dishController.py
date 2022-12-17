import json
from http import HTTPStatus

from main.dish.models.ingredient import Ingredient
from main.dish.service.dto.dishDetailDto import DishDetailDto

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace

from main.dish.models.dish import Dish
from main.dish.service.dto.dishDto import DishDto

DISH_UUID = "123e4567-e89b-12d3-a456-426614174000"


def test_get_dishes(client, mocker):
    return_value = [Dish("cheese burger", 3, "cooks_id")]
    mocker.patch('main.dish.repository.dishRepository.get_dishes',
                 return_value=return_value)
    expected_dish_list = [DishDto("cheese burger", 3)]

    response = client.get("/dishes")

    assert response.status_code == HTTPStatus.OK
    assert response.is_json

    actual_dish_list = json.loads(response.data, object_hook=lambda d: Namespace(**d))
    assert actual_dish_list[0].name == expected_dish_list[0].name
    assert actual_dish_list[0].unit_price == expected_dish_list[0].unit_price
    assert actual_dish_list[0].id


def test_get_dish(client, mocker):
    mocked_dish = Dish("cheese burger", 3, "cooks_id", DISH_UUID)
    mocked_dish.ingredients = [Ingredient("bun")]
    mocker.patch('main.dish.repository.dishRepository.get_dish',
                 return_value=mocked_dish)

    expected_dish_detail = DishDetailDto(DISH_UUID, "cheese burger", 3, [Ingredient("bun")])

    response = client.get("/dishes/" + DISH_UUID)

    assert response.status_code == HTTPStatus.OK
    assert response.is_json

    actual_dish_detail = json.loads(response.data, object_hook=lambda d: Namespace(**d))
    assert actual_dish_detail.name == expected_dish_detail.name
    assert actual_dish_detail.unit_price == expected_dish_detail.unit_price
    assert actual_dish_detail.id == expected_dish_detail.id
    assert actual_dish_detail.ingredients[0] == expected_dish_detail.ingredients[0].name
