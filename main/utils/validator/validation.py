import uuid


def validate_not_blank(value, value_name="value"):
    if not isinstance(value, str):
        raise ValueError("Your {0} isn't a string!".format(value_name))
    if not value.strip():
        raise ValueError("Your {0} cannot be empty or blank!".format(value_name))


def validate_strict_positive(value, value_name="value"):
    if not isinstance(value, int) and not isinstance(value,float):
        raise ValueError("Your {0} is not a number!".format(value_name))
    if value <= 0:
        raise ValueError("Your {0} must be strictly positive!".format(value_name))


def validate_uuid(value):
    uuid.UUID(str(value))

