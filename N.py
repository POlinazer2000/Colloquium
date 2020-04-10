#
# [McM]: Не забыть перевести кодировку FAR'а в UTF-8!!!
#

class N:
    # Инициализация класса.
    # Здесь: списку "N.digits" присваивается значение первого аргумента (тип: int).
    #Пример: "N( 75044 )" создаст объект класса "N()" с "digits = [7, 5, 0, 4, 4]".
    def __init__(self, digit):
        self.digits = []
        if isinstance(digit, (list, tuple)):
            try:
                digit = int("".join( map( str, digit ) )) # Костыли, можно и не убирать.
            except:
                raise RuntimeError("Digit cannot be presented as integer > 0.")
        elif isinstance(digit, int):
            try:
                self.digits = [int(i) for i in str(digit)]
                self.deg = len( str( digit ) )
            except:
                raise RuntimeError("Digit cannot be presented as integer > 0.")

    # Что возвращается при вызове через "print()", "format()" и им подобное.
    def __str__(self):
        return str(''.join(map(str, self.digits)))

    # Теперь вызов "len( N() )" даст длину не объекта, а длину списка цифр внутри него.
    def __len__( self ):
        return len( self.digits )



    # Переопределение сложения.
    def __add__( self, other ):
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



#print( N( 33 ) + N( 108 ) )