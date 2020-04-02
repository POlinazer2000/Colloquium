class Q:
    def __init__( self, num, denum ):
        if num is Z and denum is N:
            self.num = num      # Числитель.
            self.denum = denum  # Знаменатель.
        else:
            raise RuntimeError( "Num is not a Z-class or denum is not a N-class." )

    def __str__( self ):
        print( self.num, '/', self.denum, sep = '' )

