from math import ceil


class Kletka:
    def __init__(self, param):
        self.param = int(param)

    def __str__(self):
        if self.param >= 0:
            return f'{self.param}'
        else:
            return 'Получилось отрицательное число!'

    def __add__(self, other):
        return Kletka(self.param + other.param)

    def __sub__(self, other):
        return Kletka(self.param - other.param)

    def __mul__(self, other):
        return Kletka(self.param * other.param)

    def __truediv__(self, other):
        return Kletka(self.param // other.param)

    def make_order(self, p):
        s = p
        string = ''
        for i in range(ceil(self.param / p)):
            if self.param % p == 0:
                s = p
            elif i == ceil(self.param / p) - 1:
                s = self.param % p
            string += '*' * s + '\n'

        return string


try:
    k_1 = Kletka(int(input('Введите количество ячеек первой клетки: ')))
    k_2 = Kletka(int(input('Введите количество ячеек второй клетки: ')))
    print(f'k_1 + k_2 = {k_1 + k_2}')
    print(f'k_2 - k_1 = {k_2 - k_1}')
    print(f'k_1 - k_2 = {k_1 - k_2}')
    print(f'k_1 * k_2 = {k_1 * k_2}')
    print(f'k_2 / k_1 = {k_2 / k_1}')
    print(k_2.make_order(int(input('Введите количество ячеек в ряду для второй клетки: '))))
except:
    print('Вводите только натуральные числа: ')
