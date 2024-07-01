from datetime import datetime


date_input: str = input("Введите дату в следующем формате 'YYYY.MM.DD': ")


def get_days_from_today(date_string: str) -> str | int:
    try:
        input_date = datetime.strptime(date_string, "%Y.%m.%d").date()
    except ValueError as e:
        return f"Неверный формат даты: {e}"
    today_date = datetime.today().date()
    date_difference = (input_date - today_date).days
    return date_difference


# print(get_days_from_today(date_input))
