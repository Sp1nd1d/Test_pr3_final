value1 = ''
value2 = ''
option = 0
quantity1 = 0
answer = 0
print('1. Мили в метры', '2. Ярды в метры', '3. Фунты в килограммы', '4. Стоуны в килограммы', '5. Кубические ярды в кубометры', sep='\n')
print('11. Сажени в метры', '22. Аршины в метры', '33. Пуды в килограммы', '44. Берковцы в килограммы', '55. Верста в метры', sep='\n')


class convertor:
    def value_choose(self, x):
        global value1, value2, option
        if x == 1:
            value1 = 'Миля'
            value2 = 'Метр'
            option = 1
            return value1, value2, option
        elif x == 2:
            value1 = 'Ярд'
            value2 = 'Метр'
            option = 2
            return value1, value2, option
        elif x == 3:
            value1 = 'Фунт'
            value2 = 'Килограмм'
            option = 3
            return value1, value2, option
        elif x == 4:
            value1 = 'Стоун'
            value2 = 'Килограмм'
            option = 4
            return value1, value2, option
        elif x == 5:
            value1 = 'Кубический ярд'
            value2 = 'Кубометр'
            option = 5
            return value1, value2, option
        elif x == 11:
            value1 = 'Сажень'
            value2 = 'Метр'
            option = 11
            return value1, value2, option
        elif x == 22:
            value1 = 'Аршин'
            value2 = 'Метр'
            option = 22
            return value1, value2, option
        elif x == 33:
            value1 = 'Пуд'
            value2 = 'Килограмм'
            option = 33
            return value1, value2, option
        elif x == 44:
            value1 = 'Берковец'
            value2 = 'Килограмм'
            option = 44
            return value1, value2, option
        elif x == 55:
            value1 = 'Верст'
            value2 = 'Метр'
            option = 55
            return value1, value2, option
        else:
            return 'Ошибка'

    def quantity(self, x):
        global quantity1
        try:
            quantity1 = float(x)
            return quantity1
        except:
            return 'Ошибка'

    def calculate(self):
        global option, quantity1, answer, value1, value2
        if option == 1:
            answer = quantity1 * 0.00062
            return answer
        elif option == 2:
            answer = quantity1 * 0.91
            return answer
        elif option == 3:
            answer = quantity1 * 0.45
            return answer
        elif option == 4:
            answer = quantity1 * 6.35
            return answer
        elif option == 5:
            answer = quantity1 * 0.76
            return answer
        if option == 11:
            answer = quantity1 * 2.13
            return answer
        elif option == 22:
            answer = quantity1 * 0.71
            return answer
        elif option == 33:
            answer = quantity1 * 0.16
            return answer
        elif option == 44:
            answer = quantity1 * 163.8
            return answer
        elif option == 55:
            answer = quantity1 * 1066.8
            return answer


print(convertor().value_choose(1))
print(convertor().quantity(100))
print(convertor().calculate())
