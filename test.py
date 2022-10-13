from main import convertor

def test_value_choose():
    assert convertor().value_choose(1) == ('Миля', 'Метр', 1)
    assert convertor().value_choose(2) == ('Ярд', 'Метр', 2)
    assert convertor().value_choose(3) == ('Фунт', 'Килограмм', 3)
    assert convertor().value_choose(4) == ('Стоун', 'Килограмм', 4)
    assert convertor().value_choose(5) == ('Кубический ярд', 'Кубометр', 5)
    assert convertor().value_choose(11) == ('Сажень', 'Метр', 11)
    assert convertor().value_choose(22) == ('Аршин', 'Метр', 22)
    assert convertor().value_choose(33) == ('Пуд', 'Килограмм', 33)
    assert convertor().value_choose(44) == ('Берковец', 'Килограмм', 44)
    assert convertor().value_choose(55) == ('Верст', 'Метр', 55)
    assert convertor().value_choose(25) == ('Ошибка')

def test_quantity():
    assert convertor().quantity(25) == 25
    assert convertor().quantity(123) == 123
    assert convertor().quantity('ABC') == 'Ошибка'

def test_calculate_from_100():
    convertor().quantity(100)
    convertor().value_choose(1)
    assert convertor().calculate() == 0.062
    convertor().value_choose(2)
    assert convertor().calculate() == 91
    convertor().value_choose(3)
    assert convertor().calculate() == 45
    convertor().value_choose(4)
    assert convertor().calculate() == 635
    convertor().value_choose(5)
    assert convertor().calculate() == 76
    convertor().value_choose(11)
    assert convertor().calculate() == 213
    convertor().value_choose(22)
    assert convertor().calculate() == 71
    convertor().value_choose(33)
    assert convertor().calculate() == 16
    convertor().value_choose(44)
    assert convertor().calculate() == 16380
    convertor().value_choose(55)
    assert convertor().calculate() == 106680