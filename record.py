from dataclasses import dataclass, field
from typing import Optional, List
from phone import Phone
from name import Name
from birthday import Birthday


@dataclass
class Record:
    """
    Класс для хранения информации про контакт, включая имя, список телефонов и день рождения
    """
    name: Name
    phones: List[Phone] = field(default_factory=list)
    birthday: Optional[Birthday] = None

    def add_phone(self, phone: str):
        """
        Добавляет новый номер телефона, если он валидный и отсутствует в списке
        """
        if Phone.validate_phone(phone):
            if not self.find_phone(phone):
                self.phones.append(Phone(phone))
            else:
                print(f"Телефон {phone} уже существует.")
        else:
            print(f"Неверный формат номера: {phone}. Номер телефона должен содержать 10 цифр.")

    def find_phone(self, phone: str):
        """
        Ищет номер телефона в списке телефонов записи.
        """
        for match_phone in self.phones:
            if match_phone.value == phone:
                return match_phone
        return None

    def delete_phone(self, phone: str):
        """
        Удаляет номер телефона из записи.
        """
        phone_to_delete = self.find_phone(phone)
        if phone_to_delete:
            self.phones.remove(phone_to_delete)

    def edit_phone(self, old_phone: str, new_phone: str):
        """
        Редактирование номера телефона.
        """
        phone_to_edit = self.find_phone(old_phone)
        if phone_to_edit:
            self.phones.remove(phone_to_edit)
            self.add_phone(new_phone)

    def add_birthday(self, birthday: str):
        """
        Добавляет день рождения к записи
        """
        self.birthday = Birthday(birthday)

    def __str__(self) -> str:
        phones_str = ', '.join(str(p) for p in self.phones)
        birthday_str = f", день рождения: {self.birthday.value}" if self.birthday else ""
        return f"Имя пользователя: {self.name.value.capitalize()}, номер телефона: {phones_str}{birthday_str}"


