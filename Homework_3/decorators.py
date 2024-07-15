import sys
from constants import VALIDATE_LOGS_LEVEL


def validate_log_level(func):
    def inner(*args, **kwargs):
        if len(sys.argv) > 2:
            log_level = sys.argv[2].upper()
            if log_level not in VALIDATE_LOGS_LEVEL:
                sys.exit(
                    f"Ошибка: Недопустимый уровень логирования '{log_level}'. Допустимые уровни: {', '.join(VALIDATE_LOGS_LEVEL)}.")
        return func(*args, **kwargs)
    return inner
