from handlers import *
from functions import *


def main():
    """
    Основная функция для работы с адресной книгой. Считывает команды пользователя и выполняет соответствующие действия.
    """
    address_book = AddressBook()
    print("Бот-ассистент приветствует вас!")
    while True:
        user_input = input("Введите команду: ")
        if not user_input:
            print("Пустая строка не является командой. Введите команду.")
            continue
        command, args = parse_input(user_input)
        if command is None:
            print("Неверная команда. " + get_command_help())
            continue
        match command:
            case Command.EXIT:
                print("Пока!")
                break
            case Command.ADD:
                print(add_contact(address_book, args))
            case Command.CHANGE:
                print(change_phone(address_book, args))
            case Command.NAME:
                print(show_contact(address_book, args))
            case Command.DELETE:
                print(delete_contact(address_book, args))
            case Command.DEL:
                print(delete_phone(address_book, args))
            case Command.ADD_BIRTHDAY:
                print(add_birthday(address_book, args))
            case Command.SHOW_BIRTHDAY:
                print(show_birthday(address_book, args))
            case Command.SHOW_ALL_BIRTHDAYS:
                print(show_all_birthdays(address_book))
            case Command.ALL:
                print(address_book)
            case Command.HELP:
                print("Доступные команды:\n" + get_command_help())
            case _:
                print("Неверная команда. " + get_command_help())


if __name__ == "__main__":
    main()
