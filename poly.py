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
