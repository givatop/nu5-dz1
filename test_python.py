import math


def test_map():
    """ Проверка функции map на примере возведения
    элементов списка и кортежа во 2-ю степень """
    lst = [1, 2, 3, 4, 5]
    assert list(map(lambda x: x ** 2, lst)) == [x ** 2 for x in lst]
    assert tuple(map(lambda x: x ** 2, tuple(lst))) == tuple(x ** 2 for x in lst)


def test_filter():
    """ Проверка функции filter на примере отбора четных чисел """
    num = 10
    lst = [n for n in range(num)]
    even_lst = [n for n in range(num) if n % 2 == 0]

    assert list(filter(lambda n: n % 2 == 0, lst)) == even_lst


def test_sorted():
    """ Проверка функции sorted """
    lst = [5, 4, 3, 2, 1, 0, -1, -2, -100500, 0, .5]
    sorted_lst = [-100500, -2, -1, 0, 0, .5, 1, 2, 3, 4, 5]
    assert sorted(lst) == sorted_lst


def test_pi():
    """ Проверка числа пи из модуля math """
    assert math.pi - 3.14159265359 < 1e-8


def test_sqrt():
    """ Проверка функции math.sqrt """
    assert math.sqrt(0) == 0
    assert math.sqrt(1) == 1
    assert math.sqrt(4) == 2
    assert math.sqrt(9) == 3
    assert math.sqrt(16) == 4


def test_pow():
    """ Проверка функции math.pow """
    assert math.pow(100, 0) == 1
    assert math.pow(2, 2) == 4
    assert math.pow(4, .5) == 2


def test_hypot():
    """ Проверка math.hypot с помощью 1-й Пифагоровой тройки """
    assert math.hypot(3, 4) == 5
