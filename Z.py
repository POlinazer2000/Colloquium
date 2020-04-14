#
# [McM]: Не забыть перевести кодировку FAR'а в UTF-8!!!
#


class Z( N ):
    # Инициализация класса.
    # Здесь: списку "Z.digits" присваивается значение первого аргумента (тип: int).
    #Пример: "Z( -1234 )" создаст объект класса "Z()" с "digits = [1, 2, 3, 4]" и "sign = True".
    def __init__(self, digit):
        try:
            digit = str(int(str(digit).replace('[', '').replace(']', '').replace(' ', '').replace(',', '')))
            self.sign = False
            if (digit[0] == '-'):
                self.sign = True
                digit = digit[1:]
            self.digits = [int(i) for i in digit]
        except:
            raise RuntimeError("Digit cannot be presented as integer.")

    # Что возвращается при вызове через "print()", "format()" и им подобное.
    def __str__(self):
        out = self.sign and '-' or ""
        out += str(''.join( map( str, self.digits )))
        return out

    # "len( Z() )", наследованный от N()::__len__() возвращает количество цифр в числе, знак не учитывается.

    def __abs__( self ):
        return Z( list( map( abs, self.digits ) ) )

    def toN( self ):
        if ( self < Z( 0 ) ):
            raise RuntimeError( "Z", str( self ), "cannot be presented as N." )
        return N( int( str( self ) ) )

    def toQ( self ):
        return Q( self.digits, 1 )

    # Нет проверки на знак!
    def __lt__( self, other ):
        if ( len( self ) < len( other ) ):
            return True
        elif ( len( self ) > len( other ) ):
            return False
        else:
            for i in range( len( self ), 0, -1 ):
                if self.digits[ i ] < other.digits[ i ]:
                    return True
                elif self.digits[ i ] > other.digits[ i ]:
                    return False
            # Long check must be here...
            return True

    def __gt__( self, other ):
        if ( len( self ) > len( other ) ):
            return True
        elif ( len( self ) < len( other ) ):
            return False
        else:
            # Long check must be here...
            return True

    def __le__( self, other ):
        return not ( self > other )
    
    def __ge__( self, other ):
        return not ( self < other )

    def __add__( self, other ):
        if ( abs( self ) > abs( other ) ):
            out = "-" if self < Z( 0 ) else ""
            out += str( N( int(str(abs(self))) ) ) + N( int(str(abs(other))) )
        else:
            out = "-" if other < Z( 0 ) else ""
            out += str( abs( other ).toN() + abs( self ).toN() )
        return Z( int( out ) )


#print( Z( 33 ) + Z( -108 ) )

