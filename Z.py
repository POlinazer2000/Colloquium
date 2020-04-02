
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
