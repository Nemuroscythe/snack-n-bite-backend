class NotBlank:
    def __init__(self, getter, setter):
        self.getter = getter
        self.setter = setter

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return self.getter(instance)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Your *insert name* isn't a string!")
        if not value.strip():
            raise ValueError("Your *insert name* cannot be empty or blank!")
        return self.setter(instance, value)


def not_blank(attr):
    def decorator(cls):
        name = "__" + attr

        def getter(self):
            return getattr(self, name)

        def setter(self, value):
            setattr(self, name, value)

        setattr(cls, attr, NotBlank(getter, setter))
        return cls

    return decorator
