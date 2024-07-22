from field import Field


class Name(Field):
    """
    Класс для хранения имени контактов
    """
    def __init__(self, value: str):
        super().__init__(value)
        if not self.value:
            raise ValueError("Name cannot be empty")