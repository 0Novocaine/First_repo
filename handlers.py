from typing import List
from address_book import AddressBook
from record import Record
from name import Name
from decorators import *


@input_error
def add_contact(address_book: AddressBook, args: List[str]):
    """
    Добавляет новый контакт или обновляет существующий с указанным именем и телефонами.
    :param address_book:
    :param args:
    :return:
    """
    if len(args) < 2:
        raise ValueError("Введите имя пользователя и его контактные данные.")
    record = address_book.find(args[0])
    if not record:
        record = Record(Name(args[0]))
    for phone in args[1:]:
        record.add_phone(phone)
    address_book.add_record(record)
    return f"Контакт {args[0]} добавлен/обновлен."


@input_error
def change_phone(address_book: AddressBook, args: List[str]):
    """
    Изменяет телефонный номер у существующего контакта
    :param address_book:
    :param args:
    :return:
    """
    if len(args) < 3:
        raise ValueError("Введите имя пользователя, старый номер и новый номер телефона.")
    record = address_book.find(args[0])
    if not record:
        raise KeyError(f"Контакт с именем {args[0]} не найден.")
    record.edit_phone(args[1], args[2])
    return f"Номер телефона для контакта {args[0]} изменен с {args[1]} на {args[2]}."


@input_error
def show_contact(address_book: AddressBook, args: List[str]):
    """
    Возвращает контакт по заданному имени.
    :param address_book:
    :param args:
    :return:
    """
    if len(args) < 1:
        raise ValueError("Введите имя пользователя.")
    record = address_book.find(args[0])
    if not record:
        raise KeyError(f"Контакт с именем {args[0]} не найден.")
    return str(record)


@input_error
def delete_contact(address_book: AddressBook, args: List[str]):
    """
    Удаляет контакт по имени
    :param address_book:
    :param args:
    :return:
    """
    if len(args) < 1:
        raise ValueError("Введите имя пользователя.")
    if address_book.delete(args[0]):
        return f"Контакт с именем {args[0]} удален."
    else:
        raise KeyError(f"Контакт с именем {args[0]} не найден.")


@input_error
def delete_phone(address_book: AddressBook, args: List[str]):
    """
    удаляет телефонный номер у контакта.
    :param address_book:
    :param args:
    :return:
    """
    if len(args) < 2:
        raise ValueError("Введите имя пользователя и номер телефона.")
    record = address_book.find(args[0])
    if not record:
        raise KeyError(f"Контакт с именем {args[0]} не найден.")
    record.delete_phone(args[1])
    return f"Номер телефона {args[1]} для контакта {args[0]} удален."


@input_error
def add_birthday(address_book: AddressBook, args: List[str]):
    """
    Добавляет дату рождения к контакту
    :param address_book:
    :param args:
    :return:
    """
    if len(args) < 2:
        raise ValueError("Введите имя пользователя и дату рождения в формате DD.MM.YYYY.")
    record = address_book.find(args[0])
    if not record:
        raise KeyError(f"Контакт с именем {args[0]} не найден.")
    record.add_birthday(args[1])
    return f"Дата рождения {args[1]} добавлена для контакта {args[0]}."


@input_error
def show_birthday(address_book: AddressBook, args: List[str]):
    """
    Показывает дату рождения контакта
    :param address_book:
    :param args:
    :return:
    """
    if len(args) < 1:
        raise ValueError("Введите имя пользователя.")
    record = address_book.find(args[0])
    if not record:
        raise KeyError(f"Контакт с именем {args[0]} не найден.")
    if not record.birthday:
        return f"День рождения для контакта с именем {args[0]} не найден."
    return f"Дата рождения для контакта {args[0]}: {record.birthday.value}"


@input_error
def show_all_birthdays(address_book: AddressBook):
    """
    Показывает все дни рождения на 7 дней вперде
    :param address_book:
    :return:
    """
    upcoming_birthdays = address_book.get_upcoming_birthdays()
    if upcoming_birthdays:
        result = "Предстоящие дни рождения:\n"
        result += "\n".join(str(record) for record in upcoming_birthdays)
        return result
    else:
        return "Нет предстоящих дней рождения в течение недели."
