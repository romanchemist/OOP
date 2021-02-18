from random import gauss


class CustomFloat:
    def __int__(self):
        return int(float(self))

    def __add__(self, other):
        if isinstance(other, CustomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) + other

    def __radd__(self, other):  # добавь к объекту справа "ПРАВЕЕ ОПЕРАТОРА"
        return self + other

    def __mul__(self, other):
        if isinstance(other, CustomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) * other

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        if isinstance(other, CustomFloat):    # RandomFloat
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) - other

    def __rsub__(self, other):
        return -(self - other)

    def __pow__(self, other, modulo=None):
        if isinstance(other, CustomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) ** other

    def __rpow__(self, other):
        return other ** float(self)

    def __floordiv__(self, other):    # целочисленное деление (x // y)
        if isinstance(other, CustomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) // other

    def __rfloordiv__(self, other):
        return other // float(self)

    def __truediv__(self, other):
        if isinstance(other, CustomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) / other

    def __rtruediv__(self, other):
        return other / float(self)

    def __mod__(self, other):    #  остаток от деления
        if isinstance(other, CustomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) % other

    def __rmod__(self, other):
        return other % float(self)


class RandomFloat(CustomFloat):    # с прибора показание генерирует
    def __init__(self, mu: float, /, *, sigma: float = 1.):    # float строго позиционно ставится, после него можно нестрого kw арг, после * строго kw (1)
        if not isinstance(mu, float) or not isinstance(sigma, float):
            raise TypeError
        self.mu = mu
        self.sigma = sigma

    def __float__(self):
        return gauss(self.mu, self.sigma)


class EpsilonFloat(CustomFloat):    # допустимая погрешность вводится + все операции сравнения
    def __init__(self, /, data, *, epsilon=1e-3):
        if isinstance(data, float) and isinstance(epsilon, float) or isinstance(data, RandomFloat) and isinstance(epsilon, float):
            if epsilon >= 0:
                self.data = data
                self.epsilon = epsilon
            else:
                raise ValueError
        else:
            raise TypeError


    def __float__(self):
        return self.data

    def __eq__(self, other):
        if not isinstance(other, (float, int, EpsilonFloat, RandomFloat)):
            raise TypeError
        else:
            if abs(self.data - other) < self.epsilon:
                print("Числа равны")    # ???
                # print("Value1 =", float(self.data), "Value2 =", float(other))    # ????
                # print(f"Числа равны. Value ~ {float(self.data)}")    # ???
                return abs(self.data - other) < self.epsilon  #, print(float(self.data))
            else:
                print("Числа не равны")
                # print("Value1 =", float(self.data), "Value2 =", float(other))    # ????
                return abs(self.data - other) < self.epsilon
                #
    def __lt__(self, other):
        if not isinstance(other, (float, int, EpsilonFloat, RandomFloat)):
            raise TypeError
        else:
            if self.data < other:
                return self.data < other
            else:
                return self.data < other
# Сравниваем два показания прибора
va1 = RandomFloat(10.)
va2 = RandomFloat(10.)
value1 = EpsilonFloat(10.105)    # один прибор здесь работает
value2 = EpsilonFloat(10.2)
print(value1 == value2)
print(value1 < value2)
#____________________________________________________________________
# print("Два показания равны? :", value1 == value2,". Value ~ " f' {value1}')
# e = EpsilonFloat()
# print(e == float(value))
