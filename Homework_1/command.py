from enum import Enum


class Command(Enum):
    ADD = "add"
    CHANGE = "change"
    NAME = "name"
    ALL = "all"
    DELETE = "delete"
    DEL = "del"
    EXIT = "exit"
    HELP = "help"


COMMAND_MAP = {
    "add": Command.ADD,
    "change": Command.CHANGE,
    "name": Command.NAME,
    "all": Command.ALL,
    "delete": Command.DELETE,
    "exit": Command.EXIT,
    "del": Command.DEL,
    "help": Command.HELP
    }



