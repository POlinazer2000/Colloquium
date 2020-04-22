class Z():
    # Инициализация класса.
    # Здесь: списку "Z.digits" присваивается значение первого аргумента (тип: int).
    # Пример: "Z( -1234 )" создаст объект класса "Z()" с "digits = [1, 2, 3, 4]" и "sign = True".
    def __init__(self, digit):
        try:
            digit = str(
                int(str(digit).replace('[', '').replace(']', '').replace(' ', '').replace(',', '').replace('\'', "")))
            self.sign = False
            if (digit[0] == '-'):
                self.sign = True
                digit = digit[1:]
            self.digits = [int(i) for i in digit]
            if self.sign and self.digits[0] == 0:
                self.sign = False
        except:
            print(digit)
            raise RuntimeError("Digit cannot be presented as integer.")

    # Что возвращается при вызове через "print()", "format()" и им подобное.
    def __str__(self):
        out = self.sign and '-' or ""
        out += str(''.join(map(str, self.digits)))
        return out

    # "len( Z() )", наследованный от N()::__len__() возвращает количество цифр в числе, знак не учитывается.
    def __len__(self):
        return len(self.digits)

    def __abs__(self):
        return Z(self.digits)

    def toN(self):
        if (self.sign):
            raise RuntimeError("Z", str(self), "cannot be presented as N.")
        return N(str(self))

    def toQ(self):
        return Q(self)

    def toPoly(self):
        return poly(self)

    def __gt__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '>')
        if self.sign and other.sign:
            return abs(self).toN() < abs(other).toN()
        elif not (self.sign or other.sign):
            return abs(self).toN() > abs(other).toN()
        elif self.sign:
            return False
        else:
            return True

    def __lt__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '<')
        if self.sign and other.sign:
            return abs(self).toN() > abs(other).toN()
        elif not (self.sign or other.sign):
            return abs(self).toN() < abs(other).toN()
        elif self.sign:
            return True
        else:
            return False

    def __le__(self, other):
        return not (self > other)

    def __ge__(self, other):
        return not (self < other)

    def __eq__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '==')
        if self.sign == other.sign:
            return abs(self).toN() == abs(other).toN()
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, "+")
        if self.sign and other.sign:
            return Z('-'+str(abs(self).toN()+abs(other).toN()))
        if not (self.sign or other.sign):
            return Z(self.toN()+other.toN())
        elif self.sign:
            return Z(other.toN() - abs(self).toN())
        else:
            return Z(self.toN() - abs(other).toN())




    def __mul__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, "*")
        return Z(("-" if self.sign ^ other.sign else "") + str(abs(self).toN() * abs(other).toN()))

    def __floordiv__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, "//")
        res = abs(self).toN() // abs(other).toN()
        m = abs(self).toN()%abs(other).toN()
        if self.sign and m != N(0):
            res = res + N(1)
        return Z(("-" if self.sign ^ other.sign else "") + str(res))

    def __truediv__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, "/")
        if (self % other == Z(0)):
            return self // other
        else:
            return Q(self, other)

    def __mod__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, "%")
        return self - self // other * other

    def __sub__(self, other):
        if type(self) != type(other):
            tryReverseOp(self, other, "-")
        other = other * Z(-1)
        return self + other

    def __neg__(self):
        return Z(-1)*self