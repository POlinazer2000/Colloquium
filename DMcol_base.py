
class N:
    def __init__( self, digit ):
        self.digits = []
        if isinstance( digit, ( list, tuple ) ):
            try:
                self.digits = [ int( i ) for i in digit ]
            except:
                raise RuntimeError( "Digit cannot be presented as integer > 0." )
        elif isinstance( digit, int ):
            try:
                self.digits = [ int( i ) for i in str( digit ) ]
            except:
                raise RuntimeError( "Digit cannot be presented as integer > 0." )
        #print( self.digits )

    def __str__( self ):
		return str( ''.join( map( str, self.digits ) ) )


class Z( N ):
    def __init__( self, digit ):
        digit = str( digit ).replace( '[', '' ).replace( ']', '' ).replace( ' ', '' ).replace( ',', '' )
        try:
            self.sign = False
            if ( digit[ 0 ] == '-' ):
                self.sign = True
                digit = digit[ 1 : ]
            self.digits = [ int( i ) for i in digit ]
        except:
            raise RuntimeError( "Digit cannot be presented as integer." )

    def __str__( self ):
        out = "" if not self.sign else "-" 
        out += str( ''.join( str( self.digits ) ) )
        return out


class Q:
    def __init__( self, num, denum ):
        if num is Z and denum is N:
            self.num = num      # Числитель.
            self.denum = denum  # Знаменатель.
        else:
            raise RuntimeError( "Num is not a Z-class or denum is not a N-class." )

    def __str__( self ):
        print( self.num, '/', self.denum, sep = '' )


'''class polynom:
    def __init__( self, coeflist ):
        self.coef = []
        for i in range( len( coeflist ) ):
            if not isinstance( coeflist[ i ], ( N, Z, Q ) ):
                raise RuntimeError( "Coefficient[ " + str( i ) + " ] == '" + str( coeflist[ i ] ) + "': num is not a Z-class or denum is not a N-class." )
            else:
                self.coef.append( coeflist[ i ] ) # Список коэффицентов, начиная со старшего.
            #self.coef = coeflist # Список коэффицентов, начиная со старшего.

    def __str__( self ):
        coef, out = self.coef, ""
        if len( coef ) == 0:
            out = "0"
        else:
            if len( coef ) > 2:
                while ( str( coef[ 0 ] ) == '0' ):
                    coef = coef[ 1 : ]
            if len( coef ) > 2:
                out += "" if str( coef[ 0 ] ) == '1' else ( "-" if str( coef[ 0 ] ) == '-1' else str( coef[ 0 ] ) )
                out += "x^" + str( len( coef ) - 1 )

                for i in range( 1, len( coef ) - 2 ):
                    if ( str( coef[ i ] ) != '0' ):
                        out += "+" if str( coef[ i ] ) == '1' else ( "-" if str( coef[ i ] ) == '-1' else ( "+" + str( coef[ i ] ) if coef[ i ] > 0 else str( coef[ i ] ) ) )
                        out += "x^" + str( len( coef ) - i - 1 )
            
            if len( coef ) > 1 and coef[ -2 ] != 0:
                out += ( "+" if str( coef[ -2 ] ) == 1 and len( coef ) > 1 else ( "-" if str( coef[ -2 ] ) == -1 else ( "+" + str( coef[ -2 ] ) if coef[ -2 ] > 0 and len( coef ) > 1 else str( coef[ -2 ] ) ) ) ) + "x"
            if len( coef ) > 0 and coef[ -1 ] != 0:
                out += "+" + str( coef[ -1 ] ) if coef[ -1 ] > 0 and len( coef ) > 1 else str( coef[ -1 ] )

        return out
''' # Reserved.


#poly = polynom( [ N([0]), N([3]), N([0]), Z([-1]) ] )
#print( "f(x) =", poly )

print( N( [ 1, 3 ] ) )
q1 = Q( Z( [ 2 ] ), N( 1 ) )

print("Hello world!")
q1 = Q( Z( -24 ), N( 142 ) )
