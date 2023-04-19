# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


def sum_of_numbers(numbers):
    try:
        return sum_of_int_number(int(numbers))
    except Exception as ex:
        print(ex)


def sum_of_int_number(numbers):
    result_sum = 0
    number = numbers
    for _ in range(len(str(numbers))):
        result_sum += int(number % 10)
        number //= 10
    return result_sum


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10


def make_paper_cranes(sum_of_cranes):
    k_cranes = int((sum_of_cranes / 3) * 2)
    p_cranes = int((sum_of_cranes / 3) / 2)
    s_cranes = int((sum_of_cranes / 3) / 2)
    return p_cranes, k_cranes, s_cranes


# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
#
# 385916 -> yes
# 123456 -> no


def is_happy_ticket(ticket_number):
    try:
        num = int(ticket_number)
        num_str = str(num)
        left_half = num_str[:(len(num_str) // 2)]
        right_half = num_str[len(num_str) // 2:]
        if sum_of_numbers(left_half) == sum_of_numbers(right_half):
            return True
        else:
            return False
    except Exception as ex:
        print(ex)


# Задача 8: Требуется определить, можноp ли от шоколадки
# размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
#
# 3 2 4 -> yes
# xxx
# xxx
# 3 2 1 -> no

def is_possible_for_chocolate(rows, columns, bars):
    whole_variants = set()
    for row in range(1, rows):
        whole_variants.add((row, columns))
    for column in range(1, columns):
        whole_variants.add((rows, column))
    print(whole_variants)
    for r, c in whole_variants:
        if r * c == bars:
            return True
    return False
