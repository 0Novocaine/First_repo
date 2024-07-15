import re
import sys
from collections import Counter
from tabulate import tabulate
from constants import VALIDATE_LOGS_LEVEL


def parse_log_line(line: str) -> dict:
    """
    Парсинг входящей строки с данными логов.
    В случае успеха возвращает словарь с ключами: "date","time","level","message"
    """
    match = re.match(r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)", line)
    if match:
        return {
            'date': match.group(1),
            'time': match.group(2),
            'level': match.group(3),
            'message': match.group(4)
        }
    return {}


def load_logs(file_path: str) -> list:
    """
    Принимает путь к файлу и парсит  строку при помощи функции parse_log_line().
    """
    log_data = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs_input = parse_log_line(line.strip())
                if logs_input:
                    log_data.append(logs_input)
    except FileNotFoundError:
        sys.exit(f"По заданному пути: \"{file_path}\" файл не обнаружен.")
    except Exception as e:
        sys.exit(f"Произошла ошибка при чтении файла: {e}")
    return log_data


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Фильтрует логи по уровню и возвращает сообщение, привязанное к указанному уровню логированния.
    """
    return [log['message'] for log in logs if log['level'] == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    """
    Возвращает уровень логирования и количество его совпадений.
    """
    levels = [log['level'] for log in logs]
    return dict(Counter(levels))


def display_log_counts(counts: dict):
    """
    Выводит количество записей по уровням логирования в виде таблицы.
    """
    headers = ["Уровень логирования", "Количество"]
    data = [(level, counts.get(level, 0)) for level in VALIDATE_LOGS_LEVEL]
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))


def display_filtered_logs(messages: list, level: str):
    """
    Выводит сообщения для выбранного уровня логирования.
    """
    print(f"\nЗаписи уровня {level.upper()}: ")
    print("=" * 30)
    for message in messages:
        print(message)
