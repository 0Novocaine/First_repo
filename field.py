class Field:
    """
    Базовый класс для полей записи (имя, телефон)
    """
    def __init__(self, value: str):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)