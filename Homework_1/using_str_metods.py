import pathlib


def total_salary(path: pathlib) -> tuple | None:
    try:
        with open(path, "r", ) as file:
            lines = file.readlines()
            total_amount = 0
            quantity = 0
            average = 0
            for line in lines:
                name, salary = line.split(',')
                total_amount += int(salary.strip())
                quantity += 1
                average = total_amount / quantity
            return total_amount, average
    except FileNotFoundError:
        print(f"There is no such file at this path: {path}")
        return None


current_dir = pathlib.Path(__file__).parent / "data.txt"
total, average = (total_salary(current_dir))
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
