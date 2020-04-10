
class Z():
    # Инициализация класса.
    # Здесь: списку "Z.digits" присваивается значение первого аргумента (тип: int).
    #Пример: "Z( -1234 )" создаст объект класса "Z()" с "digits = [1, 2, 3, 4]" и "sign = True".
    def __init__(self, digit):
        digit = str(int(str(digit).replace('[', '').replace(']', '').replace(' ', '').replace(',', '')))
        try:
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

    # "len( Z() )" возвращает количество цифр в числе, знак не учитывается.
    def __len__( self ):
        return len( self.digits )

    def __abs__( self ):
        return Z( list( map( abs, self.digits ) ) )

    def toN( self ):
        if ( self < Z( 0 ) ):
            raise RuntimeError( "Z", str( self ), "cannot be presented as N." )
        return N( int( str( self ) ) )

    def __lt__( self, other ):
        if ( len( self ) < len( other ) ):
            return True
        elif ( len( self ) > len( other ) ):
            return False
        else:
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


    def __add__( self, other ):
        if ( abs( self ) > abs( other ) ):
            out = "-" if self < Z( 0 ) else ""
            out += str( N( int(str(abs(self))) ) ) + N( int(str(abs(other))) )
        else:
            out = "-" if other < Z( 0 ) else ""
            out += str( abs( other ).toN() + abs( self ).toN() )
        return Z( int( out ) )


print( Z( 33 ) + Z( -108 ) )
