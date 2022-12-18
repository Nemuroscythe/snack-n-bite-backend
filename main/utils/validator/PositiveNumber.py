class PositiveNumber:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("Your *insert name* must be positive !")
        self.value = value


def positive_number(attr):
    def decorator(cls):
        setattr(cls, attr, PositiveNumber())
        return cls

    return decorator