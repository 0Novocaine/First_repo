from dataclasses import dataclass, field
from name import Name
from phone import Phone


@dataclass
class Record:
    name: Name
    phones: list = field(default_factory=list)

    def add_phone(self, phone: str):
        if Phone.validate_phone(phone):
            if not self.find_phone(phone):
                self.phones.append(Phone(phone))
            else:
                print(f"Телефон {phone} уже существует.")
        else:
            print(f"Неверный формат номера: {phone}. Номер телефон должен содержать 10 цифр.")

    def find_phone(self, phone: str):
        for match_phone in self.phones:
            if match_phone.value == phone:
                return match_phone
        return None

    def delete_phone(self, phone: str):
        phone_to_delete = self.find_phone(phone)
        if phone_to_delete:
            self.phones.remove(phone_to_delete)

    def edit_phone(self, old_phone: str, new_phone: str):
        phone_to_edit = self.find_phone(old_phone)
        if phone_to_edit:
            self.phones.remove(phone_to_edit)
            self.add_phone(new_phone)

    def __str__(self) -> str:
        phones_str = ', '.join(str(p) for p in self.phones)
        return f"Имя пользователя: {self.name.value.capitalize()}, номер телефона: {phones_str}"