import json
from http import HTTPStatus

from main.dish.models.ingredient import Ingredient
from main.dish.service.dto.createDishDto import CreateDishDto
from main.dish.service.dto.dishDetailDto import DishDetailDto
from main.dish.service.dto.ingredientDto import IngredientDto

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace

from main.dish.models.dish import Dish
from main.dish.service.dto.dishDto import DishDto

DISH_UUID = "123e4567-e89b-12d3-a456-426614174000"
COOKS_UUID = "00000000-e89b-12d3-a456-426614174000"

def test_get_dishes(client, mocker):
    mocker.patch('main.dish.repository.dishRepository.get_dishes',
                 return_value=[Dish("cheese burger", 3, COOKS_UUID)])
    expected_dish_list = [DishDto("cheese burger", 3)]

    response = client.get("/dishes")

    assert response.status_code == HTTPStatus.OK
    assert response.is_json

    actual_dish_list = json.loads(response.data, object_hook=lambda d: Namespace(**d))
    assert actual_dish_list[0].name == expected_dish_list[0].name
    assert actual_dish_list[0].unit_price == expected_dish_list[0].unit_price
    assert actual_dish_list[0].id


def test_get_dish(client, mocker):
    mocked_dish = Dish("cheese burger", 3, COOKS_UUID, DISH_UUID)
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


def test_create_dish(client, mocker):
    mocker.patch('main.dish.repository.dishRepository.create_dish',
                 return_value=None)
    mocker.patch('main.dish.repository.ingredientRepository.get_ingredient',
                 return_value=Ingredient("bun"))
    create_dish = CreateDishDto(COOKS_UUID,
                                "cheese burger",
                                3,
                                [IngredientDto("bun").__dict__])

    dict__ = create_dish.__dict__
    body = json.dumps(dict__)
    response = client.post("/dishes",
                           data=body,
                           content_type='application/json')

    assert response.status_code == HTTPStatus.CREATED
    assert response.is_json


def test_update_dish(client, mocker):
    mocker.patch('main.dish.repository.dishRepository.update_dish',
                 return_value=None)
    mocker.patch('main.dish.repository.ingredientRepository.get_ingredient',
                 return_value=Ingredient("bun"))
    create_dish = CreateDishDto(COOKS_UUID,
                                "cheese burger",
                                3,
                                [IngredientDto("bun").__dict__])

    dict__ = create_dish.__dict__
    body = json.dumps(dict__)
    response = client.put("/dishes/" + DISH_UUID,
                          data=body,
                          content_type="application/json")

    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_dish(client, mocker):
    mocker.patch('main.dish.repository.dishRepository.delete_dish',
                 return_value=None)

    response = client.delete("/dishes/" + DISH_UUID)

    assert response.status_code == HTTPStatus.NO_CONTENT
