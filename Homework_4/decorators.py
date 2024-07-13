def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Ошибка: Пользователь не найден."
        except ValueError:
            return "Ошибка: Ожидается имя пользователя и номер телефона."
        except IndexError:
            return "Ошибка: Введите имя пользователя, чей телефон вы хотите узнать."

    return inner
