from datetime import timedelta, date
from collections import UserDict
from typing import Optional, List
from record import Record


class AddressBook(UserDict):
    """
    Класс для хранения и управления записями
    """
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name, None)

    def delete(self, name: str) -> bool:
        if name in self.data:
            del self.data[name]
            return True
        return False

    def get_upcoming_birthdays(self, days: int = 7) -> List[Record]:
        """
        Возвращает список записей с предстоящими днями рождения в течение заданного количества дней
        """
        upcoming_birthdays = []
        today = date.today()
        end_date = today + timedelta(days=days)
        for record in self.data.values():
            if record.birthday:
                birthday_date = record.birthday.to_date().replace(year=today.year)
                if today <= birthday_date <= end_date:
                    upcoming_birthdays.append(record)
        return upcoming_birthdays

    def __str__(self) -> str:
        return '\n'.join(str(record) for record in self.data.values())
