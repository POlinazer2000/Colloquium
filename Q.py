class Q():
    def __init__(self, num, denum = N(1) ):
        if isinstance( num, N ):
            self.num = Z( num.digits )
        elif isinstance( num, Z):
            self.num = Z( num.orig )
        else:
            self.num = Z( num )

        if isinstance( denum, Z ):
            if denum.sign:
                self.num = mul_zm_z( self.num )
            self.denum = trans_z_n( denum )
        elif isinstance( denum, N):
            self.denum = denum
        else:
            self.denum = N( denum )

        #self.num = num # Числитель.
        #self.denum = denum  # Знаменатель.
        if not nzer_n_b( self.denum ) :
            raise ZeroDivisionError("Divided by zero")
    def __str__(self):
        res = str(self.num) + ( str(self.denum) != '1' and "/{}".format(self.denum) or "" ) #если знаменатель == 1, не пишется
        #res = "{}/{}".format(self.num, self.denum)
        return res