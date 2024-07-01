import random


def get_numbers_ticket(quantity, min_int=1, max_int=1000):
    if not all(isinstance(x, int) for x in [min, max, quantity]):
        return [], ("Значение должно быть числом (int)")
    if 1 > min_int or max_int > 1000:
        return [], ("Значения должны быть в диапазоне от 1 до 1000")
    if quantity > (max_int - min_int):
        return [], ("Диапазон значений слишком мал для заданного количества уникальных чисел")
    list_of_winners = random.sample(range(min_int, max_int), quantity)
    return list_of_winners.sort()


# print(get_numbers_ticket(2, "l", 222))
