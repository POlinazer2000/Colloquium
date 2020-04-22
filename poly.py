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
                if coef[i] == Q(1) and i != 0:
                    pass
                elif coef[i] == Q(-1) and i != 0:
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
