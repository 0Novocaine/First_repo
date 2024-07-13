from scripts import normalize_phone
from decorators import *


@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args
    contacts[name] = normalize_phone(phone)
    return "Контакт добавлен."


@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, phone = args
    if name in contacts:
        contacts[name] = normalize_phone(phone)
        return "Контакт обновлен."
    else:
        return "Такой контакт отсутствует."


@input_error
def show_phone(args: list, contacts: dict) -> str:
    name = args[0]
    if name in contacts:
        return f"У {name.capitalize()} следующий номер телефона: {contacts[name]}."
    else:
        return "Ошибка: Пользователь не найден."


@input_error
def show_all(contacts: dict) -> str:
    if not contacts:
        return "Контакты отсутствуют."
    contact_list = [f"{name.capitalize()}: {phone}" for name, phone in contacts.items()]
    return "\n".join(contact_list)
