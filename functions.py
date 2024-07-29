from typing import Optional, List
from command import Command, COMMAND_MAP



def parse_input(user_input: str) -> tuple[Optional[Command], List[str]]:
    """
    Парсит вводные данные на команду и аргументы.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    args = [arg.lower() for arg in args]
    command = COMMAND_MAP.get(cmd, None)
    return command, args


def to_lowercase(strings: List[str]) -> List[str]:
    """
    Преобразует все строки в списке в нижний регистр.
    """
    return [s.lower() for s in strings]


def get_command_help() -> str:
    """
    Возвращает строку с описанием всех доступных команд.
    """
    command_descriptions = {
        Command.ADD: "добавить пользователя",
        Command.CHANGE: "изменить телефон пользователя",
        Command.NAME: "найти пользователя по имени",
        Command.ALL: "показать все контакты",
        Command.ADD_BIRTHDAY: "добавить день рождения",
        Command.SHOW_BIRTHDAY: "показать дату дня рождения",
        Command.SHOW_ALL_BIRTHDAYS: "показать все дни рождения",
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

