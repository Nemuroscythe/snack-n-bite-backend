import uuid


class ValidUUID:

    def __init__(self, getter, setter):
        self.getter = getter
        self.setter = setter

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return self.getter(instance)

    def __set__(self, instance, value):
        if not is_valid_uuid(value):
            raise ValueError("Your *insert name* cannot be empty or blank!")
        return self.setter(instance, value)


def valid_uuid(attr):
    def decorator(cls):
        name = "__" + attr

        def getter(self):
            return getattr(self, name)

        def setter(self, value):
            setattr(self, name, value)

        setattr(cls, attr, ValidUUID(getter, setter))
        return cls

    return decorator


def is_valid_uuid(value):
    try:
        uuid.UUID(str(value))
        return True
    except ValueError:
        return False
