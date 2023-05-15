# Задача 26:  Напишите программу,
# которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


def recursin_pow(number_1, number_2):
    def inner(num_1, num_2):
        if num_2 == 0:
            return 1
        return inner(number_1, num_2 - 1) * number_1
    return inner(number_1, number_2)


# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4


def reqursive_summ(number_1, number_2):
    def inner(num_1, num_2):
        if num_1 == 0 and num_2 == 0:
            return 0
        elif num_1 == 0 and num_2 != 0:
            return inner(num_1, num_2 - 1) + 1
        elif num_1 != 0 and num_2 == 0:
            return inner(num_1 - 1, num_2) + 1
        else:
            return inner(num_1 - 1, num_2 - 1) + 1 + 1
    return inner(number_1, number_2)
