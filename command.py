from enum import Enum


class Command(Enum):
    """
    Перечисление доступных команд для управления адресной книгой.
    """
    ADD = "add"
    CHANGE = "change"
    NAME = "name"
    ALL = "all"
    DELETE = "delete"
    DEL = "del"
    ADD_BIRTHDAY = "add-birthday"
    SHOW_BIRTHDAY = "show-birthday"
    SHOW_ALL_BIRTHDAYS = "birthdays"
    EXIT = "exit"
    HELP = "help"


COMMAND_MAP = {
    "add": Command.ADD,
    "change": Command.CHANGE,
    "name": Command.NAME,
    "all": Command.ALL,
    "delete": Command.DELETE,
    "add-birthday": Command.ADD_BIRTHDAY,
    "show-birthday": Command.SHOW_BIRTHDAY,
    "birthdays": Command.SHOW_ALL_BIRTHDAYS,
    "del": Command.DEL,
    "exit": Command.EXIT,
    "help": Command.HELP
}