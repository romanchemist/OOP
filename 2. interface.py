# Создадим класс который эмитирует работу прибора
from random import gauss


class RandomFloat:    # создали класс. называем с большой буквы классы. перед классом 2 строки пустые
    def __init__(self, mu: float, /, *, sigma: float = 1.):    # self - такая перемен которая дает возможность работать с объектом внутри функции
           # self позволяет обратиться к объекту (1-ая переменная в функциях внутри класса,слово мб любое
        if not isinstance(mu, float) or not isinstance(sigma, float):    # если атрибут не является типом str
            raise TypeError   # выдаст ошибку и код упадет напишет тип ошибки. TypeError - класс ошибки. Если скобки то это объект класса
        self.mu = mu
        self.sigma = sigma

    def __float__(self):    # 1 СТАНДАРТНЫЙ ИНТЕРФЕЙС. Получаем случайное число в данный момент (рядом с 10)
        return gauss(self.mu, self.sigma)

    def __int__(self):
        return int(float(self))

    def __add__(self, other):    # Сложение
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) + other

    # def __radd__(self, other):    # добавь к объекту справа "ПРАВЕЕ ОПЕРАТОРА"
    #     return self + other

    def __mul__(self, other):
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) * other

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) - other

    def __rsub__(self, other):
        return -(self - other)
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ HW @@@@@@@@@@@@@@@@@@@@@@@@@

    def __pow__(self, other, modulo=None):
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) ** other

    def __rpow__(self, other):
        return other ** float(self)

    def __floordiv__(self, other):
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) // other

    def __rfloordiv__(self, other):
        return other // float(self)

    def __truediv__(self, other):
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) / other

    def __rtruediv__(self, other):
        return other / float(self)

    def __mod__(self, other):
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) % other

    def __rmod__(self, other):
        return other % float(self)



    # def __iadd__(self, other):
    #     if isinstance(other, RandomFloat):
    #         other = float(other)
    #     elif not isinstance(other, (float, int)):
    #         raise TypeError
    #     elif not float(self) != other:
    #         raise ValueError
    #     self.x += other
    #     return self

#     LECTURE 3.
#  i-операторы
    def __radd__(self, other):
        return self + other

    # def __iadd__(self, other):
    #     self.mu += other
    #     return self


# c = (RandomFloat(10.),)
# print(c, c[0].mu)
# try:
#     c[0] += 1
# except:
#     pass
# print(c, c[0].mu)
# print(c, id(c))
# c += 1
# print(float(c))
# print(int(c))
# print(float(c))
# print(c + 2)
# print(c + c)
# print(1 + c) без radd не можем
# print(1 + c)
# print(c * 2)
# print(2 * c)
# print(c - c)
# print(c - 10)
# print(25 - c)
# @@@
# print(c ** 4)
# print(4 ** c)
# print(c // 2)
# print(2 // c)
# print(c / 3)
# print(3 / c)
# print(c % 4)

    def __iadd__(self, other):    # не меняет с типа объекта на просто флоат число

        if isinstance(other, RandomFloat):
            return RandomFloat(self.mu + other.mu)
        elif not isinstance(other, float):
            raise TypeError
        return RandomFloat(self.mu + other)

c = RandomFloat(10.)
print(c)
c += 1.
print(c)
