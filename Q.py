from main import *
from N import *
from Z import *
class Q():
    def __init__(self, num, denum=N(1)):
        if isinstance(num, N):
            self.num = num.toZ()
        elif isinstance(num, Z):
            self.num = num
        else:
            self.num = Z(num)

        if isinstance(denum, Z):
            if denum.sign:
                self.num = self * Z(-1)
            self.denum = abs(denum).toN()
        elif isinstance(denum, N):
            self.denum = denum
        else:
            self.denum = N(denum)

        # self.num = num # Числитель.
        # self.denum = denum  # Знаменатель.
        if self.denum == N(0):
            raise ZeroDivisionError("Divided by zero")

    def __str__(self):
        res = str(self.num) + (
                    str(self.denum) != '1' and "/{}".format(self.denum) or "")  # если знаменатель == 1, не пишется
        # res = "{}/{}".format(self.num, self.denum)
        return res

    # "Reduce" (сокращение дроби).
    def red(self):
        gcd = self.denum.gcd(abs(self.num).toN())
        num = self.num / gcd
        denum = self.denum / gcd
        return Q(num, denum)

    # Можно ли представить дробь в виде целого числа.
    def isZ(self):
        if self.num % self.denum == Z(0):
            return True
        else:
            return False

    # Перевод числа в N(), если это возможно.
    def toN(self):
        if (self.isZ() and (self.num // self.denum >= Z(0))):
            return N(str(self.num // self.denum))
        else:
            raise RuntimeError("Z", str(self), "cannot be presented as N.")

    # Перевод числа в Z(), если это возможно.
    def toZ(self):
        if (self.isZ()):
            return Z(str(self.num // self.denum))
        else:
            raise RuntimeError("Z", str(self), "cannot be presented as N.")

    # Перевод числа в poly().
    def toPoly(self):
        return poly(self)

    
    # Перегрузка операторов.
    
    def __add__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '+')

        denum = self.denum * other.denum
        num = self.num * other.denum + self.denum * other.num
        return Q(num, denum).red()

    def __sub__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '-')

        denum = self.denum * other.denum
        tmp = self.num * other.denum
        tmp2 = self.denum * other.num
        num = tmp - tmp2
        return Q(num, denum).red()

    def __mul__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '*')
        num = self.num * other.num
        denum = self.denum * self.denum
        return Q(num, denum).red()

    def __truediv__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '/')
        num = self.num * other.denum
        denum = self.denum * other.num
        return Q(num, denum).red()

    # хз, как это будет работать
    def __floordiv__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '//')
        tmp = self / other
        res = tmp.num // tmp.denum
        return res

    # не уверен, что деление с остатком имеет отношение к дробям, но пусть будет
    def __mod__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '%')
        mod = self - (self // other) * other
        return mod

    def __lt__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '<')
        return self.num * other.denum < other.num * self.denum

    def __le__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '<=')
        return self.num * other.denum <= other.num * self.denum

    def __eq__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '==')
        return self.num * other.denum == other.num * self.denum

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other
