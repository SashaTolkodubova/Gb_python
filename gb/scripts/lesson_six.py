# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithmetic_progression(first_element,
                           common_difference,
                           quantity_elements):
    result = list()
    for i in range(1, quantity_elements + 1):
        element = first_element + (i - 1) * common_difference
        result.append(element)
    return result


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def indexes_range(array, min_value, max_value):
    result = list()
    for i in range(len(array)):
        if min_value <= array[i] <= max_value:
            result.append(i)
    return result
