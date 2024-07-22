from address_book import AddressBook
from record import Record
from name import Name
from functions import parse_input, get_command_help
from command import *


def main():
    """
    Основная функция для работы с адресной книгой. Считывает команды пользователя и выполняет соответствующие действия.
    """
    address_book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Введите команду: ")
        command, args = parse_input(user_input)
        match command:

            case Command.EXIT:
                print("Good bye!")
                break

            case Command.ADD:
                if len(args) < 2:
                    print("Введите имя пользователя и его контактные данные.")
                    continue
                record = address_book.find(args[0])
                if not record:
                    record = Record(Name(args[0]))
                for phone in args[1:]:
                    record.add_phone(phone)
                address_book.add_record(record)

            case Command.CHANGE:
                if len(args) < 3:
                    print("Введите имя пользователя и два номера телефона: старый и новый.")
                    continue
                phone_to_change = address_book.find(args[0])
                if not phone_to_change:
                    print(f"Контакт с именем {args[0]} не найден.")
                    continue
                phone_to_change.edit_phone(args[1], args[2])
                print(f"Номер телефона {args[1]} для контакта {args[0]} изменен на {args[2]}.")

            case Command.NAME:
                if len(args) < 1:
                    print("Введите имя пользователя.")
                    continue
                record = address_book.find(args[0])
                print(record)

            case Command.DELETE:
                if len(args) < 1:
                    print("Введите имя пользователя.")
                    continue
                if address_book.delete(args[0]):
                    address_book.delete(args[0])
                    print(f"Контакт с именем {args[0]} удален.")
                else:
                    print(f"Контакт с именем {args[0]} не найден.")

            case Command.DEL:
                if len(args) < 1:
                    print("Введите номер телефона.")
                    continue
                phone_to_delete = address_book.find(args[0])
                if not phone_to_delete:
                    print(f"Контакт с именем {args[0]} не найден.")
                    continue
                phone_to_delete.delete_phone(args[1])
                print(f"Номер телефона {args[1]} для контакта {args[0]} удален.")

            case Command.ALL:
                print(address_book)

            case Command.HELP:
                print("Доступные команды. " + get_command_help())
            case _:
                print( "Неверная команда. " + get_command_help())


if __name__ == "__main__":
    main()

"""
Шаблоны

1. Добавление нового контакта
Формат команды: add <Имя> <Телефон1> [Телефон2] [Телефон3] ...
Примеры:
add John 0982332323 0981111111
add John 0963443434
add Poni 0983423434 0912332323

2. Поиск контакта по имени
Формат команды: name <Имя>
Примеры:
name Poni

3. Изменение номера телефона
Формат команды: change <Имя> <СтарыйТелефон> <НовыйТелефон>
Примеры:
change John 0982332323 0999999999
change Poni 0983423434 0900000000
4. Удаление номера телефона
Формат команды: del <Имя> <Телефон>
Примеры:
del John 0981111111
del Poni 0912332323

5. Удаление контакта
Формат команды: delete <Имя>
Примеры:
delete John
delete Poni

6. Вывод всех контактов
Формат команды: all
Примеры:
all

7. Получение справки по командам
Формат команды: help
Примеры:
help
"""