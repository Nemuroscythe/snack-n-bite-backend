class PositiveNumber:
    def __init__(self, getter, setter):
        self.getter = getter
        self.setter = setter

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return self.getter(instance)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Your *insert name* must be positive !")
        return self.setter(instance, value)


def positive_number(attr):
    def decorator(cls):
        name = "__" + attr

        def getter(self):
            return getattr(self, name)

        def setter(self, value):
            setattr(self, name, value)

        setattr(cls, attr, PositiveNumber(getter, setter))
        return cls

    return decorator
