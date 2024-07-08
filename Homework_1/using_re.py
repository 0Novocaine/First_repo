import pathlib
import re


def total_salary(path: pathlib) -> tuple | None:
    try:
        with open("data.txt", "r") as file:
            lines = file.read()
            pattern = r"([A-Za-z\s]+),(\d+)"
            format_lines = re.findall(pattern, lines)
            total_amount = 0
            quantity = 0
            for name, value in format_lines:
                total_amount += int(value)
                quantity += 1
                average = total_amount / quantity if quantity else "No values"
            return average, total_amount
    except FileNotFoundError:
        print(f"There is no such file at this path: {path}")
        return None


current_dir = pathlib.Path(__file__).parent / "data.txt"
total, average = (total_salary(current_dir))
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")