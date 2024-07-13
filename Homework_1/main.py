def caching_fibonacci():
    # Создаем пустой словарь для хранения значений чисел Фибоначи.
    cache = {}

    def fibonacci(number):
        if number <= 0:
            return 0
        elif number == 1:
            return 1
        # Выход из рекурсии в случае, если number присутствует в cache.
        if number in cache.keys():
            return cache[number]
        # Вычисляем число Фибоначи при помощи рекурсии, сохраняем результат в кэше.
        cache[number] = fibonacci(number - 1) + fibonacci(number - 2)
        return cache[number]
    # Возвращаем внутреннюю функцию fibonacci, чтобы её можно было использовать с кэшированием.
    return fibonacci


fibonacci = caching_fibonacci()
print(fibonacci(50))
print(fibonacci(20))
print(fibonacci(40))
