class NotBlank:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise ValueError("Your *insert name* isn't a string!")
        if not value.strip():
            raise ValueError("Your *insert name* cannot be empty or blank!")
        self.value = value


def not_blank(attr):
    def decorator(cls):
        setattr(cls, attr, NotBlank())
        return cls

    return decorator