from pytest import raises

from main.utils.validator.validation import validate_not_blank, validate_strict_positive, validate_uuid


def test_validate_not_blank():
    assert validate_not_blank("string") is None


def test_validate_not_blank_with_empty_string_throws_value_error():
    with raises(ValueError) as exception:
        validate_not_blank("", "empty string")
    assert str(exception.value) == "Your empty string cannot be empty or blank!"


def test_validate_not_blank_with_blank_name_throws_value_error():
    with raises(ValueError) as exception:
        validate_not_blank("  ", "blank string")
    assert str(exception.value) == "Your blank string cannot be empty or blank!"


def test_validate_not_blank_with_number_throws_value_error():
    with raises(ValueError) as exception:
        validate_not_blank(5, "number")
    assert str(exception.value) == "Your number isn't a string!"


def test_validate_strict_positive():
    assert validate_strict_positive(5) is None


def test_validate_strict_positive_with_negative_number_throws_value_error():
    with raises(ValueError) as exception:
        validate_strict_positive(-5, "negative number")
    assert str(exception.value) == "Your negative number must be strictly positive!"


def test_validate_strict_positive_with_zero_throws_value_error():
    with raises(ValueError) as exception:
        validate_strict_positive(0, "number")
    assert str(exception.value) == "Your number must be strictly positive!"


def test_validate_strict_positive_with_string_throws_value_error():
    with raises(ValueError) as exception:
        validate_strict_positive("five", "string")
    assert str(exception.value) == "Your string is not a number!"


def test_validate_uuid():
    assert validate_uuid("00000000-e89b-12d3-a456-426614174000") is None


def test_validate_uuid_with_wrong_format_string_throws_value_error():
    with raises(ValueError):
        validate_uuid("wrong format")
