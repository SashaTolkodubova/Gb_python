import gb.scripts.lesson_three as lesson_three


def test_count_repeating_number():
    array_1 = [1, 2, 3, 4, 5]
    array_2 = [3, 2, 3, 4, 3]
    assert lesson_three.count_repeating_number(array_1, 3) == 1
    assert lesson_three.count_repeating_number(array_2, 3) == 3


def test_get_close_value_from_array():
    array_1 = [1, 2, 3, 4, 5]
    assert lesson_three.get_close_value_from_array(array_1, 6) == 5


def test_count_word_cost():
    assert lesson_three.count_word_cost('ноутбук') == 12
