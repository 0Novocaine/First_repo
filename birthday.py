from field import Field
from datetime import date, datetime


class Birthday(Field):
    """
    Класс для хранения и валидации дней рождения
    """
    def __init__(self, value: str):
        if not self.validate_birthday(value):
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)

    @staticmethod
    def validate_birthday(birthday: str) -> bool:
        try:
            datetime.strptime(birthday, "%d.%m.%Y")
            return True
        except ValueError:
            return False

    def to_date(self) -> date:
        return datetime.strptime(self.value, "%d.%m.%Y").date()
