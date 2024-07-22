from typing import List
from command import *


def to_lowercase(strings: List[str]) -> List[str]:
    return [s.lower() for s in strings]


def parse_input(user_input: str) -> tuple[str, List[str]]:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    args = [arg.lower() for arg in args]
    command = COMMAND_MAP.get(cmd, None)
    return command, args


def get_command_help():
    command_descriptions = {
        Command.ADD: "добавить пользователя",
        Command.CHANGE: "изменить телефон пользователя",
        Command.NAME: "найти пользователя по имени",
        Command.ALL: "показать все контакты",
        Command.DELETE: "удалить пользователя",
        Command.DEL: "удалить номер телефона",
        Command.EXIT: "выйти из программы",
        Command.HELP: "доступные команды"
    }
    help_message = " Введите:\n"
    for command in Command:
        description = command_descriptions.get(command, "Нет описания")
        help_message += f"  {command.value} - {description}\n"
    return help_message

