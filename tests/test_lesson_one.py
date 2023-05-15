import gb.scripts.lesson_one as lesson_one
import gb.scripts.lesson_four as lesson_four
import gb.scripts.lesson_five as lesson_five


def test_sum_of_numbers():
    assert lesson_one.sum_of_numbers(100) == 1
    assert lesson_one.sum_of_numbers(123) == 6
    assert lesson_one.sum_of_numbers('100') == 1
    assert lesson_one.sum_of_numbers('123') == 6


def test_make_paper_cranes():
    assert lesson_one.make_paper_cranes(6) == (1, 4, 1)
    assert lesson_one.make_paper_cranes(24) == (4, 16, 4)
    assert lesson_one.make_paper_cranes(60) == (10, 40, 10)


def test_is_happy_ticket():
    assert lesson_one.is_happy_ticket(385916)
    assert not lesson_one.is_happy_ticket(123456)


def test_is_possible_for_chocolate():
    assert lesson_one.is_possible_for_chocolate(3, 2, 4)
    assert not lesson_one.is_possible_for_chocolate(3, 2, 1)


def test_get_uniq_numbers():
    ar_1 = [9, 2, 6, 0, 3, 9]
    ar_2 = [4, 2, 0, 1, 9, 5, 4]
    assert lesson_four.get_uniq_numbers(ar_1, ar_2) == [0, 2, 9]


def test_count_berry():
    bushs = [43, 2, 11, 23, 44]
    assert lesson_four.count_berry(bushs) == 110


def test_recursin_pow():
    assert lesson_five.recursin_pow(3, 5) == 243
    assert lesson_five.recursin_pow(2, 3) == 8


def test_reqursive_summ():
    assert lesson_five.reqursive_summ(2, 2) == 4
