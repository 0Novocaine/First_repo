import re
from typing import Callable

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def generator_numbers(text: str):
    numbers = re.findall(r"\d+.\d+", text)
    for num in numbers:
        yield float(num)


def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))


print(sum_profit(text, generator_numbers))