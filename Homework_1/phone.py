import re
from field import Field


class Phone(Field):
    def __init__(self, value: str):
        if not self.validate_phone(value):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

    @staticmethod
    def validate_phone(phone: str) -> bool:
        return bool(re.fullmatch(r'\d{10}', phone))