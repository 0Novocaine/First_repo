def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Ошибка: {e}"
        except ValueError as e:
            return f"Ошибка: {e}"
        except IndexError:
            return "Ошибка: Неправильный формат ввода."
        except Exception as e:
            return f"Ошибка: {e}"
    return inner
