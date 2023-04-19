# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной
# и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
#


def turn_coin(coin_heads, coin_tails):
    if coin_heads >= coin_tails:
        return coin_tails
    else:
        return coin_heads


# Задача 12: Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
#


def get_number(s, p):
    for i in range(s):
        first_number = i
        for n in range(s):
            second_number = n
            if (first_number + second_number == s and
                    first_number * second_number == p):
                return first_number, second_number


# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
def get_powers_of_two(n):
    result_list = list()
    number = 2
    power = 0
    while True:
        result = pow(number, power)
        if result > n:
            break
        result_list.append(result)
        power += 1
    return result_list
