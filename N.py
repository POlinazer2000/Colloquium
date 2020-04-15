#
# [McM]: Не забыть перевести кодировку FAR'а в UTF-8!!!
#
class Z:
    pass
class N:
    # Инициализация класса.
    # Здесь: списку "N.digits" присваивается значение первого аргумента (тип: int).
    #Пример: "N( 75044 )" создаст объект класса "N()" с "digits = [7, 5, 0, 4, 4]".
    def __init__(self, digit):
        self.digits = []
        try:
            digit = str(int(str(digit).replace('[', '').replace(']', '').replace(' ', '').replace(',', '')))
            self.digits = [int(i) for i in digit]
        except:
            raise RuntimeError( "Digit cannot be presented as integer > 0." )

    # Что возвращается при вызове через "print()", "format()" и им подобное.
    def __str__(self):
        return str(''.join(map(str, self.digits)))

    # Теперь вызов "len( N() )" даст длину не объекта, а длину списка цифр внутри него.
    def __len__( self ):
        return len( self.digits )

    # Проверка на возможность перевести запрос на более высокий уровень.
    def tryReverseOp( self, other, operator ):
        if ( isinstance( other, Z ) ):
            return eval( str( self.toZ() ) + operator + str( other ) )
        #if ( isinstance( other, Q ) ):
        #    return eval( str( self.toZ().toQ() ) + operator + str( other ) )
        return "NoRev"

    def toZ( self ):
        return Z( self.digits )


    # "Less than", "<"
    def __lt__( self, other ):
        if ( len( self ) < len( other ) ):
            return True
        elif ( len( self ) > len( other ) or ( self.digits == [ 0 ] and other.digits == [ 0 ] ) ):
            return False
        else:
            for i in range( len( self ) ):
                if self.digits[ i ] < other.digits[ i ]:
                    return True
                elif self.digits[ i ] > other.digits[ i ]:
                    return False
            return False
    # "<="
    def __le__(self, other):
        if ( len( self ) < len( other ) or ( self.digits == [ 0 ] and other.digits == [ 0 ] ) ):
            return True
        elif ( len( self ) > len( other ) ):
            return False
        else:
            for i in range( len( self ) ):
                if self.digits[ i ] < other.digits[ i ]:
                    return True
                elif self.digits[ i ] > other.digits[ i ]:
                    return False
            return True
    # "=="
    def __eq__(self, other):
        if ( len(self) != len(other) ):
            return False
        else:
            for i in range( len( self ) ):
                if self.digits[ i ] != other.digits[ i ]:
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
    def __add__( self, other ):
        #out = self.tryReverseOp( other, "+" )
        #if ( str( out ) != "noRev" ):
        #     return out

        if isinstance(other, int):
            other = N( other )
        elif not isinstance(other, N):
            raise RuntimeError( "Digit cannot be presented as integer > 0." )

        while ( len( self ) < len( other ) ):
            self.digits.insert( 0, 0 )
        while ( len( self ) > len( other ) ):
            other.digits.insert( 0, 0 )

        out = [ 0 ] * len( self )
        #print( self.digits, "+", other.digits, "; ", out, '\n' ) # 4debug.

        for i in range( len( self ) - 1, -1, -1 ):
            out[ i ] += self.digits[ i ] + other.digits[ i ]
            if ( out[ i ] > 9 ):
                if ( i == 0 ):
                    out.insert( 0, out[ i ] // 10 )
                else:
                    out[ i - 1 ] = out[ i ] // 10
                out[ i ] %= 10

        return N( int( str(''.join(map(str, out))) ) )
    

    # Перегрузка "/"
    def __truediv__(self, other):
        self.tryReverseOp(other, "/")
        out=0
        if (int(str(other)) >= 0 and int(str(self)) >= 0):
            for i in range(int(str(other))):
                out -= self.digits[ i ]
                if (out < 0 and i != 0):
                    out += self.digits[ i ]
                    break
                else:
                    out = 0
            out = list(str(out))
            return N(int(str(''.join(map(str, out)))))
        else:
            raise RuntimeError("Some of these digits is not N class")

    # Перегрузка "//"
    def __floordiv__( self, other ):
        return self / other

    # Перегрузка "-"
    def __sub__(self, other):
        self.tryReverseOp(other, "-")
    
        signMustExist = False
        
        if ( self < other ):
            self, other = other, self
            signMustExist = True

        while (len(self) < len(other)):
            self.digits.insert(0, 0)
        while (len(self) > len(other)):
            other.digits.insert(0, 0)

        out = [0] * ( len(self) + 1 )
        #print( self.digits, "-", other.digits, "; ", out, '\n' ) # 4debug.

        for i in range( len( self ), 0, -1 ):
            if ( self.digits[ i - 1 ] - other.digits[ i - 1 ] < 0 and i != 1 ):
                self.digits[ i - 2 ] -= 1
                self.digits[ i - 1 ] += 10
            out[ i ] += self.digits[ i - 1 ] - other.digits[ i - 1 ]
            #print( str( self.digits ), "-", str( other.digits ), "=", str( out ), ": (", out[ i ], "=", self.digits[i-1], "-", other.digits[i-1], ")" )
        
        while ( out and out[ 0 ] == 0 ):
            out.pop( 0 )

        if ( not out ):
            return N( 0 )
        elif ( signMustExist ):
            newz = Z( out )
            newz.sign = True
            return newz
        else:
            return N(int(str(''.join(map(str, out)))))
    '''if (out[i] < 0):
                #print( )
                #out[ i ] += 10 - ( self.digits[ i ] - other.digits[ i ] )
                if (i == 0):
                    #out = list( str( N( out ).toZ() )[ i ] for i in range( len( str ) ) )
                    #out.toZ()
                    #outZ = self.toZ()
                    out[ i ] = -out[ i ]
                    #mustBeZ = Zsign = True
                else:
                    for k in range (i-1,-1,-1):
                        if (out[k]!=0):
                            self.digits[k]-=1
                            out[i]+=10
                            #print( i, out[ i ])
                            #if out[ i ] < 0:
                            #    out[ i ] += 10
                        if (k==0):
                            mustBeZ = Zsign = True
                            #out[ i ]
                            #outZ = self.toZ()
                            #outZ.sign=True
        if (type(out)!=Z):
            return N(int(str(''.join(map(str, out)))))
        else:
            return Z(int(str(''.join(map(str, out)))))'''

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
        return N(self.digits+[0]*k)

    def __mul__(self, other):
        lst = []
        for i in range(len(other)):
            lst.append( self.muld(other.digits[-i-1]).mulk(i) )
        n = N(0)
        for i in lst:
            n = i + n
        return n

    def nzer(self):
        if self.digits[0]==0:
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
    #магия "/" здесь целая часть ( не уверен, что работает во всех случаях )
    def __truediv__(self, other):
        lst = []
        lst += self.digits
        tmp = N(lst)
        n = N(0)

        while tmp > other:
            n = n + N( tmp.divdk(other) )
            if tmp < N( tmp.divdk(other) ) * other:
                break
            tmp = tmp - N( tmp.divdk(other) ) * other
        return n
    # "%"
    def __mod__(self, other):
        n = self / other
        n = n * other
        n = self - n
        return n
    # НОД, пока в виде метода
    def gcd(self, other):
        lst1 = []
        lst2 = []
        lst1 += self.digits
        lst2 += other.digits
        tmp1 = N(lst1)
        tmp2 = N(lst2)
        while tmp2 != N(0):
            tmp1 = tmp1 % tmp2
            tmp1, tmp2 = tmp2, tmp1
        return tmp1
    # НОК
    def lcm(self,other):
        res = self * other
        res = res / self.gcd(other)
        return res
print( N(120) % N(11))
n1 = N(120)
n2 = N(48)
print( n1.lcm(n2))

