import re
from field import Field


class Phone(Field):
    """
    Класс для хранения номеров телефонов и их валидации
    """
    def __init__(self, value: str):
        if not self.validate_phone(value):
            raise ValueError("Телефонный номер должен содержать 10 цифр.")
        super().__init__(value)

    @staticmethod
    def validate_phone(phone: str) -> bool:
        return bool(re.fullmatch(r'\d{10}', phone))
