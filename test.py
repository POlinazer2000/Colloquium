def tryReverseOp(a, b, op):
    crutch = {type(N(0)): 1,
              type(Z(0)): 2,
              type(Q(0)): 3,
              type(poly(0)): 4
              }

    # print( type( a ), type( b ) )
    # print( type(N(0)), type(Z(0)), type(Q(0)), type(poly(0)) )
    # print( a, op, b, ": ", type( a ), type( b ) )
    # print( self, "__add__", other, ": ", type( self ), type( other ) )
    try:
        if crutch[type(a)] < crutch[type(b)]:
            return eval('type(b)(a)' + op + 'b')
        else:
            # print( str( a ) + op + str( eval( "type(a)(b)" ) ) )
            return eval("a" + op + 'type(a)(b)')
    except:
        print(a, op, b, ": ", type(a), type(b))
        raise RuntimeError


#
# [McM]: Не забыть перевести кодировку FAR'а в UTF-8!!!
#

class N:
    # Инициализация класса.
    # Здесь: списку "N.digits" присваивается значение первого аргумента (тип: int).
    # Пример: "N( 75044 )" создаст объект класса "N()" с "digits = [7, 5, 0, 4, 4]".
    def __init__(self, digit):
        self.digits = []
        try:
            digit = str(int(str(digit).replace('[', '').replace(']', '').replace(' ', '').replace(',', '')))
            self.digits = [int(i) for i in digit]
        except:
            raise RuntimeError("Digit cannot be presented as integer > 0.")

    # Что возвращается при вызове через "print()", "format()" и им подобное.
    def __str__(self):
        return str(''.join(map(str, self.digits)))

    # Теперь вызов "len( N() )" даст длину не объекта, а длину списка цифр внутри него.
    def __len__(self):
        return len(self.digits)

    # Проверка на возможность перевести запрос на более высокий уровень.

    def toZ(self):
        return Z(self.digits)

    def toQ(self):
        return Q(self, 1)

    def toPoly(self):
        return poly(self)

    # "Less than", "<"
    def __lt__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '<')
        if (len(self) < len(other)):
            return True
        elif (len(self) > len(other) or (self.digits == [0] and other.digits == [0])):
            return False
        else:
            for i in range(len(self)):
                if self.digits[i] < other.digits[i]:
                    return True
                elif self.digits[i] > other.digits[i]:
                    return False
            return False

    # "<="
    def __le__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '<=')
        if (len(self) < len(other) or (self.digits == [0] and other.digits == [0])):
            return True
        elif (len(self) > len(other)):
            return False
        else:
            for i in range(len(self)):
                if self.digits[i] < other.digits[i]:
                    return True
                elif self.digits[i] > other.digits[i]:
                    return False
            return True

    # "=="
    def __eq__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '==')
        if (len(self) != len(other)):
            return False
        else:
            for i in range(len(self)):
                if self.digits[i] != other.digits[i]:
                    return False
            return True

    # "!="
    def __ne__(self, other):
        return not self == other

    # ">"
    def __gt__(self, other):
        return not self <= other

    # ">="
    def __ge__(self, other):
        return not self < other

    # Переопределение сложения.
    def __add__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '+')

        while (len(self) < len(other)):
            self.digits.insert(0, 0)
        while (len(self) > len(other)):
            other.digits.insert(0, 0)

        out = [0] * len(self)
        # print( self.digits, "+", other.digits, "; ", out, '\n' ) # 4debug.

        for i in range(len(self) - 1, -1, -1):
            out[i] += self.digits[i] + other.digits[i]
            if (out[i] > 9):
                if (i == 0):
                    out.insert(0, out[i] // 10)
                    out[i+1] %= 10
                else:
                    out[i - 1] = out[i] // 10
                out[i] %= 10

        return N(''.join(map(str, out)))

    # Перегрузка "-"
    def __sub__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '-')
        signMustExist = False

        if (self < other):
            self, other = other, self
            signMustExist = True

        while (len(self) < len(other)):
            self.digits.insert(0, 0)
        while (len(self) > len(other)):
            other.digits.insert(0, 0)

        out = [0] * (len(self) + 1)
        # print( self.digits, "-", other.digits, "; ", out, '\n' ) # 4debug.

        for i in range(len(self), 0, -1):
            if (self.digits[i - 1] - other.digits[i - 1] < 0 and i != 1):
                self.digits[i - 2] -= 1
                self.digits[i - 1] += 10
            out[i] += self.digits[i - 1] - other.digits[i - 1]
            # print( str( self.digits ), "-", str( other.digits ), "=", str( out ), ": (", out[ i ], "=", self.digits[i-1], "-", other.digits[i-1], ")" )

        while (out and out[0] == 0):
            out.pop(0)

        if (not out):
            return N(0)
        elif (signMustExist):
            newz = Z(out)
            newz.sign = True
            return newz
        else:
            return N(''.join(map(str, out)))

    def muld(self, d):
        t = 0
        lst = []
        lst += self.digits
        for i in range(1, len(self) + 1):
            lst[-i] *= d
            lst[-i] += t
            t = lst[-i] // 10
            lst[-i] %= 10
        if t:
            lst.insert(0, t)
        return N(lst)

    def mulk(self, k):
        return N(self.digits + [0] * k)

    # "*"
    def __mul__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '*')
        lst = []
        for i in range(len(other)):
            lst.append(self.muld(other.digits[-i - 1]).mulk(i))
        n = N(0)
        for i in lst:
            n = i + n
        return n

    def nzer(self):
        if self.digits[0] == 0:
            return False
        return True

    # степень частного с первой цифрой
    def divdk(self, other):
        k = 0
        while self >= other.mulk(k):
            k += 1

        k -= 1
        res = 9

        while self < other.muld(res).mulk(k):
            res -= 1
        return res * 10 ** k

    # магия "//" здесь целая часть ( не уверен, что работает во всех случаях )
    def __floordiv__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '//')
        lst = []
        lst += self.digits
        tmp = N(lst)
        n = N(0)

        while tmp >= other:
            n = n + N(tmp.divdk(other))
            if tmp < N(tmp.divdk(other)) * other:
                break
            tmp = tmp - N(tmp.divdk(other)) * other
        return n

    # "%"
    def __mod__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '%')
        n = self // other
        n = n * other
        n = self - n
        return n

    # Перегрузка "/"
    def __truediv__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '//')
        if (self % other == N(0)):
            return self // other
        else:
            return Q(self, other)

    # НОД, пока в виде метода
    def gcd(self, other):
        # в этом варианте self не будет изменен
        lst1 = []
        lst2 = []
        lst1 += self.digits
        lst2 += other.digits
        tmp1 = N(lst1)
        tmp2 = N(lst2)
        '''tmp1 = self
        tmp2 = other'''
        while tmp2 != N(0):
            tmp1 = tmp1 % tmp2
            tmp1, tmp2 = tmp2, tmp1
        return tmp1

    # НОК
    def lcm(self, other):
        res = self * other
        res = res / self.gcd(other)
        return res


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
                self.num = self.num * Z(-1)
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

    def red(self):
        gcd = self.denum.gcd(abs(self.num).toN())
        num = self.num / gcd
        denum = self.denum / gcd
        return Q(num, denum)

    def ifZ(self):
        if self.num % self.denum == Z(0):
            return True
        else:
            return False

    def toN(self):
        if (self.ifZ and (self.num // self.denum >= Z(0))):
            return N(str(self.num // self.denum))
        else:
            raise RuntimeError("Z", str(self), "cannot be presented as N.")

    def toZ(self):
        if (self.ifZ):
            return Z(str(self.num // self.denum))
        else:
            raise RuntimeError("Z", str(self), "cannot be presented as N.")

    def toPoly(self):
        return poly(self)

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
        denum = self.denum * other.denum
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
        tmp = self / other
        mod = tmp.num % tmp.denum
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


class poly():
    # Здесь: poly() имеет в себе одну переменную-словарь "coef", в которой хранятся
    # значения по шаблону { <степень>: <Q-объект>, ... }.
    # Пример: poly( {23: Q( 3, 4 ), 7: Q( -4 )} ) будет выглядеть как "3/4 * x^23 - 4 * x^7".
    def __init__(self, coeflist):
        self.coef = {}

        if isinstance(coeflist, list):
            for i in range(len(coeflist)):
                if not isinstance(i, Q):
                    self.coef.update({i: Q(coeflist[i])})
                else:
                    self.coef.update({i: coeflist[i]})
        elif isinstance(coeflist, dict):
            for i in coeflist:
                if isinstance(coeflist[i], Q):
                    self.coef.update({i: coeflist[i]})
                else:
                    self.coef.update({i:Q(coeflist[i])})

        elif isinstance(coeflist, (Z, N)):
            self.coef = {0: coeflist.toQ()}
        elif isinstance(coeflist, Q):
            self.coef = {0: coeflist}
        elif isinstance(coeflist, str):
            lst = coeflist.split(' ')
            for i in range(len(lst)):
                self.coef.update({i: Q(lst[-i - 1])})
        coeflist = self.coef.copy()
        for i in self.coef.keys():
            if str(self.coef[i]) == "0":  # A-a-argh, beautiful crutch!..
                coeflist.pop(i)
        self.coef = coeflist.copy()

        if len(self.coef) == 0:
            self.coef.update({0: Q(0)})

    def __str__(self):
        coef, out = self.coef, ""
        if self.lead()==Q(0):  # Not "self.deg()" (see "poly({ 0: Q( 1 ) })").
            out = "0"
        else:
            key = sorted(list(coef.keys()))[::-1]

            for i in key:
                if coef[i].num.sign == False:
                    out+='+'
                if coef[i] == Q(1):
                    pass
                elif coef[i] == Q(-1):
                    out+='-'
                else:
                    out+= str(coef[i])
                if i > 1:
                    out+='x^{}'.format(i)
                elif i == 1:
                    out += 'x'
                else:
                    if coef[i]==Q(1):
                        out+=str(coef[i])
            if out[0]=='+':
                out = out[1:]
        return out

    # Степень и длина списка коэффициентов многочлена.
    def __len__(self):
        return len(list(self.coef.keys()))

    def deg(self):
        return max(list(self.coef.keys()))

    # Ведущий (самый старший) аргумент
    def lead(self):
        return self.coef[self.deg()]

    # Перегрузка операторов.

    def __add__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '+')
        tmp = {}
        tmp.update(self.coef)
        for i in other.coef:
            if i in tmp:
                tmp[i] = tmp[i] + other.coef[i]
            else:
                tmp.update({i: other.coef[i]})
        return poly(tmp)

    def __sub__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '-')
        tmp = {}
        tmp.update(self.coef)
        for i in other.coef:
            if i in tmp:
                tmp[i] = tmp[i] - other.coef[i]
            else:
                tmp.update({i: Z(-1) * other.coef[i]})
        return poly(tmp)

    def mulq(self, q):
        out = poly(self.coef)
        for i in out.coef:
            out.coef[i] = out.coef[i] * q
        return out

    def mulqx(self, q, k):
        key = self.coef.keys()
        out = {}
        for i in key:
            out[i + k] = self.coef[i] * q
        return poly(out)

    def __mul__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '*')
        if deg(self) < deg(other):
            self, other = other, self
        out = poly(0)
        for i in other.coef.keys():
            out = out + self.mulqx(other.coef[i], i)
        return out

    '''
        out = {}
        for i in self.coef:
            for j in other.coef:
                if i+j in out:
                    out[i+j] = out[i+j] + self.coef[i] * other.coef[j]
                else:
                    out.update({i+j:self.coef[i] * other.coef[j]})
        return poly(out)'''

    def factor_P(self):
        a = poly(self.coef)
        g = abs(a.coef[0].num).toN().gcd(abs(a.coef[0].num).toN())
        l = a.coef[0].denum.lcm(a.coef[0].denum)
        for i in range(1, len(a.coef)):
            g = g.gcd(abs(a.coef[0].num))
            l = l.lcm(a.coef[i].denum)
        return Q(g, l)

    # вернет целую часть
    def __truediv__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '/')
        p1 = poly(self.coef)
        p2 = poly(other.coef)
        res = poly(0)
        while (p1.deg() >= p2.deg()):
            dif = p1.deg() - p2.deg()
            q = p1.lead() / p2.lead()
            res = res + poly({dif: q})
            p1 = p1 - p2.mulqx(q, dif)
        r = p1
        return res

    def __mod__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '%')
        p1 = poly(self.coef)
        p2 = poly(other.coef)
        res = poly(0)
        while (p1.deg() >= p2.deg()):
            dif = p1.deg() - p2.deg()
            q = p1.lead() / p2.lead()
            res = res + poly({dif: q})
            p1 = p1 - p2.mulqx(q, dif)
        return p1

    def __floordiv__(self, other):
        if type(self) != type(other):
            return tryReverseOp(self, other, '//')
        return self / other

    def gcd(self, other):
        poly1 = poly(self.coef)
        poly2 = poly(other.coef)
        while poly2.deg() > 0:
            poly1 = poly1 % poly2
            poly1, poly2 = poly2, poly1

        poly1 = poly1.mulq(Q(1)/ poly1.lead())
        return poly1

    # Производная многочлена.
    def der(self):
        poly_derivative = poly(0)
        pol = poly(self.coef)
        for i in pol.coef:
            if i:
                poly_derivative = poly_derivative + poly({i - 1: Q(i) * pol.coef[i]})
        return poly_derivative

    # кратные корни в простые
    def nmr(self):
        der = self.der()
        gcd = self.gcd(der)
        res = self / gcd
        return res


# print( poly({  -4: Q( 5, 4 )  }) + poly({  -4: Q( 7, 17 ), 17: Q( -3 )  }) )
print(poly('1 2 2'))
print(poly('2 2')/poly('1 1'))
print(poly('1 2 1').gcd(poly('2 2')))
print(poly('1 -20 175 -878 2779 -5744 7737 -6534 3132 -648').nmr())
print(poly({100:1})/poly({100:1}))
